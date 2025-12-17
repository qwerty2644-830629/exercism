def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob.isupper():
        response = "Whoa, chill out!"
        if hey_bob.endswith('?'):
            response = "Calm down, I know what I'm doing!"            
    elif hey_bob.endswith('?'):
        response = "Sure."
    elif not hey_bob:
        response = "Fine. Be that way!" 
    else:
        response = "Whatever." 
    return response