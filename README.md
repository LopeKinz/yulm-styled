# YULM Styled

YULM Styled is a Python module that provides ANSI escape codes for text and background color styling. It allows you to add colorful and visually appealing text to your command-line applications.

## Features

- Text colorization using ANSI escape codes
- Faded text colors for a subtle effect
- Rainbow text with changing colors
- Background colors for text

## Usage

### Text Colorization

You can colorize your text by using the `colorize_text` function:

```python
import yulm_styled

# Specify the text and color
text = "Hello, World!"
color = yulm_styled.Color.RED

# Colorize the text
colored_text = yulm_styled.colorize_text(text, color)

# Print the colored text
print(colored_text)
```

### Faded Text Color

You can apply faded color to your text using the `fade_text` function:

```python
import yulm_styled

text = "Hello, World!"
color = yulm_styled.FadedColor.YELLOW

faded_text = yulm_styled.fade_text(text, color)

print(faded_text)
```

### Rainbow Text

To apply a rainbow effect to your text, use the `rainbow_text` function:

```python
import yulm_styled

text = "Hello, World!"

rainbow_text = yulm_styled.rainbow_text(text)

print(rainbow_text)
```

### Background Color

You can add background colors to your text by using the `colorize_text` function with the `background` parameter:

```python
import yulm_styled

text = "Hello, World!"
color = yulm_styled.Color.RED
background = yulm_styled.BackgroundColor.YELLOW

colored_text = yulm_styled.colorize_text(text, color, background)

print(colored_text)
```

## Adding More Colors

If you want to add more colors, you can modify the module by extending the existing color classes (`Color`, `FadedColor`, `RainbowColor`, `BackgroundColor`) with additional ANSI escape codes.

## License

This module is released under the MIT License. See [LICENSE](LICENSE) for more information.

## Author

- Author: LopeKinz
- GitHub: [https://github.com/lopekinz/yulm-styled](https://github.com/lopekinz/yulm-styled)


