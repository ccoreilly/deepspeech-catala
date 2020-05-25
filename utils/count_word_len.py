#!/usr/bin/env python

import argparse
import os


def process_data(params):
    input_file = os.path.abspath(params.input)
    if os.path.isfile(input_file):
        with open(input_file, encoding="utf-8") as input_file_data:
            word_len_dict = {}
            max_word_len = 0
            total_occ = 0
            for line in input_file_data:
                if line == 'wav_filename,wav_filesize,transcript\n':
                    continue
                
                data = line.split(',')
                sentence = data[2].rstrip('\n')
                word_len = len(sentence.split())
                word_len_dict[word_len] = word_len_dict.get(word_len, 0) + 1
                max_word_len = word_len if word_len > max_word_len else max_word_len
                total_occ = total_occ + 1
            
            acc_occ = 0
            print('Count\tOccur.\t%\t%acc')
            for x in range(max_word_len):
                occ = word_len_dict.get(x, 0)
                acc_occ = acc_occ + occ
                if acc_occ / total_occ > 0.05:
                    print(f"{x}\t{occ}\t{occ/total_occ*100:.2f}\t{acc_occ/total_occ*100:.2f}")
                if acc_occ / total_occ > 0.95:
                    break;
                    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cleans labels for LM generation")
    parser.add_argument(
        "input",
        help="Text file containing the labels. One label per row",
    )


    PARAMS = parser.parse_args()

    process_data(PARAMS)
