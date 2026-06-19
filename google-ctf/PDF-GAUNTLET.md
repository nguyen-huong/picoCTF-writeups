# prompt: Find the parts of the flag hidden in this PDF file... see the .zip file attached

# part 3: 
```
cat document.pdf
```
<img width="927" height="444" alt="Screenshot 2026-06-19 at 1 28 17 PM" src="https://github.com/user-attachments/assets/48e2a23a-c06b-4ed2-886e-83497394a97e" />
Part3{1fFIc}

# part 4
```
strings document.pdf
```
<img width="927" height="662" alt="Screenshot 2026-06-19 at 1 28 55 PM" src="https://github.com/user-attachments/assets/723b4b4f-c29e-47bc-a59a-aa200ef3a456" />
Part4{uLt=-}

# part 6
```
└─$ exiftool e62126d9156e192e51cf7cc410ce747fff51e034bf65c65bdff7118e7a72e2100c7ca23684a2a2df7407a2ce11d5648045ad673b97726514e8cbf91d3abab3f9.zip 
ExifTool Version Number         : 13.50
File Name                       : e62126d9156e192e51cf7cc410ce747fff51e034bf65c65bdff7118e7a72e2100c7ca23684a2a2df7407a2ce11d5648045ad673b97726514e8cbf91d3abab3f9.zip
Directory                       : .
File Size                       : 59 kB
File Modification Date/Time     : 2025:11:19 11:09:02-05:00
File Access Date/Time           : 2026:06:19 13:39:50-04:00
File Inode Change Date/Time     : 2026:06:19 13:39:50-04:00
File Permissions                : -rw-rw-r--
File Type                       : ZIP
File Type Extension             : zip
MIME Type                       : application/zip
Zip Required Version            : 20
Zip Bit Flag                    : 0
Zip Compression                 : None
Zip Modify Date                 : 1980:00:00 00:00:00
Zip CRC                         : 0xc73a69a0
Zip Compressed Size             : 59325
Zip Uncompressed Size           : 59325
Zip File Name                   : document.pdf
```

```
 echo e62126d9156e192e51cf7cc410ce747fff51e034bf65c65bdff7118e7a72e2100c7ca23684a2a2df7407a2ce11d5648045ad673b97726514e8cbf91d3abab3f9 | base64 -d
{��ۧ}מ��ݞ�W��8�G���}�u{M�m��s�[u���_���{mt���km����kg_��;kg�Wy��4㖝��������x{�]ݦ�ow�                                                                                                                                                           
$ hashid e62126d9156e192e51cf7cc410ce747fff51e034bf65c65bdff7118e7a72e2100c7ca23684a2a2df7407a2ce11d5648045ad673b97726514e8cbf91d3abab3f9
Analyzing 'e62126d9156e192e51cf7cc410ce747fff51e034bf65c65bdff7118e7a72e2100c7ca23684a2a2df7407a2ce11d5648045ad673b97726514e8cbf91d3abab3f9'
[+] SHA-512 
[+] Whirlpool 
[+] Salsa10 
[+] Salsa20 
[+] SHA3-512 
[+] Skein-512 
[+] Skein-1024(512) 

```

```
$ binwalk document.pdf

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PDF document, version: "1.4"
17546         0x448A          Zlib compressed data, default compression


$ binwalk -e document.pdf

$ python3 -c "
import zlib

with open('448A', 'rb') as f:
    data = f.read()

for offset in range(0, 16):
    for wbits in [15, -15, 47]:  # zlib, raw deflate, gzip
        try:
            decompressed = zlib.decompress(data[offset:], wbits)
            print(f'Success! offset={offset}, wbits={wbits}, size={len(decompressed)}')
            with open('output', 'wb') as f:
                f.write(decompressed)
            exit()
        except zlib.error:
            pass

print('All attempts failed')
"
Success! offset=5, wbits=-15, size=3
# Bytes too small, so have to start over

ls -la _document.pdf.extracted/

# Extract every zlib stream by brute force
python3 -c "
import zlib

with open('document.pdf', 'rb') as f:
    data = f.read()

found = 0
for i in range(len(data) - 2):
    # Look for zlib magic bytes
    if data[i] == 0x78 and data[i+1] in (0x01, 0x9C, 0xDA, 0x5E):
        try:
            out = zlib.decompress(data[i:])
            if len(out) > 10:  # skip tiny fragments
                fname = f'stream_{i:06x}.bin'
                with open(fname, 'wb') as f2:
                    f2.write(out)
                print(f'[+] Offset {hex(i)}: {len(out)} bytes -> {fname}')
                found += 1
        except:
            pass

print(f'Total streams found: {found}')
"
total 64
drwxrwxr-x  2 kali kali  4096 Jun 19 14:03 .
drwx------ 22 kali kali  4096 Jun 19 14:02 ..
-rw-rw-r--  1 kali kali  6796 Jun 19 13:59 448A
-rw-rw-r--  1 kali kali 41779 Jun 19 13:59 448A.zlib
-rw-rw-r--  1 kali kali     3 Jun 19 14:03 output
[+] Offset 0x448a: 6796 bytes -> stream_00448a.bin
Total streams found: 1

                                        
```
Part6{M.aT!}desc


