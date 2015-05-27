import requests
import hashlib
import os
from datetime import datetime
from random import randint
from collections import OrderedDict


class MarvelRequest():

    def __init__(self):
        self._PUBLIC_KEY = os.environ['PUBLIC_KEY']
        self._PRIVATE_KEY = os.environ['PRIVATE_KEY']
        self.start_url = 'http://gateway.marvel.com/v1'

    def authorize_request(self):
        time_stamp = str(datetime.now().microsecond * randint(1, 1000000000))
        hash_object = hashlib.md5(bytes(time_stamp+self._PRIVATE_KEY+self._PUBLIC_KEY, 'utf-8'))
        _hash = hash_object.hexdigest()
        auth_dict = {'hash': _hash, 'apikey': self._PUBLIC_KEY, 'ts': time_stamp}
        return auth_dict

    def request_character(self, name='', starts_with='', modified_since='',
                          comics='', series='', events='', stories='',
                          order_by='', limit='', offset=''):

        char_url = self.start_url + '/public/characters'

        order_by_choices = ['', 'name', 'modified', '-name','-modified']

        if order_by not in order_by_choices:
            return('You can only order by name, modified, -name, and \
            -modified.\n')

        payload = {'name': name, 'starts_with': starts_with,
                  'modified_since': modified_since, 'comics': comics,
                  'series': series, 'events': events, 'stories': stories,
                  'order_by': order_by, 'limit': limit, 'offset': offset}

        payload = {key: value for key, value in payload.items() if value != ''}

        payload.update(self.authorize_request())

        char_request = requests.get(char_url, params=payload)

        return char_request


    # def comic_request(self):
