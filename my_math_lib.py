# File: my_math_lib.py
"""
A simple math library for demonstrating Git workflow.
Contains basic mathematical operations.
"""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b
    
def mul(a,b):
    return a*b
    
def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a**b
    
