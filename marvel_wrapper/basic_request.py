import requests
import hashlib
import os
import inspect
from datetime import datetime
from random import randint

class MarvelRequest():

    def __init__(self):
        self._PUBLIC_KEY = os.environ['PUBLIC_KEY']
        self._PRIVATE_KEY = os.environ['PRIVATE_KEY']
        self.start_url = 'http://gateway.marvel.com/v1'

    def authorize_request(self):
        """Returns a dictionary containing authroization
        for the marvel api. It must be incorporated into the parameters of
        the request made to the API."""
        time_stamp = str(datetime.now().microsecond * randint(1, 1000000000))
        byte_stamp = bytes(time_stamp + self._PRIVATE_KEY + self._PUBLIC_KEY, 'utf-8')
        hash_object = hashlib.md5(bytes(byte_stamp))
        _hash = hash_object.hexdigest()
        auth_dict = {'hash': _hash, 'apikey': self._PUBLIC_KEY, 'ts': time_stamp}
        return auth_dict

    def fill_parameters(self, **params):
        '''Returns a dictionary of all the keyword arguments of a function.'''
        return {key: value for key, value in params.items() if value != ''}

    def make_request(self, url, params):
        '''Returns an authorized request object made with the parameters given.'''
        params.update(self.authorize_rqeuest())
        request = requests.get(url, params=params)
        return request

    def choices_check(self, choices, choice, param_name):
        '''Returns True if a choice in not in the possible options.
        Returns False if the choice is in the possible options.'''
        if choice not in choices:
            print("You may only use " + ' '.join(x for x in choices) + " in " + param_name)
            return True
        return False

    def request_character(self, name='', starts_with='', modified_since='',
                          comics='', series='', events='', stories='',
                          order_by='', limit='', offset=''):
        '''This function will return a request object that will contain
        all the information from a chracter request made to the marvel API.'''

        # Add the start of the API request URL
        char_url = self.start_url + '/public/characters'

        # The only options for order_by are these, I must check for them
        order_by_choices = ['', 'name', 'modified', '-name','-modified']

        # If choices_check returns True then the order_by given is a bad choice
        if self.choices_check(order_by_choices, order_by, 'order_by'):
            return None

        # Get the dictionary of parameters given in this function
        payload = self.fill_parameters(name = name, starts_with = starts_with,
                  modified_since = modified_since, comics = comics,
                  series = series, events = events, stories = stories,
                  order_by = order_by, limit = limit, offset = offset)

        char_request = self.make_request(char_url, payload)

        return char_request

    # def comic_request(self format='', format_type='', no_variants='',
    #                   date_descriptor='', date_range='', title=''
    #                   title_starts_with='', start_year='', issue_number=''
    #                   diamond_code='', digitalID):
    #
    #     comic_url = self.start_url + '/public/comics'
