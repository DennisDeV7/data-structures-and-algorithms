import pytest
from code_challenges.insertion_sort import insertion_sort


# @pytest.mark.skip("TODO")
def test_insertion_sort():
    test_list = [8, 4, 23, 42, 16, 15]
    insertion_sort(test_list)
    expected = [4, 8, 15, 16, 23, 42]
    assert test_list == expected

# @pytest.mark.skip("TODO")
def test_insertion_sort_reverse():
    test_list = [20, 18, 12, 8, 5, -2]
    insertion_sort(test_list)
    expected = [-2, 5, 8, 12, 18, 20]
    assert test_list == expected

# @pytest.mark.skip("TODO")
def test_insertion_sort_few_uniques():
    test_list = [5, 12, 7, 5, 5, 7]
    insertion_sort(test_list)
    expected = [5, 5, 5, 7, 7, 12]
    assert test_list == expected

# @pytest.mark.skip("TODO")
def test_insertion_sort_nearly_sorted():
    test_list = [2, 3, 5, 7, 13, 11]
    insertion_sort(test_list)
    expected = [2, 3, 5, 7, 11, 13]
    assert test_list == expected
