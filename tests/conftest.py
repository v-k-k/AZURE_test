from pytest import fixture
from enum import Enum
from pathlib import Path
from collections import namedtuple
import configparser
import json
import sys
import os


config = configparser.ConfigParser()
config.read('data.ini')

myself = Path(__file__).resolve()
sys.path.append(str(myself.parents[1]))
TestData = namedtuple('TestData', ('positive', 'negative', 'exception'))

BASE_URL = config['URL']['BASE_URL']

ENDPOINT_1 = config['ENDPOINTS']['ENDPOINT_1']
ENDPOINT_2 = config['ENDPOINTS']['ENDPOINT_2']

LATITUDE = config['COORDINATES']['lat']
LONGITUDE = config['COORDINATES']['lon']

test_data = TestData(f'tests{os.sep}positive_test_data.json', f'tests{os.sep}negative_test_data.json',
                     f'tests{os.sep}exception_test_data.json')


class HTTPs(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'

    def __str__(self):
        return str(self._value_)


def load_test_data(path):    
    with open(path) as data_file:
        return json.load(data_file)


@fixture(scope='class', params=load_test_data(test_data.positive))
def get_positive_data(request):
    data = request.param
    return data


@fixture(scope='class', params=load_test_data(test_data.negative))
def get_negative_data(request):
    data = request.param
    return data
    

@fixture(scope='class', params=load_test_data(test_data.exception))
def get_exception_data(request):
    data = request.param
    return data


@fixture(scope='class')
def get_positive_api_data_1(request):
    return BASE_URL, ENDPOINT_1, HTTPs.GET


@fixture(scope='class')
def get_negative_api_data_1(request):
    return BASE_URL, ENDPOINT_1, HTTPs.POST


@fixture(scope='class')
def get_positive_api_data_2(request):
    return BASE_URL, ENDPOINT_2, HTTPs.GET, LATITUDE, LONGITUDE


@fixture(scope='class')
def get_negative_api_data_2(request):
    return BASE_URL, ENDPOINT_2, HTTPs.GET, '100'+LATITUDE, LONGITUDE

