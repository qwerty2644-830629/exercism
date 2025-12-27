def value(colors):
    resistor_code = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
                     'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

    return 10 * resistor_code[colors[0]] + resistor_code[colors[1]]