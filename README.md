# Windows 95 Keygen

windowskeygen.py - Generates Windows 95 and 95 OEM keys using the modulus 7 check algorithm. These keys also work on some licensed Microsoft applications of that era.


Just download and drop in the directory you are using for the script you're currently writing, or drop it in your python module directory to call it from anywhere.
Then just import the function as one does normally.

`keygen95()` - Generates a retail 95 key that works on all 95 era software, not just the OS.

`keygen95oem()` - Generates an OEM 95 key.


Some example uses:

Just print one of each key.
```python
import windowskeygen as wkg

print(wkg.keygen95())
print(wkg.keygen95oem())
```

Use a loop to generate 'n' keys.

```python
import windowskeygen as wkg

count = 15 # Generate 15 keys

while count > 0:
  print(wkg.keygen95())
  count = count - 1
```

Although Windows 95 and it's associated software is considered abandonware, Microsoft may not like the fact keys are being generated for it.
That being said, this is a proof of concept piece of sourcecode. I'm not responsible for how you choose to use it.
