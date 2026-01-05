def resistor_label(colors):
    Ohms_code = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
                 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    
    Tolerance_code = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5,
                      'brown': 1, 'red': 2, 'gold': 5, 'silver': 10}
    if len(colors) < 4: return '0 ohms'
        
    # Value

    value = 0
    for color in colors[:-2]: value = value * 10 + Ohms_code[color]
    value *= (10 ** Ohms_code[colors[-2]])

    # Unit
    metric_list = ['ohms', 'kiloohms', 'megaohms', 'gigaohms']
    metric = metric_list[0]
    for i in range(3, 0, -1):
        if  value >= 10 ** (i*3):
            value /= 10 ** (i*3)
            metric = metric_list[i]

    
    return f"{value:g} {metric} ±{Tolerance_code[colors[-1]]}%"