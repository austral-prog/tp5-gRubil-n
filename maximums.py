# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y


def max_of_three(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z

