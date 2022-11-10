# takes an unfiltered csv file and runs it through the pipeline to produce a filtered csv file of latinised arabic tweets

import csv
import os
import sys

from filters.arabic_letters_filter import filter_arabic_letters
from filters.language_filter import filter_lang
from filters.noise_filter import filter_noise

def read_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data



def write_csv(data, file):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


# give pathname after the script name
if __name__ == '__main__':
    fn = sys.argv[1]
    if not os.path.exists(fn):
        print('File not found')
        exit(1)
    data = read_csv(fn)
    no_arabic_letters_data = filter_arabic_letters(data)
    noise_filtered_data = filter_noise(no_arabic_letters_data)
    no_foreign_language_data = filter_lang(noise_filtered_data)
    second_noise_filtered_data = filter_noise(no_foreign_language_data)

    write_csv(second_noise_filtered_data, fn[:-4] + '_filtered.csv')
