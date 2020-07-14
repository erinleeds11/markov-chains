from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.

    """
    file = open(file_path)
    contents = file.read()
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """


    words = contents.split()

    words.append(None) #so it ends at None and you dont get key error

    chains = {}

    for i in range(len(words)-2):
        key = (words[0], words[1])
        value = words[i+2]
        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return chains



def make_text(chains):
    """Return text from chains."""

    words = []

    rando_key = choice(list(chains.keys()))
    words = [rando_key[0], rando_key[1]]
    rando_word = choice(chains[rando_key])

    while rando_word is not None:
        rando_key = (rando_key[1], rando_word)
        words.append(rando_word)
        rando_word = choice(chains[rando_key])

    return " ".join(words)

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)








