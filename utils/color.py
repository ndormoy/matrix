def colorize_text(text, color):
    """
    Colorize the provided text using ANSI escape codes.

    Parameters:
        text (str): The text to colorize.
        color (str): The color to apply (e.g., 'red', 'green', 'blue').
    """
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }

    if color in colors:
        print(f"{colors[color]}{text}{colors['reset']}")
    else:
        print(text)