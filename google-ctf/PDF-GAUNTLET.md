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

