import requests
import hashlib
import os
from datetime import datetime
from random import randint

class MarvelRequest():

    def __init__(self):
        self._PUBLIC_KEY = os.environ['PUBLIC_KEY']
        self._PRIVATE_KEY = os.environ['PRIVATE_KEY']
        self.start_url = 'http://gateway.marvel.com/v1'

    def authorize_request(self):
        """This function returns a dictionary containing authroization
        for the marvel api. It must be incorporated into the parameters of
        the request made to the API."""
        time_stamp = str(datetime.now().microsecond * randint(1, 1000000000))
        byte_stamp = bytes(time_stamp + self._PRIVATE_KEY + self._PUBLIC_KEY, 'utf-8')
        hash_object = hashlib.md5(bytes(byte_stamp))
        _hash = hash_object.hexdigest()
        auth_dict = {'hash': _hash, 'apikey': self._PUBLIC_KEY, 'ts': time_stamp}
        return auth_dict

    def fill_parameters(self, **params):
        return {key: value for key, value in params.items() if value != ''}

    def make_request(self, url, params):
        params.update(self.authorize_rqeuest())
        request = requests.get(url, params=params)
        return request

    def choices_check(self, choices, choice, param_name):
        if choice not in choices:
            print("You may only use " + ' '.join(x for x in choices) + " in " + param_name)
            return True
        return False

    def request_character(self, name='', starts_with='', modified_since='',
                          comics='', series='', events='', stories='',
                          order_by='', limit='', offset=''):
        '''This function will return a request object that will contain
        all the information from a chracter request made to the marvel API.'''

        # Add the start of the API request URL.
        char_url = self.start_url + '/public/characters'

        # The only options using
        order_by_choices = ['', 'name', 'modified', '-name','-modified']

        if self.choices_check(order_by_choices, order_by, 'order_by'):
            return None

        payload = fill_parameters(name = name, starts_with = starts_with,
                  modified_since = modified_since, comics = comics,
                  series = series, events = events, stories = stories,
                  order_by = order_by, limit = limit, offset = offset)

        char_request = make_request(char_url, payload)

        return char_request


    def comic_request(self format='', format_type='', no_variants='',
                      date_descriptor='', date_range='', title=''
                      title_starts_with='', start_year='', issue_number=''
                      diamond_code='', digitalID):

        comic_url = self.start_url + '/public/comics'
