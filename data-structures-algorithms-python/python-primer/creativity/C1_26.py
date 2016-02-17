def basic_arithmetic(a, b, c):
    '''Write a short program that takes as input three integers,
    a, b, and c, from the console and determines if they can be
    used in a correct arithmetic formula (in the given order),
    like 'a + b = c,' 'a = b − c,' or 'a ∗ b = c.'
    '''

    add = lambda x, y, z: x + y == z
    mul = lambda x, y, z: x * y == z
    sub = lambda x, y, z: y - z == x

    return all([add(a, b, c), mul(a, b, c), sub(a, b, c)])
