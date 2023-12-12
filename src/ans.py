""" 
2. Transformative Quote (Enhances 2-5, 2-6)

Task: Choose a quote from a famous person and assign it to a variable. Create a function that takes this quote and performs the following transformations sequentially: a) converts it to uppercase, b) replaces spaces with underscores, c) appends the length of the quote at the end. Display the transformed quote and ensure your function can handle any string passed to it.

Key Concepts: String methods, functions, len() function.
"""

def transform_quote(quote):
    return f"{quote.replace(' ', '_').upper()}{len(quote)}"