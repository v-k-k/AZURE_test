from pytest import fixture
from pathlib import Path
from collections import namedtuple
import json
import sys
import os


myself = Path(__file__).resolve()
sys.path.append(str(myself.parents[1]))
TestData = namedtuple('TestData', ('positive', 'negative', 'exception'))

test_data = TestData(f'tests{os.sep}positive_test_data.json', f'tests{os.sep}negative_test_data.json', f'tests{os.sep}exception_test_data.json')


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
