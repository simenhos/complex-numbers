import math

class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Assignment 3.3

    """
    Changes the sign of the imaginary part of the complex number
    """
    def conjugate(self):
        return Complex(self.real, - self.imag)

    """
    Returns the square root of the numbers^2
    """
    def modulus(self):
        return math.sqrt(self.real**2 + self.imag**2)

    """
    If the number is an int, we jsut add the int to the real number
    else, we are adding the 1st numbers real to 2nd numbers real
    and 1st numbers imaginary to the 2nd numbers imaginary
    """
    def __add__(self, other):
        if(isinstance(other, int)):
            return Complex(self.real + other, self.imag)
        else:
            return Complex(self.real + other.real, self.imag + other.imag)

    """
    Same as add, just subtracting instead
    """
    def __sub__(self, other):
        if(isinstance(other, int)):
            return Complex(self.real - other, self.imag)
        else:
            return Complex(self.real - other.real, self.imag - other.imag)

    """
    Mostly same as add, except multiplying with both real and imaginary
    When multiplying complex numbers the formula (a+bi)(c+di) = (a*c−b*d) + (a*d+b*c) is used
    """
    def __mul__(self, other):
        if(isinstance(other, int)):
            return Complex(self.real * other, self.imag * other)
        else:
            return Complex(self.real * other.real - self.imag * other.imag,
         self.imag * other.real + self.real * other.imag)

    """
    Returns true if all the attributes of self equals to those of others
    """
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    """
    Formating the string depending on the value of the different attributes
    This way im not showing the real value if it's zero, but I have chosen to
    show the imaginary value even if its 0. This formating also handles + and -
    signs in such a way it wont show double.
    """
    def __str__(self):
        if(self.imag >= 0 and self.real != 0):
            return '({:.0f}+{:.0f}i)'.format(self.real, self.imag)
        elif(self.imag >= 0 and self.real == 0):
            return '({:.0f}i)'.format(self.imag)
        elif(self.imag < 0 and self.real != 0):
            return '({:.0f}{:.0f}i)'.format(self.real, self.imag)
        else:
            return '({:.0f}i)'.format(self.imag)

    # Assignment 3.4
    """
    Since the order of addition doesn't matter, we simply use add method
    """
    def __radd__(self, other):
        return self.__add__(other)

    """
    Order of subtraction does however matter, so if the second number is a int we
    change the sign by using the __neg__ method and adds the number after to the real value.
    If the second number is a complex number, we send it to the sub method
    """
    def __rsub__(self, other):
        if(isinstance(other, int)):
            return Complex(self.__neg__().real + other, self.__neg__().imag)
        else:
            return self.__sub__(other)

    """
    Since the order of multiplication doesn't matter, we use the mul method
    """
    def __rmul__(self, other):
        return self.__mul__(other)


    # Optional, possibly useful methods

    # Returns the numbers with - instead of +
    def __neg__(self):
        return Complex(-self.real, -self.imag)
