"""Module contenant les fonctions de calcul"""


def addition(a, b):
    result = a + b
    return result



def substraction(a, b):
    result = a - b
    return result




def division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    result = a / b
    return result