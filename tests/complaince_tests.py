import unittest
from complaince.complaince import param_check

class ComplainceTests(unittest.TestCase):

    def test_no_return_default_level(self):
        '''Test case where we do not check return types and level
           is warning i.e default 0
        '''
        @param_check((int, float), (int,float))
        def add(a, b):
            return a + b
        #check case where it goes through perfectly
        self.assertEqual(add(1,2), 3)

        #Check case where warning message is printed i.e returns a value expected
        self.assertEqual(add('b','a'),'ba')

    def test_no_return_level_one(self):
        '''Test Case where we do not check return types and level
           is 1 i.e we throw exception
        '''

        @param_check((int, float),(int, float), level = 1)
        def add(a , b):
            return a + b
        #check case where it goes through perfectly
        self.assertEqual(add(2,5), 7)

        #check case where exception is thrown
        with self.assertRaises(TypeError):
            add('b','a')

    def test_return_val_default_level(self):
        '''Test case where we check the return value type and level
           is default 0
        '''
        @param_check((int, float),(int, float), ret=(int, float))
        def add(a, b):
            return a + b

        #check two cases in case of correct values
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(1.1,3),4.1)
        self.assertEqual(add(23.46,32.69),56.15)

        #check cases where wrong value is returned , but still goes through due to warning

        self.assertEqual(add(1,True),2)
        self.assertEqual(add(True,1.6), 2.6)

    def test_return_val_level_one(self):
        '''Test Case where we check return types and level
           is 1 i.e we throw exception
        '''

        @param_check((int, float),(int, float), level = 1, ret=(int,float))
        def add(a , b):
            return a + b
        #check case where it goes through perfectly
        self.assertEqual(add(2,5.2), 7.2)
        self.assertEqual(add(1.1,7.5), 8.6)
        @param_check((int, float),(int, float), level = 1, ret=(int,float))
        def wrong_add(a, b):
            return 'x'
        #check case where exception is thrown
        with self.assertRaises(TypeError):
            wrong_add(2,1)
        with self.assertRaises(TypeError):
            wrong_add(1,2.2)


if __name__ == '__main__':
    unittest.main()
