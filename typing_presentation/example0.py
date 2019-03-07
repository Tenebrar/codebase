def my_function(a, b):
    """Do something with a and something else with b."""
    a.something()
    b.something_else()

# This becomes hard to understand in large codebases. In theory, this is solved by documentation, but in practice
# this is often not present or outdated.

# Subtle bugs may occur as a result of passing elements of the wrong type
