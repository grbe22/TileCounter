# TileCounter
A simple python program to count, and display, unique 8x8 tiles in images.

This  was done over the course of September 30th, 2023, to help a friend in a Gameboy-themed art contest.
They were allowed a canvas of 160x144, but there may only be 192 unique tiles - 8x8 positions on the image.
This program counts the number of unique tiles, and displays an image where the first instance of each unique tile is marked with white.

Due to the small constraint of this challenge, storing each tile as a 2D array with a 4-value tuple was enough, but it becomes woefully inefficient in larger canvas sizes.
My first draft ran in O(n^2). It took ~ .08 seconds to run on a 160x144 canvas. By changing to a set, and converting the 32-byte tuple into a 3-byte string, I halved this runtime.
Additionally, on a larger canvas (2208x2944) which took ~ 1 miunte to process the first 50 lines, this optimization brought the entire image comparison down to a ~14 second runtime.

1. Python runs slow; I could attempt to load the image in c for a much faster runtime, but I must first familiarize myself with appropriate libraries.
2. The original project only requires 2 bits for each color, as gameboys have four available colors. This could theoretically quarter runtime, but wouldn't work with real-life images like the 2208x2944 image I tested.
3. Alternatively, I could attempt to check each tile in parallel, separating them as they become indistinct until each group of tile only has 1 member or reaches the end.
