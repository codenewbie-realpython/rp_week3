def c_to_f(temp_c):
    new_temp_f = (temp_c * 9.0 / 5) + 32
    return "{} degrees C = {} degrees F".format(temp_c, new_temp_f)


def f_to_c(temp_f):
    new_temp_c = (temp_f - 32) * 5 / 9.0
    return "{} degrees F = {} degrees C".format(temp_f, new_temp_c)

print c_to_f(37)
print f_to_c(98.6)