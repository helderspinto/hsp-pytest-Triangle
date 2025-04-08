class Triangle:
    """
    Represents a triangle with properties for its base, right side, left side, and height.
    Provides functionality to calculate the perimeter and area of the triangle.

    :ivar _base: The base of the triangle. Default value is 1.
    :ivar _right_side: The right side of the triangle. Default value is 1.
    :ivar _left_side: The left side of the triangle. Default value is 1.
    :ivar _height: The height of the triangle. Default value is 1.
    :ivar was_defaulted: True when the input values for a constructor are incorrect. Default is False.
    """

    def __init__(self, *args):
        """
        Initializes a new instance of the Triangle class with specified values for base, right side, left side, and height.
        Allows for multiple constructor patterns by using default arguments and conditional logic.

        :param b: The value of the triangle's base. It must be a positive value greater than zero.
        :param rs: The value of the triangle's right side. It must be a positive value greater than zero.
        :param ls: The value of the triangle's left side. It must be a positive value greater than zero.
        :param h: The height of the triangle. It must be a positive value greater than zero. If not provided, defaults to 1.
        :param t: Another instance of Triangle from which to copy properties. If provided, other parameters are ignored.
        """
        self.was_defaulted = False
        self._base = 1
        self._right_side = 1
        self._left_side = 1
        self._height = 1

        if len(args) ==1 and args[0] is not None and isinstance(args[0], Triangle):
            self._base = args[0]._base
            self._right_side = args[0]._right_side
            self._left_side = args[0]._left_side
            self._height = args[0]._height
        elif len(args) == 2:
            self.base = args[0]
            self.height = args[1]
        elif len(args) == 3:
            self.base = args[0]
            self.right_side = args[1]
            self.left_side = args[2]

            if not self._is_valid_triangle(self.base, self.right_side, self.left_side):
                self.was_defaulted = True
        elif len(args) ==4:
            self.base = args[0]
            self.right_side = args[1]
            self.left_side = args[2]
            self.height = args[3]

            if not self._is_valid_triangle(self.base, self.right_side, self.left_side):
                self.was_defaulted = True

    @property
    def base(self):
        """The base of the triangle. Must be a positive number greater than zero."""
        return self._base

    @base.setter
    def base(self, value):
        if value > 0:
            self._base = value

    @property
    def right_side(self):
        """The right side of the triangle. Must be a positive number greater than zero."""
        return self._right_side

    @right_side.setter
    def right_side(self, value):
        if value > 0:
            self._right_side = value

    @property
    def left_side(self):
        """The left side of the triangle. Must be a positive number greater than zero."""
        return self._left_side

    @left_side.setter
    def left_side(self, value):
        if value > 0:
            self._left_side = value

    @property
    def height(self):
        """The height of the triangle. Must be a positive number greater than zero."""
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value

    def perimeter(self):
        """
        Calculates and returns the perimeter of the triangle.

        :return: The sum of all sides of the triangle.
        """
        return self._right_side + self._base + self._left_side

    def area(self):
        """
        Calculates and returns the area of the triangle.

        :return: The area of the triangle calculated using the base and height.
        """
        return self._base * (self._height / 2)

    def get_triangle_type(self):
        """
        Determines the type of the triangle based on its sides.

        :return: A string indicating whether the triangle is Equilateral, Isosceles, or Scalene.
        """
        if self._right_side == self._base == self._left_side:
            return "Equilateral"
        elif self._right_side == self._base or self._right_side == self._left_side or self._base == self._left_side:
            return "Isosceles"
        else:
            return "Scalene"

    def __str__(self):
        """
        Provides a string representation of the Triangle object, including its base, sides, and height.

        :return: A string detailing the dimensions of the triangle.
        """
        return f"Triangle:\n\tbase: {self._base:.2f}" \
               f"\n\tright side: {self._right_side:.2f}" \
               f"\n\tleft side: {self._left_side:.2f}" \
               f"\n\theight: {self._height:.2f}"

    def _is_valid_triangle(self, a, b, c):
        """
        Determines if the given side lengths can form a valid triangle.

        :param a: Length of side a.
        :param b: Length of side b.
        :param c: Length of side c.
        :return: True if the side lengths can form a triangle, False otherwise.
        """
        return a + b > c and a + c > b and b + c > a