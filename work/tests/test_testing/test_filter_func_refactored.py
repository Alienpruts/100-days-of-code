from unittest import TestCase
from unittest.mock import patch, call
from nose.tools import assert_equal, assert_list_equal
from work.testing.filter_funcs_refactored import filter_ints


class FilterIntstestCase(TestCase):

    @patch('work.testing.filter_funcs_refactored.is_positive')
    def test_filter_ints(self, is_positive_mock):
        # Setup
        v = [3, -4, 0, 5, 8]

        # Execution
        filter_ints(v)

        # Verification
        assert_equal(
            [call(3), call(-4), call(0), call(5), call(8)], # We call the mock is_positive
            is_positive_mock.call_args_list
        )

    def test_filter_ints_return_value(self):
        v = [3, -4, 0, -2, 5, 0, 8, -1]

        result = filter_ints(v)

        assert_list_equal([3, 5, 8], result)
