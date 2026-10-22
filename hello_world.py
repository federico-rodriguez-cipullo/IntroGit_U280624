# My first file tracked by git
# Author: Federico Rodriguez Cipullo

def greet(name):
    """Return a welcome message for the given name."""
    print(f"Hello {name}! Welcome to Git.")

# This block runs only when the file is excecuted directly,
# not when it is imported as a module from another file.

if __name__ == "__main__":
    print(greet("World"))