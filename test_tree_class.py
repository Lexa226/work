import unittest
from pandas import DataFrame
from tree_class import Tree


class TestTreeMethods(unittest.TestCase):
    def setUp(self):
        data = {
            'объект': ['имя1', 'имя2', 'имя3', 'имя4', 'имя5'],
            'классификатор1': ['класс11', 'класс12', 'класс11', 'класс11', 'класс12'],
            'классификатор2': ['класс21', 'класс21', 'класс22', 'класс21', 'класс22']
        }
        self.test_data = DataFrame(data)
        self.tree = Tree('классификатор1', 'классификатор2')
        self.tree.data = self.test_data

    def test_get_children_without_filters(self):
        result = self.tree.get_children()
        expected = ['имя1', 'имя2', 'имя3', 'имя4', 'имя5']
        self.assertEqual(result, expected)

    def test_get_children_with_single_filter(self):
        result = self.tree.get_children(('классификатор1', 'класс11'))
        expected = ['имя1', 'имя3', 'имя4']
        self.assertEqual(result, expected)

    def test_get_children_with_multiple_filters(self):
        result = self.tree.get_children(('классификатор1', 'класс12'), ('классификатор2', 'класс22'))
        expected = ['имя5']
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
    