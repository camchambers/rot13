# ROT13 Cipher
An example of a [ROT13 cipher](https://en.wikipedia.org/wiki/ROT13) in Python. 

Applies a ROT13 cipher from standard input where each character is rotated 13 spaces. 

Disclaimer: This code is for learning purposes only and should never be used in practice as it is easily reversable.

![ROT13 Cipher Example](/../screenshots/screenshots/example.png?raw=true)

## Examples


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

