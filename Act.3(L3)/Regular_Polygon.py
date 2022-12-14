# name: Villas, Justin Lawrence DL.
#lab: 3.1
#cource: cmpe30053
# -------------------------------------------------------------------------

import math
PI = math.pi


class RegularPolygon():
    __n = 3
    __s = 1
    __x = 0.0
    __y = 0.0

    # ------------------------------------------------------------------
    # purpose: initilize the variables that will be used
    # parameter: number of lines, sides and x and y
    # return:    none
    def __init__(self, n=3, sides=1, x=.0, y=.0):
        self.__n = n
        self.__sides = sides
        self.__x = x
        self.__y = y

    # ------------------------------------------------------------------
    # purpose: to display the area and perimeter
    # parameter: none
    # return:    none
    def __showAreaPerimeter(self):
        print("======================")
        print(f"Perimeter of the Polygon:{self.get_Perimeter()}")
        print(f"Area of the Polygon:{self.get_Area()}")
        print("=======================\n")

    # ------------------------------------------------------------------
    # purpose: for solving the perimeter
    # parameter: none
    # return:    return the solveperimeter
    def get_Perimeter(self):
        solvePerimeter = self.__n * self.__s
        return solvePerimeter

    # ------------------------------------------------------------------
    # purpose: for solving the area
    # parameter: none
    # return:    return the area
    def get_Area(self):
        newmerator = self.__n * (self.__sides**2)
        tan = math.tan(PI/self.__n)
        denominator = 4 * tan
        area = newmerator/denominator
        floatformat = "{:.2f}".format(area)
        solveArea = floatformat
        return solveArea

    # ------------------------------------------------------------------
    # purpose: when called it will call the _showAreaPerimeter.
    # parameter: none
    # return:    none
    def get_answers(self):
        self.__showAreaPerimeter()
