"""Author : Suchita Dmello"""
"""" SSW 567: Homework 1"""

from math import acos, degrees

"""Function to classify the type of triangle"""
def classifyTriangle(a,b,c):
    if(a==b and b==c):
        return "Equilateral triangle"
    elif (a==b or b==c or c==a):
        return "Isosceles triangle"
    else:
        try:
            sides=[a,b,c]
            sides.sort()
            angle = degrees(acos((sides[0]*sides[0] + sides[1]*sides[1] - sides[2]*sides[2])/(2.0 * sides[0] * sides[1])))
        except:
            return "Not a triangle"
        if angle == 90.0:
            return "Right triangle"
        else:
            return "Scalene triangle"

import unittest    
class ClassifyTriangleTest(unittest.TestCase):
    
    def testTriangle(self):
       """ test for equilateral triangle """ 
       self.assertEqual(classifyTriangle(3,3,3),"Equilateral triangle")
       self.assertNotEqual(classifyTriangle(3,7,3),"Equilateral triangle")

       """ test for isosceles triangle """         
       self.assertEqual(classifyTriangle(3,4,3),"Isosceles triangle")
       self.assertEqual(classifyTriangle(3,3,4),"Isosceles triangle")
       self.assertEqual(classifyTriangle(3,4,4),"Isosceles triangle")
       self.assertNotEqual(classifyTriangle(3,3,3),"Isosceles triangle")

       """ test for Right triangle """
       self.assertEqual(classifyTriangle(3,4,5),"Right triangle")
       self.assertEqual(classifyTriangle(3,5,4),"Right triangle")
       self.assertEqual(classifyTriangle(5,3,4),"Right triangle")
       self.assertNotEqual(classifyTriangle(3,3,3),"Right triangle")
       self.assertNotEqual(classifyTriangle(3,3,4),"Right triangle")

       """ test for Scalene triangle """
       self.assertEqual(classifyTriangle(3,4,7),"Scalene triangle")
       self.assertNotEqual(classifyTriangle(3,3,3),"Scalene triangle")
       self.assertNotEqual(classifyTriangle(3,4,3),"Scalene triangle")
       self.assertNotEqual(classifyTriangle(5,3,4),"Scalene triangle")

       """ test for Not a triangle """
       self.assertEqual(classifyTriangle(3,2,6),"Not a triangle")
       self.assertNotEqual(classifyTriangle(3,3,3),"Not a triangle")
       self.assertNotEqual(classifyTriangle(3,2,3),"Not a triangle")
       self.assertNotEqual(classifyTriangle(3,4,5),"Not a triangle")
       self.assertNotEqual(classifyTriangle(3,4,7),"Not a triangle")

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
