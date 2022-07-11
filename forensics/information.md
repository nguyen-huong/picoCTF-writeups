# Information

## Prompt
Files can always be changed in a secret way. Can you find the flag? cat.jpg

## Tools used
- https://fotoforensics.com/

## Solution
- Inspect image metadata using FotoForensics
- License found is a base64 string
```
echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d

picoCTF{the_m3tadata_1s_modified}%
```
