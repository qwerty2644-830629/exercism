def rows(letter):
    ascii = ord(letter) - 65
    output = []
    for i in range(ascii+1):
        if i == 0:
            string = ' ' * ascii + chr(i+65) + ' ' * ascii
        else:
            string = ' ' * (ascii - i) + chr(i+65) + ' ' * (2*i -1) + chr(i+65) + ' ' * (ascii - i)
        output.append(string)

    return output + [output[-(i+1)] for i in range(1, len(output))]