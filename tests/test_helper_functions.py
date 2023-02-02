import sys
sys.path.append('../')

from src.helper_functions import add, multiply


def test_add_two_positive_numbers_produce_positive_number():
    # given
    i, j = 1, 2
    # when
    res = add(i, j)
    # then
    assert res == 3


def test_add_two_negative__():
    # given
    i, j = -5, -2
    # when
    res = add(i, j)
    # then
    assert res == -7


def test_add_positive_and_zero__():
    pass


if __name__ == '__main__':
    test_add_two_positive_numbers_produce_positive_number()
    test_add_two_negative__()
    test_add_positive_and_zero__()
    print("All tests passed")