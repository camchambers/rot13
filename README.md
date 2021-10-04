# ROT13 Cipher
An example of a [ROT13 cipher](https://en.wikipedia.org/wiki/ROT13) in Python. 

Applies a ROT13 cipher from standard input where each character is rotated 13 spaces. 

Disclaimer: This code is for learning purposes only and should never be used for practical purposes as it is easily reversable.

![ROT13 Cipher Example](/../screenshots/screenshots/example.png?raw=true)

## Examples

<<<<<<< HEAD
### Piping Text as Input
```
echo "abc" | ./rot13.py
> Guvf vf n grfg
```
### Text as Input Using a Here String
```
 ./rot13.py <<< "This is a test"
> Guvf vf n grfg
```
### Text as Input Using a Here String and Shell Expansion
```
./rot13.py <<< $(date +'%B')
> Bpgbore
```

### Reading Input from a File
```
./rot13.py < poem.txt
```

### Reading Input from a File and Redirecting Output to a File
```
./rot13.py < poem.txt > rot13_output.txt
```

## Testing

Ensure that [pytest](https://docs.pytest.org/en/6.2.x/getting-started.html) is installed.

Run tests: 
```
pytest -v test_rot13.py
```
=======
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
>>>>>>> 8096573b9e0b318acc1930510a19542a9428f1a3
