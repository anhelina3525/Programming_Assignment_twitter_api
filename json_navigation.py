"""
This module lets you see
the different elements of a json file
containing information about the people you follow
on twitter.
"""
import json
import argparse
from twitter2 import get_dict_twitter
def main():
    def parser():
        """
        Parses the arguments passed by the user.
        """
        our_parser = argparse.ArgumentParser()
        our_parser.add_argument('account', type=str,
                                help='The account you want\
                                to view information about')
        args = our_parser.parse_args()
        return args

    def create_json():
        """
        Takes a dictionary with information from twitter,
        creates a json file and turns the contents
        of a dictionary into json format.
        """
        account = parser().account
        twitter_dict = get_dict_twitter(account)
        with open('twitter.json', 'w') as json_file:
            json.dump(twitter_dict, json_file, indent=4)

    def json_navigation():
        """
        This function navigates through a json file
        letting the user access the different elements
        of it.
        """
        path = 'twitter.json'
        with open(path, 'r') as file:
            user_data = json.load(file)
        while True:
            if isinstance(user_data, dict):
                print('The keys present\
 in this dictionary are:{}.\
 Choose a key.'.format(list(user_data.keys())))
                chosen_key = input()
                if chosen_key in list(user_data.keys()):
                    user_data = user_data[chosen_key]
                else:
                    print("The key you\
 entered is not present in this dictionary. Try again.")
            elif isinstance(user_data, list):
                print('This list contains {} values.\
 Which one would you like to see?'.format(len(user_data)))
                chosen_index = int(input())
                if chosen_index < len(user_data):
                    user_data = user_data[chosen_index-1]
                else:
                    print('There are only {} elements\
 present in this list'.format(len(user_data)))
            else:
                print(user_data)
                break
    create_json()
    json_navigation()
if __name__ == "__main__":
    main()
