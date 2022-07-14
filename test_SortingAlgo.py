from MergeAlgo.Sorting_Algo import Algo


def test_empty_list():
    empty = Algo.merge1([])
    assert empty, "this is a failed test"
