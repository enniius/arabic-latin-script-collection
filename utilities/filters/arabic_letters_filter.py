# takes a csv file and removes tweets with arabic letters and return csv file with the filtered data

import csv
import re

# read the csv file


def read_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

# filter the tweets from arabic letters.


def filter_arabic_letters(data):
    filtered_data = []
    for tweet in data:
        if re.search(r'[أ-ي]', tweet[0]):
            continue
        else:
            filtered_data.append(tweet)
    return filtered_data


# write the filtered tweets to a new csv file with the same name
def write_csv(file, data):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == '__main__':
    countries_array = ['algeria', 'egypt', 'ksa', 'jordan',
                       'lebanon', 'qatar', 'uae', 'qatar', 'morocco', 'kuwait']
    for country in countries_array:
        data = read_csv('./external_resources/Tweets/text_only/tweet_text_of_' + country + '.csv')
        filtered_data = filter_arabic_letters(data)
        write_csv('./external_resources/Tweets/latin_only/latinized_' +
                  country + '.csv', filtered_data)
