

import unittest
from sorts import selection_sort, insertion_sort, bubble_sort, merge_sort, quick_sort

class SelectionSortTest(unittest.TestCase):
    def test_empty_array(self):
        unsorted = []
        expected = []

        sorted = selection_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = insertion_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = bubble_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = merge_sort(unsorted)
        self.assertEqual(sorted, expected)

    def test_one_element_array(self):
        unsorted = [1]
        expected = [1]

        sorted = selection_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = insertion_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = bubble_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = merge_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = quick_sort(unsorted)
        self.assertEqual(sorted, expected)

    def test_ten_element_array(self):
        unsorted = [5, 4, 3, 2, 1, 6, 7, 8, 9, 0]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        sorted = selection_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = insertion_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = bubble_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = merge_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = quick_sort(unsorted)
        self.assertEqual(sorted, expected)

    def test_duplicate_elements_array(self):
        unsorted = [2, 3, 1, 3]
        expected = [1, 2, 3, 3]

        sorted = selection_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = insertion_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = bubble_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = merge_sort(unsorted)
        self.assertEqual(sorted, expected)

        sorted = quick_sort(unsorted)
        self.assertEqual(sorted, expected)

if __name__ == '__main__':
    unittest.main()
