class Polynomial:
    """Polynomials in one variable. Only non-zero terms 
    are stored!!
    """
    def __init__(self, *args):
        """Creates a new polynomial initialized with 
        given terms
        
        Check the Python documentation to understand 
        the '*args' format for a variable number of 
        arguments to a function. If args is empty,then 
        the polynomial is the zero polynomial. 
        Otherwise, args is an even-length tuple 
        consisting of coefficients and associated degrees 
        coming in pairs, e.g. Polynomial(3,2,7,6,-1,0) 
        constructs the polynomial with terms $3x^2$, 
        $7x^6$ and $-1$. Be sure to remove all
        zero-coefficient terms from the polynomial.
        """
        pass
    
    def __str__(self):
        """Printable representation, e.g. 2x^2 - 3x + 5

        Should format the polynomial with terms in
        decreasing order of degree
        """
        return ''
    
    def getCoefficient(self, degree):
        """Returns the coefficient (or 0) for the term. 

        >>> p = Polynomial(2,2,-1,3,5,0)
        >>> p.getCoefficient(3)
        -1
        >>> p.getCoefficient(1)
        0
        """
        return 0
    
    def __call__(self, x):
        """Returns the result of evaluating the polynomial at x

        >>> p = Polynomial(2,2,-1,3,5,0)
        >>> p(-1)
        8
        """
        return 0
        
    def __len__(self):
        """Return the number of terms in the polynomial

        The constant term, even zero, will contribute 1 to the
        length.

        >>> p = Polynomial(2,2,-1,3,5,0)
        >>> len(p)
        3
        >>> p = Polynomial()
        >>> len(p)
        1
        """
        return 0
    
    def __add__(self, other):
        """Returns a new polynomial obtained by adding self 
        with other

        other: Polynomial

        >>> p = Polynomial(2,2,-1,3,5,0)
        >>> q = Polynomial(1,3,-1,2,1,1)
        >>> r = p+q
        >>> r.getCoefficient(3)
        0
        >>> r.getCoefficient(2)
        1
        """
        return Polynomial()

    def __sub__(self, other):
        """Returns a new polynomial obtained by subtracting other 
        from self.
        
        other: Polynomial

        >>> p = Polynomial(2,2,-1,3,5,0)
        >>> q = Polynomial(-1,3,1,2,-1,1)
        >>> r = p-q
        >>> r.getCoefficient(3)
        0
        >>> r.getCoefficient(1)
        1
        """
        return Polynomial()
    
    def __mul__(self, other):
        """Returns a new polynomial obtained by multiplying 
        self with other
        
        other: Polynomial or an integer

        >>> p = Polynomial(2,2,-1,3,5,0)
        >>> q = Polynomial(1,1,1,0)
        >>> r = p*q
        >>> r.getCoefficient(3)
        1
        >>> r.getCoefficient(1)
        5
        >>> s = p*-2
        >>> s.getCoefficient(3)
        2
        """
        return Polynomial()
    
    def derivative(self):
        """Return a new polynomial that is the first derivative.

        >>> p = Polynomial(2,2,-1,3,5,0)
        >>> q = p.derivative()
        >>> q.getCoefficient(2)
        -3
        >>> q.getCoefficient(1)
        4
        """
        return Polynomial()

    ###################################
    ##  Do not modify!!
    ###################################

    def __rmul__(self, other):
        """Returns a new polynomial obtained by right-multiplying 
        self with other.

        other: Polynomial or an integer scalar

        >>> p = Polynomial(2,2,-1,3,5,0)
        >>> s = -2*p
        >>> s.getCoefficient(3)
        2
        """
        return self.__mul__(other)

if __name__=="__main__":
    import doctest
    doctest.testmod()
