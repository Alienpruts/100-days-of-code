from unittest import TestCase
from unittest.mock import patch, call
from nose.tools import assert_equal, assert_list_equal
from work.testing.filter_funcs import filter_ints


class FilterIntstestCase(TestCase):

    def test_filter_ints_return_value(self):
        v = [3, -4, 0, -2, 5, 0, 8, -1]

        result = filter_ints(v)

        assert_list_equal([3, 5, 8], result)
