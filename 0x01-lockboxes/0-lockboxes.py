#!/usr/bin/python3
"""Creates a function to check if a box with nested lists
   can be unlocked using keys found within those lists.
"""


def canUnlockAll(boxes):
    """This checks if boxes can be opened"""
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
