import  math

def roots(a, b, c):

    disc = (b**2) - (4*a*c)

    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        return root1, root2
    elif disc == 0:
        root1 = -b / 2*a
        return f"({root1})"
    else:
        return "( )"


def value_y(a, b, c, x):
    y = (a*(x**2)) + (b*x) + c
    return y


def to_string(a, b, c):
    return f"{a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):
    if b != 0:
        return f"f'x = {2*a} * X + {b}"
    else:
        return f"f'x = {2*a} * X"
