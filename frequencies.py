"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        item=str(item)
        if item in frequencies.keys():
            frequencies[item]+=1
        else:
            frequencies[item]=1
    return frequencies
