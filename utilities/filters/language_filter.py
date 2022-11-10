# this programm takes a csv file that contains tweets in multiple languages and returns on csv file with the tweets in latinised arabic.

import csv
import re
from polyglot.detect import Detector

# read the csv file


def read_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


# filter out tweets that are in in english, german, spanish, french or italian with the help of polyglot
def filter_lang(data):
    filtered_data = []

    for tweet in data:
        if len(Detector(tweet[0], quiet=True).language.code) == 2:
            pass
        else:
            filtered_data.append(tweet)
        
    return filtered_data


def write_csv(data, file):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == '__main__':
    countries_array = ['algeria', 'egypt', 'ksa', 'jordan',
                       'lebanon', 'qatar', 'uae', 'qatar', 'morocco']
    for country in countries_array:
        data = read_csv(
            './external_resources/Tweets/clean_only/clean_' + country + '.csv')
        filtered_data = filter_lang(data)
        write_csv(filtered_data,
                  './external_resources/Tweets/latin_arabic_only/arabizi_'+country+'.csv')
