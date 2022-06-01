# Caesar's cipher
The program is Python script version of one of the simplest encryption techniques.
## Use
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.  [Source: Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher).

This program does encoding in right shift, and decoding in left shift.
When program is being run, the user will be asked for:
- direction (encode or decode)
- text input 
- moving rate (int number that represents degree of letter shift.
Direction input determines what function is called. Text input and moving rate are then passed as arguments to wanted function which return ciphered or deciphered text as string.

## Functions and modules
The program does not use any modules.

```python
encrypt(text, change)
```
This function right-shifts passed string argument for number of places specified by the change argument. 
It uses empty string named "ciphered" and a foor loop to loop through string, and, if character is in signs list, it is left as it is and added to ciphered, but, if the character is in alphabet list, it is shifted and added to ciphered.
The function returns "ciphered" variable.

```python
decrypt(text, change)
```
This function works by the same mechanism as encrypt(), but, in the left direction.

## Workflow 
Simple "if" statement determines, on the base of user "direction" input, which function will be used. Then, printed f string displays returned string in the terminal.

## Running the game
This game is intended to be run by Python IDE or other Python interpeter. 
To install Python 3 see [Tutorials Point page](https://www.tutorialspoint.com/how-to-install-python-in-windows).
