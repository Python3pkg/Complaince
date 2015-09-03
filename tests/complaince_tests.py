import unittest
from complaince.complaince import param_check

class Vector(object):
    '''A vector class this can be an example of adapter pattern'''
    def __init__(self, dimensions):
        '''Create a vector using python list as underlying implementation'''
        self._coords =  [0 for d in range(dimensions)]

    def __len__(self):
        '''Len of vector is the len of the underlying list'''
        return len(self._coords)

    def __getitem__(self, n):
        '''get the nth coordinate of vector'''
        return self._coords[n]
    def __setitem__(self, n, val):
        '''set the nth dimension value'''
        self._coords[n] = val

    def __add__(self, additive):
        '''Find sub of two vectors'''
        if len(self) != len(additive):
            raise ValueError("The vectors should be of same length")
        result = Vector(len(self))
        for i in range(len(additive)):
            result[i] = self[i] + additive[i]
        return result

    def __eq__(self, comparitive):
        return self._equality(comparitive)
    def __ne__(self, comparitive):
        return not self._equality(comparitive)

    def _equality(self, comparitive):
        '''Equality checker'''
        if(len(self) != len(comparitive)):
            return False
        for i in range(len(self)):
            if(self[i] != comparitive[i]):
                return False
        return True


class ComplainceTests(unittest.TestCase):
    '''A Test Plan'''
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

    def test_class_based_level_one(self):
        '''Test case for a user defined Class type
           Using class vector defined above
        '''
        @param_check((Vector,), (Vector,), level = 1, ret=(Vector,))
        def vector_add(a, b):
            return a + b
        v1 = Vector(2)
        v1[0] = 1
        v1[1] = 2
        v2 = Vector(2)
        v2[0] = 3
        v2[1] = 5
        expected_result = Vector(2)
        expected_result[0] = 4
        expected_result[1] = 7
        self.assertEqual(vector_add(v1, v2), expected_result)

        with self.assertRaises(TypeError):
            vector_add(v1,2)



if __name__ == '__main__':
    unittest.main()
