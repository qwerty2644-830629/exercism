def resistor_label(colors):
    OHMS_CODE= {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
                 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    
    TOLERANCE_CODE = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5,
                      'brown': 1, 'red': 2, 'gold': 5, 'silver': 10}
    if len(colors) < 4: return '0 ohms'
        
    # Value

    value = 0
    for color in colors[:-2]: value = value * 10 + OHMS_CODE[color]
    value *= (10 ** OHMS_CODE[colors[-2]])

    # Unit
    metric_list = ['ohms', 'kiloohms', 'megaohms', 'gigaohms']
    metric = metric_list[0]
    for i in range(3, 0, -1):
        if  value >= 10 ** (i*3):
            value /= 10 ** (i*3)
            metric = metric_list[i]

    
    return f"{value:g} {metric} ±{TOLERANCE_CODE[colors[-1]]}%"