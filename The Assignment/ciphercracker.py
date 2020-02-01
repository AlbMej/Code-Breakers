# Add wordlist import here
from cipher import Cipher

class CipherCracker:
    def __init__(self, ciphertext):
        """
        The constructor takes a ciphertext that is assumed to have a preamble
        of 30 characters that contains the codeword.

        The preamble is removed from the ciphertext and stored separately.
        When we decode the message, we will omit the preamble.
        """

        # Add your code here
        pass

    def decode(self, i, j):
        """
        Attempts to decode the message using self.preamble[i:j] as the codeword.
        Returns the resulting string.
        """

        # Add your code here
        pass

    def quality(self, i, j):
        """
        Decodes the message using self.preamble[i:j] as the codeword and returns
        a number that gives an indication of how many of the words in the
        decoded string are real words.  It does this by checking if the words
        are in the `wordlist` variable imported from `words.py`.

        There are several ways this could be done.  The most important thing is
        that for a real message, the correct values of i and j should give
        a higher output than other values.
        """

        # Add your code here
        pass


    def mostlikelycodeword(self):
        """
        Return the codeword that has the highest quality score among all
        substrings of the preamble.
        """

        # Add your code here
        pass

    def mostlikelydecode(self):
        """
        Return the decoded message that you get by decoding with the most
        likely codeword.
        """

        # Add your code here
        pass
        