"""Deep Cave, by Al Sweigart al@inventwithpython.com
An animation of a deep cave that goes forever into the earth.
This code is available at
https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, scrolling, artistic"""

import random
import sys
import time


def deepcave(width, pause_amount, left_width, gap_width):
    """Main animation loop for Deep Cave."""
    while True:
        # Display the tunnel segment:
        right_width = width - gap_width - left_width
        print(('#' * left_width) + (' ' * gap_width) + ('#' * right_width))

        # Check for Ctrl-C press during the brief pause:
        try:
            time.sleep(pause_amount)
        except KeyboardInterrupt:
            sys.exit()  # When Ctrl-C is pressed, end the program.

        # Adjust the left side width:
        dice_roll = random.randint(1, 6)
        if dice_roll == 1 and left_width > 1:
            left_width -= 1  # Decrease left side width.
        elif dice_roll == 2 and left_width + gap_width < width - 1:
            left_width += 1  # Increase left side width.

        # Adjust the gap width (optional, currently commented out):
        dice_roll = random.randint(1, 6)
        if dice_roll == 1 and gap_width > 1:
            gap_width -= 1  # Decrease gap width.
        elif dice_roll == 2 and left_width + gap_width < width - 1:
            gap_width += 1  # Increase gap width.

        # Adjust the gap width:
        # (!) Try uncommenting out all of the following code:
        # dice_roll = random.randint(1, 6)
        # if dice_roll == 1 and gapWidth > 1:
        #    gapWidth = gapWidth - 1  # Decrease gap width.
        # elif dice_roll == 2 and left_width + gapWidth < WIDTH - 1:
        #    gapWidth = gapWidth + 1  # Increase gap width.
        # else:
        #    pass  # Do nothing; no change in gap width.
