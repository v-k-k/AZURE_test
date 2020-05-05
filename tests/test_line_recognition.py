from pytest import mark
from game import find_line
from point import Point


@mark.smoke
class BaseTests:

    @mark.positive
    def test_positive_data(self, get_positive_data):
        assert find_line([Point(int(pt[0]), int(pt[1])) for pt in get_positive_data])

    @mark.negative
    def test_negative_data(self, get_negative_data):
        assert not find_line([Point(int(pt[0]), int(pt[1])) for pt in get_negative_data])

    @mark.xfail
    def test_exception_data(self, get_exception_data):
        assert not find_line([Point(int(pt[0]), int(pt[1])) for pt in get_exception_data])
