<img width="716" height="669" alt="Screenshot 2025-09-09 at 11 28 39 AM" src="https://github.com/user-attachments/assets/c0dd07d8-49b1-453c-9a5e-3df69b915e05" />

the code doesn't print by default lyrics that are empty ('')... so any of these keywords

```
REFRAIN, CROWD, RETURN, END
```

CODE in here 

<img width="716" height="350" alt="Screenshot 2025-09-09 at 11 31 09 AM" src="https://github.com/user-attachments/assets/d6e8c94c-1bdb-42af-b037-6fd73e286a6e" />

the conditional branches have some of the onesn that skip the print() statement

also flag is a variable, and is stdout several times. Nothing in the code writes the flag to a file, variable, or log.

```
# print() sends text directly to stdout (the console)
        print(line, flush=True)
        time.sleep(0.5)
        lip += 1
```
The flag is at the very start (line 0), but the script starts from [VERSE1]
```
elif re.match(r"RETURN [0-9]+", line):
    lip = int(line.split()[1])
```
trick the parsing with a ;
<img width="1432" height="700" alt="image" src="https://github.com/user-attachments/assets/d5acddec-47c5-480b-ba8b-de7e2cec295a" />
