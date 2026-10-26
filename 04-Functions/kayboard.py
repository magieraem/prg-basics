###
# Functions to read any data type from the keyboard
#
def input_string(message):
    a = str(input(message))
    return a

def input_integer(message):
    b = int(input(message))
    return b

def input_real(message):
    c = float(input(message))
    return c

def input_boolean(message):
    d = input(message)
    if d == 'y':
        return bool(True)
    else:
        return bool(False)
