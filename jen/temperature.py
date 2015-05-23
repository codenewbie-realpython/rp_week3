#week three assignment 2 - jen b
from __future__ import division

def conv_celcius(cel_number):
    convert_cel = cel_number * 9/5 + 32
    return convert_cel


def conv_faren(far_number):
    convert_far= (far_number -32) * 5/9
    return convert_far


temp_1 = 80
print "{} degrees F = {} degrees C".format(temp_1, conv_celcius(temp_1))

temp_2 = 30
print "{} degrees C = {} degrees F".format(temp_2, conv_faren(temp_2))


'''note : i need to get better at naming! too confusing'''
