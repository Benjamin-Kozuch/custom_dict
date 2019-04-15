import unittest
from custom_dict import Dict


class TestDict(unittest.TestCase):

    def test_create_empty_Dict(self):
        my_dict = Dict()
        self.assertIsInstance(my_dict, Dict)
        self.assertEqual(my_dict._storage_length, my_dict.INITIAL_STORAGE_LENGTH)
        self.assertEqual(my_dict.items(), [])
        with self.assertRaises(KeyError):
            my_dict["x"]

    def test_initialize_Dict_with_element(self):
        my_dict = Dict(("x", 1))
        self.assertEqual(my_dict.items(), [("x", 1)])
        self.assertEqual(my_dict["x"], 1)

    def test_initialize_Dict_with_multiple_elements(self):
        my_dict = Dict(("x", 1), ("y", 2))
        self.assertIn(("x", 1), my_dict.items())
        self.assertIn(("y", 2), my_dict.items())

    def test_setting_Dict_value(self):
        my_dict = Dict()
        my_dict['y'] = 2
        self.assertIn(("y", 2), my_dict.items())
        self.assertEqual(my_dict["y"], 2)

    def test_overwrite_value(self):
        my_dict = Dict()
        my_dict['x'] = 1
        self.assertIn(("x", 1), my_dict.items())
        my_dict['x'] = 2
        self.assertIn(("x", 2), my_dict.items())
        self.assertNotIn(("x", 1), my_dict.items())

    def test_fill_up_storage(self):
        my_dict = Dict()
        for i in range(my_dict.INITIAL_STORAGE_LENGTH):
            my_dict[i] = i
        self.assertEqual(my_dict._storage_length, my_dict.INITIAL_STORAGE_LENGTH)
        my_dict['a'] = 1
        self.assertEqual(my_dict._storage_length, my_dict.INITIAL_STORAGE_LENGTH * 2)

    def test_fill_up_storage_multiple_times(self):
        my_dict = Dict()
        for i in range(my_dict.INITIAL_STORAGE_LENGTH):
            my_dict[i] = i
        self.assertEqual(my_dict._storage_length, my_dict.INITIAL_STORAGE_LENGTH)
        
        for i in range(
            my_dict.INITIAL_STORAGE_LENGTH, 
            my_dict.INITIAL_STORAGE_LENGTH * 2
        ):
            my_dict[i] = i
        self.assertEqual(my_dict._storage_length, my_dict.INITIAL_STORAGE_LENGTH * 2)

        for i in range(
            my_dict.INITIAL_STORAGE_LENGTH * 2, 
            my_dict.INITIAL_STORAGE_LENGTH * 4
        ):
            my_dict[i] = i
        self.assertEqual(my_dict._storage_length, my_dict.INITIAL_STORAGE_LENGTH * 4)

        for i in range(
            my_dict.INITIAL_STORAGE_LENGTH * 4, 
            my_dict.INITIAL_STORAGE_LENGTH * 8
        ):
            my_dict[i] = i
        self.assertEqual(my_dict._storage_length, my_dict.INITIAL_STORAGE_LENGTH * 8)
        
        my_dict['a'] = 1
        self.assertEqual(my_dict._storage_length, my_dict.INITIAL_STORAGE_LENGTH * 16)


            



if __name__ == '__main__':
    unittest.main()

