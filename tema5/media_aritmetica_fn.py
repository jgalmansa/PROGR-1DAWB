def media_aritmetica(*args):
    '''Realiza la media aritmética de n numeros
    args: (int) numeros a los que se le quiere hacer la media
    return: (int) Media de los valores args'''
    total = 0
    n = len(args)
    #print (num_arg)
    for arg in args:
        total += arg
    if n == 0:
        return None
    return total / n


print(media_aritmetica(1.5,3.7,9.1,16.4,2.7))
print(media_aritmetica())

help (media_aritmetica)