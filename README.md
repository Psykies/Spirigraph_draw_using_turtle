
# Random Color Spirograph

This Python script generates a spirograph using the Turtle module in Python. Each circle drawn in the spirograph has a randomly selected color.

## Description

The spirograph is a geometric drawing toy that produces mathematical curves known as hypotrochoids and epitrochoids. This script utilizes the Turtle module in Python to draw circles with random colors, creating visually appealing spirograph patterns.

## Features

- Draws a spirograph with circles of random colors.
- Allows customization of the gap size between circles.

## Usage

1. Ensure you have Python installed on your system.
2. Clone or download the repository containing the script.
3. Run the script using a Python interpreter.
4. Watch as the spirograph is drawn with random colors.

## How it Works

- The script first imports the necessary modules, including Turtle and random.
- It defines a function `random_color()` to generate a random color for each circle.
- The `draw_spirograph()` function is then defined to draw the spirograph using circles with random colors.
- The script sets the speed of drawing to "fastest" using the `speed()` method.
- Finally, it calls the `draw_spirograph()` function with a specified size of the gap between circles and displays the spirograph on the screen.

## Example

The following example demonstrates how to use the script to generate a spirograph with circles of random colors:


draw_spirograph(5)



This will draw a spirograph with circles and a gap size of 5 units between each circle.

## Requirements

- Python 3.x
- Turtle module (included in standard Python distribution)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


