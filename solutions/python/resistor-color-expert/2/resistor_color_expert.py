def resistor_label(colors):
    ohms_code = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
                 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    tolerance_code = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5,
                     'brown': 1, 'red': 2, 'gold': 5, 'silver': 10}
    metric_list = ['ohms', 'kiloohms', 'megaohms', 'gigaohms']
    value = 0
    metric = 'ohms'

    # Value
    if len(colors) < 4: return '0 ohms'
    for i, color in enumerate(colors[:-2]): value += (10 ** (len(colors) - 3 - i)) * ohms_code[color]
    value *= (10 ** ohms_code[colors[-2]])

    # Unit
    for i in range(3, 0, -1):
        print(value, value >= 10 **(i*3) ,value /10 ** (i*3) )
        if  value >= 10 ** (i*3):
            value /= 10 ** (i*3)
            metric = metric_list[i]
    if value % 1.0 == 0: value = int(value)
    
    return f'{str(round(value,2))} {metric} ±{tolerance_code[colors[-1]]}%'