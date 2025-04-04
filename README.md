# Seby's Square-1 Image Generator

### https://sq1-img-gen-gold-grass.reflex.run

![Square-1 image generated using SSIG](./docs/images/example.svg)

## Made using [Reflex](https://github.com/reflex-dev/reflex)!

This Square-1 image generator is designed to be customizable to your heart's content!

### Here's how to use it:

1. Choose your input type.
    - **Case**: Your input will solve the Square-1 in the generated image.
        - *This input type is intended for algset designers. It works by inverting the input and then applying it (so that the image generated will be the case the algorithm solves). Be careful in that the inverted input can be applied properly (in the context of algsets, this usually means starting and ending in cubeshape with no misaligned layers).*
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

6. If it hasn't already loaded correctly, click the "**Reload Image**" button, and your generated image should appear on the right!
    - I like clicking the button after I am done changing my desired settings, just in case something is generated incorrectly and I can't tell at a glance.
    - If there is an error with the input, it will generate an image of a solved Square-1. If you weren't expecting a solved Square-1, check your input for typos, and make sure you chose the correct input type.
        - I am working on adding error messages, so errors should be more clear after I do that!

<br>

7. Right-click and save the `.svg` file, and that's it!

<br><hr><br>

### Advanced Settings:

- **Custom colors:** Input any valid RGB value into the text box to change that part of the image to your desired color!
    - This includes all the sides (for Normal and Orientation renders), the border (for all renders), and the shape color (for equator in Orientation render and everything in Shape render).
- **Custom extension factor:** Input any numerical value to change how far the pieces extend into/out of the top/bottom sides!
    - Values above 1 lead to the sides sticking out of the top/bottom. Values below 1 lead to the sides sticking into the top/bottom. A value of 1 leads to no visible side colors on the top/bottom layers (but you will be able to see them on the equator). Values below 0 lead to some weird-looking things that kind of look cool sometimes.
- **Toggle slice indicator:** Choose to remove the line running through the slice of the Square-1!

<br><hr><br>

### Known Bugs:

- **Color indicator circles don't work**
    - no clue why they dont update (might have to do with the fact that it's an `rx.box`?) but oh well maybe one day ill figure it out
- **Changing a setting too fast makes that setting stop working**
    - yeah man idk, thats why i added the reload image button. might just go back to a "generate image button" to avoid this cuz im fairly sure it has to do with the time it takes to generate the image

<br><hr><br>

- **Exporting to `.png`:** Currently working on it!

<br>

- **Error messages:** Hopefully will be added. **REQUIRES UPDATING [virtual-sq1](https://github.com/Wo0fle/virtual-sq1)**
- **Graying out particular pieces:** Hopefully will be added.

<br>

- **Labeling/coloring particular pieces:** May or may not be added.
- **Custom background color:** May or may not be added.

<br>

- **Built-in optimal solver:** Likely won't happen, but it's on my mind.
