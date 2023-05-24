# yulm-styled

This Python module provides utilities for colorizing text with various effects such as faded colors and rainbow colors.

## Usage

To use this module, import it into your Python script:

```python
import sys
import time
from yulm-styled import Color, FadedColor, RainbowColor, colorize_text, fade_text, rainbow_text, fade_color
```

### Colorizing Text

To colorize a text with a specific color, use the `colorize_text` function:

```python
colored_text = colorize_text("Hello, World!", Color.RED)
print(colored_text)
```

Output:
```
Hello, World! (with the color)
```

### Faded Text

To apply faded color to a text, use the `fade_text` function:

```python
faded_text = fade_text("Hello, World!", FadedColor.YELLOW)
print(faded_text)
```

Output:
```
Hello, World! (Faded out Color)
```

### Rainbow Text

To apply rainbow color to a text, use the `rainbow_text` function:

```python
rainbow_text = rainbow_text("Hello, World!")
print(rainbow_text)
```

Output:
```
Hello, World! (Rainbow Colors)
```

### Fading Color

To fade the color of a text from one color to another, use the `fade_color` function:

```python
fade_color("Hello, World!", "RED", "BLUE", duration=2.0)
```

Output:
```
Hello, World! (From Red to Blue in a nice gradiend)
```

## Color Class

The `Color` class provides ANSI escape codes for standard text colors. It includes the following color constants:

- `Color.RESET`
- `Color.BLACK`
- `Color.RED`
- `Color.GREEN`
- `Color.YELLOW`
- `Color.BLUE`
- `Color.MAGENTA`
- `Color.CYAN`
- `Color.WHITE`
- `Color.GRAY`

## FadedColor Class

The `FadedColor` class provides ANSI escape codes for faded text colors. It includes the following color constants:

- `FadedColor.BLACK`
- `FadedColor.RED`
- `FadedColor.GREEN`
- `FadedColor.YELLOW`
- `FadedColor.BLUE`
- `FadedColor.MAGENTA`
- `FadedColor.CYAN`
- `FadedColor.WHITE`
- `FadedColor.GRAY`

## RainbowColor Class

The `RainbowColor` class provides ANSI escape codes for rainbow text colors. It includes the following method:

- `RainbowColor.get_color(index)`: Returns the ANSI escape code for the color at the specified index in the rainbow sequence.

## fade_color Function

The `fade_color` function fades the specified text from left to right with a gradual color change. The user can specify the color names (e.g., "RED", "BLUE"). The number of steps is calculated based on the duration.

```python
fade_color(text, from_color_name, to_color_name, duration=1.0)
```

- `text`: The text to be faded.
- `from_color_name`: The name of the starting color.
- `to_color_name`: The name of the ending color.
- `duration`: The duration of the fade animation in seconds (default: 1.0).

## License

This module is released under the MIT License. See [LICENSE](LICENSE) for more information.
