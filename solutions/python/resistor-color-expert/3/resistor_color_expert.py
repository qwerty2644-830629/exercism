def resistor_label(colors):
    if len(colors) < 4: return '0 ohms'
        
    # Value
    ohms_code = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
                 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    value = 0
    for i, color in enumerate(colors[:-2]): value = value * 10 + ohms_code[color]
    value *= (10 ** ohms_code[colors[-2]])

    # Unit
    metric_list = ['ohms', 'kiloohms', 'megaohms', 'gigaohms']
    metric = metric_list[0]
    for i in range(3, 0, -1):
        print(value, value >= 10 **(i*3) ,value /10 ** (i*3) )
        if  value >= 10 ** (i*3):
            value /= 10 ** (i*3)
            metric = metric_list[i]
    if value % 1.0 == 0: value = int(value)

    tolerance_code = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5,
                      'brown': 1, 'red': 2, 'gold': 5, 'silver': 10}
    
    return f'{str(round(value,2))} {metric} ±{tolerance_code[colors[-1]]}%'