from marvel_wrapper.basic_request import MarvelRequest
import os

basic_request = MarvelRequest()

def test_marvel_request():
    assert basic_request._PUBLIC_KEY == os.environ['PUBLIC_KEY']
    assert basic_request._PRIVATE_KEY == os.environ['PRIVATE_KEY']

def test_character_request():
    hulk_request = basic_request.request_character(name='Hulk')
    assert hulk_request.status_code == 200
    hulk_json = hulk_request.json()
    assert hulk_json['status'] == 'Ok'
    bad_request = basic_request.request_character(order_by='not a parameter')
