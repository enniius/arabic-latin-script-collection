# recieves a csv file and a column number and returns a list of the values in that column then write it in csv file using pandas

import pandas as pd


def csv_column_extracter(csv_file, column_number):
    # read the csv file
    df = pd.read_csv('./external_resources/Tweets/dirty' + csv_file)
    # extract the column
    column = df.iloc[:, column_number]
    # write the column to a new csv file
    column.to_csv('./external_resources/Tweets/tweet_text_of_' +
                  csv_file, index=False)


if __name__ == '__main__':
    countries_array = ['algeria', 'egypt', 'ksa', 'jordan',
                       'lebanon', 'qatar', 'uae', 'qatar', 'morocco', 'kuwait']
    for country in countries_array:
        csv_column_extracter(country + '.csv', 1)
