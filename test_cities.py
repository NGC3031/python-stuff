''' Sample unit testing - use with city_functions.py'''

import unittest
from city_functions import city_function


class NamesTestCase(unittest.TestCase):
    '''Tests for 'name_function.py'.'''

    def test_country_city(self):
        ''' Test Sydney Australia '''
        formatted_name = city_function('Sydney', 'Australia')
        print('----'+formatted_name+'----')
        self.assertEqual(formatted_name, 'Sydney, Australia')


if __name__ == '__main__':
    unittest.main()
