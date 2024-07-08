# Seby's Square-1 Image Generator

### https://sq1-img-gen.reflex.run

## Made using [Reflex](https://github.com/reflex-dev/reflex)!

This Square-1 image generator is designed to be customizable to your heart's content!

### Here's how to use it:

1. Choose your input type.
    - **Case**: Your input will solve the Square-1 in the generated image.
        - *This input type is inteded for algset designers. It works by inverting the input and then applying it (so that the image generated will be the case the algorithm solves). Be careful in that the inverted input can be applied properly (in the context of algsets, this usually means starting and ending in cubeshape with no misaligned layers).*
    - **Algorithm**: Your input will be applied to a solved Square-1 to generate the image.
    - **State**: Your inputted [sq1optim](https://www.jaapsch.net/puzzles/square1.htm#progs) state will be the Square-1's state in the generated image.

<br>

2. Input your Case/Alg/State in the text area.
    - **Case** and **Alg** read standard Square-1 notation, **State** reads standard [sq1optim](https://www.jaapsch.net/puzzles/square1.htm#progs)/[virtual-sq1](https://github.com/Wo0fle/virtual-sq1/blob/main/docs/jared19.md) notation.

<br>

3. Choose your rendering type.
    - **Normal**: Generates a fully colored Square-1 (including side colors).
    - **Orientation**: Generates a Square-1 with only top and bottom colors (and a monochrome equator, if applicable).
    - **Shape**: Generates a monochrome Square-1.

<br>

4. Choose which layers to include.
    - You can choose to include any combination of **top**, **bottom**, and **equator** layers (so long as you choose **at least one**).

<br>

5. Choose image orientation.
    - You can choose **vertical** or **horizontal**.

<br>

6. Click <span style="border:3px solid blue;padding:5px;border-radius:10px">Generate</span> , and your generated image should appear on the right!

<br>

7. Right-click and save the `.svg` file, and that's it!

<br><hr>

### Advanced Settings:

- **Custom color scheme:** In the works!
- **Custom extension factor:** In the works!
- **Custom border color:** In the works!
- **Turning on/off slice indicator:** In the works!

<br>

- **Error messages:** Hopefully will be added.
- **Exporting to `.png`:** Hopefully will be added.
- **Graying out particular pieces:** Hopefully will be added.

<br>

- **Labeling particular pieces:** May or may not be added.
- **Custom background color:** May or may not be added.

<br>

- **Built-in optimal solver (using [Jaap's Square-1 Optimiser (modified by Doug Benham)](https://github.com/dougbenham/Square1-Optimizer)):** Likely won't be added, but it's on my mind.