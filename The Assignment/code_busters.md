# Code Busters

You are a high school student in the 31st century interested in Computer Science. In a time travel mishap, you became trapped in the year 1940 just before the Enigma Machine had been cracked by famous Computer Scientist Alan Turing. However, this has caused Alan Turing to disappear. You now must pose as Alan Turing and crack the Enigma Machine yourself to avoid any causality effects!

## The process

In this activity, you will write some code to crack codes. These codes are simpler ciphers than the Enigma Machine. However, the idea behind it is related to how the early versions of the German Enigma machine was cracked.

# **Instructions for cipher.py**

## Simple Substitution Ciphers

A **substitution cipher** is when every letter of the alphabet is mapped to a different letter. You will write some code to encode and decode messages.  
A simple case of this might be described as follows:

`A B C D E F G H I J K L M N O P Q R S T U V W X Y Z`  
`J K L M N W X C D P Q R S T U V A E F O B G H I Z Y`  

Each letter in the top line (called the *plaintext*) will get changed into the corresponding letter in the bottom line (called the *codestring*).
For example the string `"HELLO"` is **encoded** as `"CNRRU"` using the code above.
The string `"GDLOUEZ"` is **decoded** as `"VICTORY"`.

It is not too hard to decode such a code if you know the codestring for the whole alphabet. Here is some code that prints a decoded output. We'll call the string we want to decode as the ciphertext. 

```python
alphabet =   "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
codestring = "BCDEFGHIJKLMNOPQRSTUVWXYZA"
ciphertext = "IFMMPXPSME"

for char in ciphertext:
    print(alphabet[codestring.index(char)], end = "")
```

```python
# Output
HELLOWORLD
```

## What to do

You will be adding support to the Cipher class for codeword substitution ciphers.

1. Write a constructor for the Cipher class that takes a codestring and stores both the code (the mapping of a alphabet to it's codestring) and its inverse in two dictionaries.
2. Write an `encode` method for the `Cipher` class that takes a plaintext as input and returns the corresponding ciphertext.
3. Write a `decode` method for the `Cipher` class that takes a ciphertext as input and returns the corresponding plaintext.

## Hints

1. Adapt your code so that it automatically converts plaintext, ciphertext, and codestrings to uppercase.  Use the `str.upper()` method.
This method returns an uppercase version of the string so, for example,  `'Hello'.upper() == 'HELLO'`.
2. The `encode` and `decode` methods should leave all spaces and punctuation in place. This will mean that you should check if the letter is in the code and leave it if not. Checking if a key `k` is in a dictionary `D` can be done by writing `if k in D:`.

# **Instructions for ciphercracker.py**

## Breaking Substitution Ciphers

It is possible to break simple substitution ciphers without even using a computer. This is why, for example, such puzzles appear in newspapers. In this activity, you will write a program that automatically decodes a variant of these codes without knowing the codestring in advance 😨.

## Codeword Substitution

One approach to defining a codestring for a substitution cipher is to specify a *codeword* instead.  The idea is that a codeword (with no repeating letters is given) and that is used as the start of the codestring.  The rest of the codestring is filled in with the remaining letters of the alphabet in reverse order.  For example, if the codeword is `ZEBRA`, then the codestring would be:

`ZEBRAYXWVUTSQPONMLKJIHGFDC`

If the codeword is `DOG`, then the codestring would be:

`DOGZYXWVUTSRQPNMLKJIHFECBA`

You will want to be able to generate such a codestring from a codeword.  Here is the code I used to extend the codeword into a codestring.

```
w = 'DOG'
cs = ''
for a in 'ZYXWVUTSRQPONMLKJIHGFEDCBA':
    if a not in w:
        cs = cs + a
```

## Hiding Codewords in Plain Sight

In the kingdom of Vulgaria, instead of choosing a cipher in advance, the spies send coded messages that all start with a string of 30 characters that we'll call the **preamble**.  The codeword for the cipher is a substring of those first 30 characters.  They have some secret way of finding the codeword in there, so they can decode messages.

Their idea is that they want anyone deciphering the messages to break a new code for each message. Maybe this would work until word gets out that the codeword is hiding in plain sight. Now code breakers can try all the different substrings of those first 30 characters and see which one produces a message that looks like real words.

Incidentally, this is related to how the early versions of the German Enigma machine was cracked.

## Using data

You can get a program to do this for you.  You will be given a list of frequently used words.  Use this list to check if you have the correct codeword.  Then try all the different choices and see which one produces something the *looks like* a real message.

If we have a guess at what the codestring is, we can try to decode the message.   Then, we can look at it to see if it resembles a real message, for example by checking if the words are real words. If there is a small number of possible codestrings, we can choose between them by checking which produces the largest

There is a file called `words.py` included in the skeleton.  It contains a string with a big collection of words. You can import the variable `wordlist` from `words.py` using the following line of python at the top of your `ciphercracker.py` file.

`from words import wordlist`

You will then be able to use the wordlist variable in your code.
This approach is not considered great style, but it is easy and appropriate for this case.

## Your mission
1. Add support to the Cipher class for codeword substitution ciphers.
2. Finish the implementation of the class `CipherCracker`.  A `CipherCracker` object should store a ciphertext that you are trying to decode. It should separate out the preamble from the beginning of the ciphertext. Finish implementing the methods called `decode`, `quality`, `mostlikelydecode`, and `mostlikelycodeword`. The description of the desired input and output of each method is given in the skeleton code.