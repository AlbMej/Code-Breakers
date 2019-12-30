# Code Busters

## Encryption  

## Enigma Machine

## The process

## Your mission

1. Write a constructor for the Cipher class that takes a codestring and stores both the code and its inverse in two dictionaries.
2. Write an `encode` method for the `Cipher` class that takes a plaintext as input and returns the corresponding ciphertext.
3. Write a `decode` method for the `Cipher` class that takes a ciphertext as input and returns the corresponding plaintext.
4. Finish the implementation of the `CipherCracker`.  A `CipherCracker` object should store a ciphertext that you are trying to decode. It should separate out the preamble from the beginning of the ciphertext. Finish implementing the methods called `decode`, `quality`, `mostlikelydecode`, and `mostlikelycodeword`. The description of the desired input and output of each method is given in the skeleton code.