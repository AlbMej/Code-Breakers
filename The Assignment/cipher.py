class Cipher:
    def __init__(self, codestring):
        # Hints: 
        # Does the capitalization of the words or letter matter here? 
        # Is hello the same as Hello or even hElLo in terms of definition? Yes
        # Maybe we should convert everything to uppercase

        # Add your code here
        self.alphabet = None # Add alphabet here by replacing None with the answer 
        self.codestring = ""

        for letter in 'ZYXWVUTSRQPONMLKJIHGFEDCBA':
            if None not in codestring: # Replace None with answer     
                self.codestring += None # Replace None with answer        
        self.codestring = codestring + self.codestring 

        self.code = {}
        for (a,b) in zip(self.codestring.upper(), None): # Replace None & "None2" with the answers
            self.code["None2"] = None

        self.inverse = {}
        for (a,b) in zip(None, self.alphabet):
            self.inverse[None] = "None2" # Replace None & "None2" with the answers
        
    def encode(self, plaintext):
        # Add your code here
        encoded_string = ""
        for c in None: #Replace None with the answer
            if c.isalpha():
                encoded_string += None #Replace None with the answer
            else:
                encoded_string += None
        return "".join(encoded_string)


    def decode(self, ciphertext):
        # Add your code here
        decoded_string = "" 
        for c in None: #Replace None with the answer
            if None:   #Replace None with the answer
                decoded_string += self.code[None] #Replace None with the answer   
            else:
                None #Replace None with the answer (it's 1 line of code)
        return "".join(decoded_string)
