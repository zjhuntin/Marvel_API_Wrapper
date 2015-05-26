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
        hash_object = hashlib.md5(bytes(ts+self._PRIVATE_KEY+self._PUBLIC_KEY, 'utf-8'))
        _hash = hash_object.hexdigest()
        payload = {'hash': _hash, 'apikey': public_key, 'ts': ts}
        auth_params = 'ts={ts}&apikey={apikey}&hash={hash}'.format(**payload)
        return auth_params

    def request_character(self, name='', starts_with='', modified_since='',
                          comics='', series='', events='', stories='',
                          order_by='', limit='', offset=''):

        char_params = '/public/characters?'

        order_by_choices = ['name', 'modified', '-name','-modified']

        params = [('name', name), ('starts_with', starts_with),
                  ('modified_since' modified_since), ('comics', comics),
                  ('series', series), ('events', events), ('stories', stories),
                  ('order_by', order_by), ('limit', limit), ('offset', offset)]

        params = OrderedDict(params)

        char_params = []
        for key in parameters.keys():
            if parameters[key] != '':
                if key == 'order_by':
                    if parameters[key] not in order_by_choices:
                        return('You can only order by name, modified, -name,\
                                and -modified.\n')
                if len(char_params) == 0:
                    char_params += key
                else:
                    char_params += '&' + key

        full_url = self.start_url + char_params + authorize_request()

        char_request = requests.get(full_url)


    def comic_request(self):
