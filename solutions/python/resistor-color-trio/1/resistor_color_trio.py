def label(colors):
    resistor_code = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
                     'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    ohm_value = (resistor_code[colors[0]]*10 + resistor_code[colors[1]]) * 10 ** resistor_code[colors[2]]
    metric = ' ohms'
    if ohm_value >= 10 ** 9:
        ohm_value /= 10 ** 9
        metric = ' gigaohms'
    elif ohm_value >= 10 ** 6:
        ohm_value /= 10 ** 6
        metric = ' megaohms'
    elif ohm_value >= 10 ** 3:
        ohm_value /= 10 ** 3
        metric = ' kiloohms'
    return str(int(ohm_value)) + metric