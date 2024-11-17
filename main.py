"""This module handles the initialization and execution of the project.
Make sure to organize imports and configurations correctly."""

from config import WIDTH, PAUSE_AMOUNT, LEFT_WIDTH, GAP_WIDTH
from deepcave.deepcave import deepcave

if __name__ == "__main__":
    deepcave(WIDTH, PAUSE_AMOUNT, LEFT_WIDTH, GAP_WIDTH)
