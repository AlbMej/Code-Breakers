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

        slice_index = None # Replace None
        self.preamble = ciphertext[:slice_index]
        self.ciphertext = ciphertext[slice_index:]

    def decode(self, i, j):
        """
        Attempts to decode the message using self.preamble[i:j] as the codeword.
        Returns the resulting string.
        """

        codeword = Cipher(None)  # Replace. Hint: read description
        return codeword.decode(None) # Replace None. What does decode take again in the Cipher class? 

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

        messages = self.decode(None, None).split()
        count = None # Replace
        for i in None: # Replace
            if i in None: # Replace:
                count += None # Replace
        return count


    def mostlikelycodeword(self):
        """
        Return the codeword that has the highest quality score among all
        substrings of the preamble.
        """

        # Add your code here
        stoping_int = None # Replace
        best, first_index, last_index = None, None, None # Replace all three with an integer
        for i in range(stoping_int):
            for j in range(None, stoping_int): # Replace None. 
                current = self.quality(None, None)
                if None > None # Replace both Nones
                    best, first_index, last_index = current, i, j
        return self.preamble[None:None]

    def mostlikelydecode(self):
        """
        Return the decoded message that you get by decoding with the most
        likely codeword.
        """

        # Add your code here
        most_likely_codeword = Cipher(None) # Replace None with a method
        return most_likely_codeword.decode(None) # Replace None. What does decode take again in the Cipher class? 
        