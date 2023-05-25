#simple program to compute cuberoot of any float number

def cube_root(f):
    if type(f) == float:
        cr = f ** (1/3)
        print ("The cube root is: ", cr)
        return cr
    else:
        print('{} value is not a float'.format(f))
        return None
