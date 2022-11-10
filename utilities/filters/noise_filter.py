# this programm takes a csv file that contains tweets as values and removes hashtags, urls and mentions and returns a csv file with the filtered data
#
import csv
import re
import langdetect

# read the csv file


def read_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


# filter out hashtags, urls, mentions and duplicates from the tweets
def filter_noise(data):
    filtered_data = []
    for tweet in data:
        tweet[0] = re.sub(r'#[\w]+', '', tweet[0])
        tweet[0] = re.sub(r'@[a-zA-Z0-9_]+', '', tweet[0])
        tweet[0] = re.sub(r'http\S+', '', tweet[0])
        if tweet[0] not in filtered_data:
            filtered_data.append(tweet)
    return filtered_data

# get the filtered data and write it to a csv file


def write_csv(data, file):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


# main function
if __name__ == '__main__':
    countries_array = ['algeria', 'egypt', 'ksa', 'jordan',
                       'lebanon', 'qatar', 'uae', 'qatar', 'morocco', 'kuwait']
    for country in countries_array:
        data = read_csv(
            './external_resources/Tweets/latin_only/latinized_' + country + '.csv')
        filtered_data = filter_noise(data)
        write_csv(filtered_data,
                  './external_resources/Tweets/clean_only/clean_'+country+'.csv')
