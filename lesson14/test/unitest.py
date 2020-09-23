import unittest


def sum(array: list):
    # assert type(array) is list, "type not "list""
    assert isinstance(array, tuple) or isinstance(array, list)
    total = 0
    for val in array:
        total += val
    return total


# if __name__ == "__main__":
#     sum(3)
#     sum([3, 3])
#     sum("3333")
#     sum(["3", "3"])


class TestSum(unittest.TestCase):
    def test_list_int(self):
        lst = 3
        self.assertTrue(isinstance(lst, list) or isinstance(lst, tuple), "Тест на список/кортеж")
        for val in lst:
            self.assertTrue(isinstance(val, int))


if __name__ == "__main__":
    unittest.main()