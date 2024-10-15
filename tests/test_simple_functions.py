import pytest,numpy

from simple_functions import my_sum, factorial, sin


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected
        
    @pytest.mark.parametrize('number, expected', [
        (5, numpy.sin(5)),
        (3, numpy.sin(3)),
        (1, numpy.sin(1))
    ])
    def test_sin(self, number, expected):
        '''Test our factorial function'''
        answer = sin(number)
        assert np.isclose(answer, expected, atol=1e-10)
