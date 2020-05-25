#!/usr/bin/env python

import argparse
import os


def process_data(params):
    input_file = os.path.abspath(params.input)
    min_words = int(params.min_words) if params.min_words is not None else 0
    max_words = int(params.max_words) if params.max_words is not None else float('inf')
    if os.path.isfile(input_file):
        with open(input_file, encoding="utf-8") as input_file_data:
            for line in input_file_data:
                data = line.split(',')
                sentence = data[2].rstrip('\n')
                word_len = len(sentence.split())
                if (min_words <= word_len <= max_words):
                    print(f"{data[0]},{data[1]},{sentence}") 
                    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cleans labels for LM generation")
    parser.add_argument(
        "input",
        help="Text file containing the training data as expected by DeepSpeech",
    )
    
    parser.add_argument(
        "--min_words",
        help="Minimum number of words a sentence has to have in order to be kept. Default is 0.")

    parser.add_argument(
        "--max_words",
        help="Maximum number of words a sentence has to have in order to be kept. Default is infinite.",
    )


    PARAMS = parser.parse_args()

    process_data(PARAMS)
