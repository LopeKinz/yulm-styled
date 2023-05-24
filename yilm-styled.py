import sys


class Color:
    """
    Class representing ANSI escape codes for text color.
    """
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'


class FadedColor:
    """
    Class representing ANSI escape codes for faded text color.
    """
    BLACK = '\033[30;1m'
    RED = '\033[31;2m'
    GREEN = '\033[32;2m'
    YELLOW = '\033[33;2m'
    BLUE = '\033[34;2m'
    MAGENTA = '\033[35;2m'
    CYAN = '\033[36;2m'
    WHITE = '\033[37;2m'
    GRAY = '\033[90;2m'


class RainbowColor:
    """
    Class representing ANSI escape codes for rainbow text color.
    """
    COLORS = [Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE, Color.MAGENTA, Color.CYAN]

    @staticmethod
    def get_color(index):
        return RainbowColor.COLORS[index % len(RainbowColor.COLORS)]


def colorize_text(text, color):
    """
    Colorizes the given text with the specified color.
    """
    return f"{color}{text}{Color.RESET}"


def fade_text(text, color):
    """
    Applies faded color to the given text.
    """
    return f"{color}{text}{Color.RESET}"


def rainbow_text(text):
    """
    Applies rainbow color to the given text.
    """
    rainbow_text = ""
    for i, char in enumerate(text):
        color = RainbowColor.get_color(i)
        rainbow_text += f"{color}{char}"
    rainbow_text += Color.RESET
    return rainbow_text


if __name__ == "__main__":
    # Example usage
    print(colorize_text("Hello, World!", Color.RED))
    print(fade_text("Hello, World!", FadedColor.YELLOW))
    print(rainbow_text("Hello, World!"))
