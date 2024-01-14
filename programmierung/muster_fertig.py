def dreieck_muster():
    for i in range(1, 7):
        print('x' * i + ' ' * (26 - 2*i) + 'o' * i)

    for i in range(5, 0, -1):
        print('x' * i + ' ' * (26 - 2*i) + 'o' * i)

dreieck_muster()
