# Python program for Bisection Method

def bisection(a, b):

    if f(a) * f(b) >= 0:
        print("Wrong assumption: f(a) and f(b) must have opposite signs.")
        return

    tolerance = 1e-6

    while (b - a) >= tolerance:
        # Find middle point
        m = (a + b) / 2

        # Check if middle point is root
        if f(m) == 0.0:
            break

        # Decide the side to repeat the steps
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

    print("\nThe value of root is: %.6f" % m)

    # Example function: f(x) = x^3 - 2x^2 -5


def f(x):
    return x**3 - 2*x**2 - 5


# Example 1: Polynomial function
a = 2
b = 3


print("Function: f(x) = x^3 - 2x^2 -5 \n")
print("f(a): ", f(a))
print("f(b): ", f(b))


bisection(a, b)
