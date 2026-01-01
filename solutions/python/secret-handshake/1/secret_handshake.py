def commands(binary_str):
    actions = ['wink', 'double blink', 'close your eyes', 'jump', 'Reverse']
    handshake = []
    
    for i, number in enumerate(binary_str):
        if number == '1': handshake.insert(0, actions[4 - i])

    if 'Reverse' in handshake:
        handshake = [handshake[len(handshake)- 1 - i] for i in range(len(handshake))]
        handshake = handshake[1:]

    return handshake