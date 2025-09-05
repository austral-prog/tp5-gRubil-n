import  math

def roots(a, b, c):

    disc = (b**2) - (4*a*c)

    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        return f"({root1}, {root2})"
    elif disc == 0:
        root1 = -b / 2*a
        return f"({root1})"
    else:
        return "( )"


def value_y(a, b, c, x):
    y = (a*(x**2)) + (b*x) + c
    return y


def to_string(a, b, c):

    if a != 0 and b != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a != 0 and b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a == 0 and b != 0:
        return f"f(x) = {b} * X + {c}"
    else:
        return f"f(x) = {c}"

def derivation(a, b, c):

    if a != 0 and b != 0:
        return f"f'(x) = {2*a} * X + {b}"
    elif a != 0 and b == 0:
        return f"f'(x) = {2*a} * X"
    elif a == 0 and b != 0:
        return f"f'(x) = {b}"
    else:
        return f"f'(x) = 0"

#   if b != 0:
#        return f"f'x = {2*a} * X + {b}"
#    else:
#        return f"f'x = {2*a} * X"

print(roots(3,1,0))
print(value_y(1,2,3,4))
print(to_string(2,4,1))
print(derivation(2,5,1))