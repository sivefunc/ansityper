import termios
import tty
import sys

def getch(ch=1, stream=sys.stdin):
    """
    Get the keyboard press one character at a time of a Unix like tty
    """

    old_settings = termios.tcgetattr(sys.stdin) # Save terminal settings
    try:
        tty.setcbreak(sys.stdin) # Read one character at a time
        return stream.read(ch)
    
    except IOError:
        pass

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSANOW, old_settings) # Reset it
