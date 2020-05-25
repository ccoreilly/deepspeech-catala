#!/usr/bin/env python

import argparse
import os
import importlib
import sys

from deepspeech_training.util.text import Alphabet


def get_validate_label(args):
    if 'validate_label_locale' not in args or (args.validate_label_locale is None):
        print('ERROR: Required --validate_label_locale not specified. Please check.')
        return None
    if not os.path.exists(os.path.abspath(args.validate_label_locale)):
        print('ERROR: Inexistent --validate_label_locale specified. Please check.')
        return None
    module_dir = os.path.abspath(os.path.dirname(args.validate_label_locale))
    sys.path.insert(1, module_dir)
    fname = os.path.basename(args.validate_label_locale).replace('.py', '')
    locale_module = importlib.import_module(fname, package=None)
    return locale_module.validate_label

def process_data(input, print_invalid):
    input_file = os.path.abspath(input)
    if os.path.isfile(input_file):
        with open(input_file, encoding="utf-8") as input_file_data:
            for line in input_file_data:
                if line == 'wav_filename,wav_filesize,transcript\n':
                    print(line)
                    continue
                data = line.split(',')
                label = label_filter_fun(data[2])
                if label is not None and print_invalid is False: 
                        print(f"{data[0]},{data[1]},{label}") 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cleans labels for LM generation")
    parser.add_argument(
        "input",
        help="Text file containing the training data as expected by DeepSpeech",
    )
    
    parser.add_argument(
        "--validate_label_locale",
        help="Path to a Python file defining a |validate_label| function for your locale.")

    parser.add_argument(
        "--filter_alphabet",
        help="Exclude samples with characters not in provided alphabet",
    )

    parser.add_argument(
        "--print_invalid",
        action="store_true",
        help="Prints invalid labels instead of valid ones",
    )


    PARAMS = parser.parse_args()
    validate_label = get_validate_label(PARAMS)

    ALPHABET = Alphabet(PARAMS.filter_alphabet) if PARAMS.filter_alphabet else None

    def label_filter_fun(label):
        validated_label = validate_label(label)
        if (PARAMS.print_invalid and validated_label is None):
            print(label, end='')
        
        if ALPHABET and validated_label:
            try:
                ALPHABET.encode(validated_label)
            except KeyError:
                validated_label = None
                if (PARAMS.print_invalid and validated_label is None):
                    print(label, end='') 
        return validated_label

    process_data(PARAMS.input, PARAMS.print_invalid)
