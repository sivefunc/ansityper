ESC = chr(27)
CSI = ESC + '['

def gen_graphics(text_to_write, text_written):
    RTX_TEXT = ''
    
    for ch_to_write, ch_written in zip(text_to_write, text_written):
        # You can do this one liner with ternary operators, but it would be
        # very hard to read

        if ch_to_write == ch_written: # Green color
            RTX_TEXT += f'{CSI}1;32m{ch_written}{CSI}0m' # FG

        else: # Red color
            if ch_written == ' ':
                RTX_TEXT += f'{CSI}1;41m {CSI}0m' # BG
            
            else:
                RTX_TEXT += f'{CSI}1;31m{ch_written}{CSI}0m' # FG

    text_left = len(text_to_write) - len(text_written)
    RTX_TEXT += text_to_write[::-1][:text_left][::-1]

    return RTX_TEXT + f'{CSI}0m'
