from sys import stdout
from timeit import default_timer
from random import shuffle

from GameParser import game_parser
from gen_graphics import gen_graphics
from GetKBChar import getch

write = stdout.write # Faster alternative to print
ESC = chr(27)
CSI = ESC + '['

def main():
    # Text preparation
    with open('Dictionary/en.txt') as f: words = f.read().split('\n')[:-1]
    shuffle(words)
    text_to_write = ' '.join(words[:vars(game_parser())['words']])
    text_written = ''

    # Terminal preparation
    write(f'{CSI}?25l')         # Hide cursor
    write(f'{CSI}2J{CSI}H')     # Erase entire screen
    write(text_to_write)
    stdout.flush()

    # Run
    start = default_timer()
    while key := getch():
        if key == '\x7f': # DEL
            text_written = text_written[:-1]

        elif key != '\n': # Alphabet key (probably)
            text_written += key if len(text_written)<len(text_to_write) else ''
            if text_written == text_to_write:
                write('\x1b[2J\x1b[H') # Clear and put cursor on TOP
                write(gen_graphics(text_to_write, text_written))
                stdout.flush()

                break

        write('\x1b[2J\x1b[H') # Clear and put cursor on TOP
        write(gen_graphics(text_to_write, text_written))
        stdout.flush()
        
            
    end = default_timer()
    time = (end - start) / 60 # Minutes

    # https://www.typingtyping.com/wpm-calculator/
    GROSS_WPM = (len(text_written) / 5) // time

    write(f'\n{GROSS_WPM}\n')

if __name__ == '__main__':
    try:

        main()

    except KeyboardInterrupt:
        write('\n')

    finally:
        write(f'{CSI}?25h')                         # Cursor visible
        write(f'{CSI}0m')                           # RST STY and COL
