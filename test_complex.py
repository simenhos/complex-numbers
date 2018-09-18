from complex import Complex

"""
Most test are pretty straight forward, the method name describes what is being tested.
assert (TEST == EXPECTED RESTULT) == True, for the most part atleast.
"""
class Test_complex:
    def test_complex_eq():
        assert (Complex(1, 2) == Complex(1, 2)) == True

    def test_complex_add():
        assert (Complex(1, 2) + Complex(2, 2) == Complex(3, 4)) == True

    def test_complex_sub():
        assert (Complex(1, 2) - Complex(2, 3) == Complex(-1, -1)) == True

    def test_complex_mul():
        assert (Complex(1, 2) * Complex(2, 3) == Complex(-4, 7)) == True

    def test_complex_conjugate():
        a1 = Complex(1, 2)
        assert (a1.conjugate() == Complex(1, -2)) == True

    def test_complex_mudulus():
        a1 = Complex(4, 3)
        assert (a1.modulus() == 5) == True

    def test_complex_radd():
        assert ((1+2j) + Complex(2, 2) == Complex(3, 4)) == True

    def test_complex_rsub():
        assert ((2+3j) - Complex(1, 2) == Complex(-1, -1)) == True

    def test_complex_rmul():
        assert ((4 * Complex(3, 4)) - 2 == Complex(10, 16)) == True

    #These three test are made to use a multiple of methods at the same time.
    def test_all():
        assert(Complex(1, 1) * 2 - (Complex(3, 4) * 4) + (2+2j) == Complex(-8, -12)) == True

    def test_all2():
        assert(((1+2j) * Complex(2, 2)) * 2 == Complex(-4, 12)) == True

    def test_all3():
        assert(2 - (((1+2j) * Complex(2, 2)) * 2) == Complex(6, -12)) == True




    test_complex_eq()
    test_complex_add()
    test_complex_sub()
    test_complex_mul()
    test_complex_conjugate()
    test_complex_mudulus()
    test_complex_radd()
    test_complex_rsub()
    test_complex_rmul()
    test_all()
    test_all2()
    test_all3()
    print("All tests done. No errors! Hurrah!")
