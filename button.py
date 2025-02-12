def button_sequences(seqR, seqB):

    result = ""
    red_pressed = False
    blue_pressed = False

    for i in range(len(seqR)):
        r = seqR[i]
        b = seqB[i]

        if r == '1' and not red_pressed and not blue_pressed:
            result += "R"
            red_pressed = True
        elif r == '0' and red_pressed:
            red_pressed = False
            if b == '1' and not blue_pressed: 
                result += "B"
                blue_pressed = True
            elif b == '0' and blue_pressed:
                blue_pressed = False

        if b == '1' and not blue_pressed and not red_pressed:
            result += "B"
            blue_pressed = True
        elif b == '0' and blue_pressed:
            blue_pressed = False
            if r == '1' and not red_pressed:  
                result += "R"
                red_pressed = True
            elif r == '0' and red_pressed:
                red_pressed = False
            

    return result