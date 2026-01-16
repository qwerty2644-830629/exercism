def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    texts = text.split()
    new_text = ''
    for text in texts:
        if text.startswith('xr') or text.startswith('yt'):
            new_text += text + 'ay'
            continue
        for i, letter in enumerate(text):
            if letter == 'q' and text[i+1] == 'u':
                new_text += text[i+2:] + text[:i+2] + 'ay '
                break
            if letter in vowels:
                new_text += text[i:] + text[:i] + 'ay '
                break
            elif letter == 'y' and i != 0:
                new_text += text[i:] + text[:i] + 'ay '
                break
    return new_text.strip()