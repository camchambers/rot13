# ROT13 Cipher
An example of a [ROT13 cipher](https://en.wikipedia.org/wiki/ROT13) in Python. 

Applies a ROT13 cipher from standard input where each character is rotated 13 spaces. 

Disclaimer: This code is for learning purposes only and should never be used for practical purposes as it is easily reversable.

![ROT13 Cipher Example](/../screenshots/screenshots/example.png?raw=true)

## Examples

### Text Input
Pipe the input "abc" into the script which rotates each character by 13 spaces resulting in the output "nop". 
```
echo "abc" | ./rot13.py
```

### File Input
Read the contents of a file as input and redirect output to a file. 
```
./rot13.py < poem.txt > rot13_output.txt
```
