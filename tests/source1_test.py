"""
Test for source.source1
"""
from source.source1 import get_triangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')
        
    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(2, 2, 3)
        self.assertEqual(result, 'isosceles')
        
    def test_get_triangle_invalid_some_letter(self):
        result = get_triangle_type(1, 2, '3')
        self.assertEqual(result, 'invalid')
        
    def test_get_triangle_invalid_some_negative(self):
        result = get_triangle_type(1, 2, -3)
        self.assertEqual(result, 'invalid')   
        
    def test_get_triangle_scalene_list(self):
        result = get_triangle_type([1,2,3])
        self.assertEqual(result, 'scalene') 
        
    def test_get_triangle_equilateral_dict(self):
        result = get_triangle_type({'a':3,'b':3,'c':3})
        self.assertEqual(result, 'equilateral') 
        
 