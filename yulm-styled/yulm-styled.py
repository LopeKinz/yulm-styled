import sys
import time

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

class BackgroundColor:
    """
    Class representing ANSI escape codes for background color.
    """
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'

def colorize_text(text, color, background=None):
    """
    Colorizes the given text with the specified color and background.
    """
    color_code = color
    background_code = background if background else ''
    return f"{background_code}{color_code}{text}{Color.RESET}"


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

class Colorr:
    """
    Class representing ANSI escape codes for text color.
    """
    RESET = '\033[0m'
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)

def fade_color(text, from_color_name, to_color_name, duration=1.0):
    """
    Fades the specified text from left to right with a gradual color change.
    The user can specify the color names (e.g., "RED", "BLUE").
    The number of steps is calculated based on the duration.
    """
    from_color = getattr(Colorr, from_color_name.upper(), Color.WHITE)
    to_color = getattr(Colorr, to_color_name.upper(), Color.WHITE)

    steps = int(duration * 10)
    sleep_time = duration / steps

    text_length = len(text)
    r_step = (to_color[0] - from_color[0]) / text_length
    g_step = (to_color[1] - from_color[1]) / text_length
    b_step = (to_color[2] - from_color[2]) / text_length

    for i, char in enumerate(text):
        r = int(from_color[0] + i * r_step)
        g = int(from_color[1] + i * g_step)
        b = int(from_color[2] + i * b_step)

        sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}")
        sys.stdout.flush()
        time.sleep(sleep_time)

    sys.stdout.write(Color.RESET + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    # Example usage
    print(colorize_text("Hello, World!", Color.RED))
    print(fade_text("Hello, World!", FadedColor.YELLOW))
    print(rainbow_text("Hello, World!"))
    fade_color("Hello, World!", "RED", "GREEN", duration=2.0)
