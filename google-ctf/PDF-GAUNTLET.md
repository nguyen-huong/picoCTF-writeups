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

# Another part

extract fonts and all imgs w/ mutool 
```
mutool document.pdf
ing: ICC support is not available
format error: xref stream missing Size entry (1337 0 R)
warning: trying to repair broken xref
warning: repairing PDF document
extracting image-0028.png
extracting font-0037.ttf
                                                                                                                                                                                                                                                                                           

└─$ strings image-0028.png 
IHDR
        pHYs
OIDATx
l>-/
1u+R
2gXY>
IEND
                                                                                                                                                           

└─$ binwalk image-0028.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 32 x 100, 8-bit grayscale, non-interlaced
62            0x3E            Zlib compressed data, default compression


file _image-0028.png.extracted/3E
xxd _image-0028.png.extracted/3E | head -20
strings _image-0028.png.extracted/3E
_image-0028.png.extracted/3E: data
00000000: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000010: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000020: 0000 0000 0000 0000 0000 0000 0000 0072  ...............r
00000030: 7373 7373 7200 0000 0000 0000 0000 0000  ssssr...........
00000040: 0000 0000 0000 0000 0000 0000 53a6 c6da  ............S...
00000050: dcde dede dedc dbc6 943b 0000 0000 0000  .........;......
00000060: 0000 0000 0000 0000 0000 0053 aed9 dde0  ...........S....
00000070: e1e2 e2e2 e2e2 e2e1 e0dd d9a6 3b00 0000  ............;...
00000080: 0000 0000 0000 0000 0000 0094 d8dc e0e2  ................
00000090: e3e3 e4e4 e4e4 e4e4 e3e3 e2e0 dcd2 7f00  ................
000000a0: 0000 0000 0000 0000 0000 00ad d8de e1e3  ................
000000b0: e3e4 e5e5 e6e6 e6e6 e5e5 e4e4 e3e2 ded8  ................
000000c0: 8a00 0000 0000 0000 0000 00ad d8de e2e3  ................
000000d0: e4e5 e6e7 e7e7 e8e8 e7e7 e7e6 e5e4 e3e2  ................
000000e0: dfd8 8a00 0000 0000 0000 007f d7de e2e3  ................
000000f0: c4a3 e7e7 e8e9 e9e9 e9e9 e9e8 e7e7 c58b  ................
00000100: b7e2 ded6 5f00 0000 0000 003b d1dc e1d4  ...._......;....
00000110: 9377 94e8 e9ea eaeb ebeb ebeb eae9 e8d7  .w..............
00000120: 9477 93dc dcb7 0000 0000 0000 9dd8 dfd4  .w..............
00000130: 8177 bae8 e9ea ebec ecec ecec eceb ebe9  .w..............
rssssr
wwwww
wwwww
wwwwwwwwwwwwwwww
wwwww~
wwwwww

                                                                                                                                                           
```
check the fonts
```
┌──(kali㉿kali)-[~]
└─$ python3 -c "from fontTools.ttLib import TTFont; font = TTFont('font-0037.ttf'); print(font.keys())"
['GlyphOrder', 'head', 'hhea', 'maxp', 'hmtx', 'fpgm', 'prep', 'cvt ', 'loca', 'glyf', 'gasp']
                                                                                                                                                           
┌──(kali㉿kali)-[~]
└─$ python3 -c "
from fontTools.ttLib import TTFont
font = TTFont('font-0037.ttf')

# Dump fpgm and prep as raw bytes
for tag in ['fpgm', 'prep', 'cvt ']:
    try:
        data = font.reader[tag]
        print(f'=== {tag} ({len(data)} bytes) ===')
        # Try to find printable strings
        import re
        strings = re.findall(b'[ -~]{4,}', data)
        for s in strings:
            print(s.decode())
        print()
    except Exception as e:
        print(f'{tag}: {e}')
"

# Also dump ALL glyph names
python3 -c "
from fontTools.ttLib import TTFont
font = TTFont('font-0037.ttf')
glyphs = font.getGlyphOrder()
print('Glyph count:', len(glyphs))
for g in glyphs:
    if g not in ['.notdef', 'nonmarkingreturn'] and not g.startswith('glyph'):
        print(g)
"

# Raw strings from the font file directly
strings font-0037.ttf | grep -E 'Part|flag|\{|\}'
=== fpgm (3596 bytes) ===
UXEY  K
(Y`f 
cc#b
C`B-
 `f-
,#!#!-
C ``B
CTx 
CCad
C`B#
PXeY
C`B-
CX#!#!
PXeY
CEcE
%YR[X!#!
PPX!
8PX!
8YY 
CEcEad
(PX!
CEcE 
0PX!
PX f 
 PX!
6PX!
`YYY
bYYdaY
+YY#
PXeYY d
C#BY-
, E 
%ad 
,#!#!
&QX`P
aRYX#Y!Y 
PXeY-
C`B-
#B# 
,  E 
@`Yf
CEB*!
C`B-
C`B-
,  E 
%` E
#a d 
 PX!
@YY#
PXeY
%#aDD
,  E 
%` E
#a d
PXeY
%#aDD
EPX!
#!Y*!-
daD-
#BY-
#B#-
,KTX
dDY$
e#x-
,KQXKSX
e#x-
@`Yf
@`Yf
C`B-
#B E
`B `
+,# 
`KTX# .
!!Y-
,,# 
`KTX# .
!!Y-
-,# 
&`KTX# .
!!Y-
#B E
`B `
., <
/, `
` C#
.*!-
1,  G  
@`Yf
c`#a8# 
UX G  
@`Yf
c`#a8
EX0Y
EX0Y
4, 5
@`Yf
@`Yf
D>#8
6, < G 
@`Yf
Ca8-
8, < G 
@`Yf
Cc8-
% . G
G#G#a Xb
%G#G#a
.#  <
% .G#G#a 
`PX 
YBB# 
#G#G#a#F`
@`Yf
C`d#
CadPX
@`Yf
ca#  
&#Fa8
CG#G#a` 
@`Yf
c`# 
@`Yf
%`d#
%`dPX!
#!Y#  
&#Fa8Y-
#B   
& .G#G#a#<8-
#B   F#G
+#a8-
%G#G#a
TX. <#!
%G#G#a 
%G#G#a
cc# Xb
@`Yf
c`#.#  <
8#!Y-
C .G#G#a `
@`Yf
c#  <
@,# .F
RYX <Y.
A,# .F
PYX <Y.
B,# .F
RYX <Y# .F
PYX <Y.
:+# .F
RYX <Y.
8# .F
RYX <Y.
&   F#Ga
#B.G#G#a
C+# < .#8
% .G#G#a 
`PX 
YBB# G
@`Yf
C`d#
CadPX
@`Yf
%Fa8# <#8
!  F#G
+#a8!Y
;+!#  <
#B#8
E# . F
EX#!
!YYB+
EX0Y-

=== prep (214 bytes) ===
NA1!
DYYYYY@

=== cvt  (176 bytes) ===

Glyph count: 12
r:p6}
```

the r:p6} looks like a flag, see what glyph is correlated to that, but then nothing

strings and search for part, saw 
Part1{5 characters} with ) Tj

that means pdftodrawing might work

# part 5
```
qpdf --qdf --object-streams=disable document.pdf unpacked.pdf
```

<img width="1854" height="1324" alt="image" src="https://github.com/user-attachments/assets/c0b21c02-b937-4691-af91-ee74f57ea63f" />
Part5{-f'05}


# other zsteg 
```

└─$ pngcheck image-0028.png    
OK: image-0028.png (32x100, 8-bit grayscale, non-interlaced, static, 79.1%).
                                                                                                                                                           

└─$ zsteg -a image-0028.png                           
imagedata           .. text: ["w" repeated 16 times]
chunk:0:IHDR        .. file: Adobe Photoshop Color swatch, version 0, 32 colors; 1st RGB space (0), w 0x64, x 0x800, y 0, z 0; 2nd RGB space (0), w 0, x 0, y 0, z 0                                                                                                                                                  
b3p,rgb,lsb,xy      .. text: "%JJJJJJ%"
b3p,rgb,msb,xy      .. text: "[[R\t[[[[\t"
b4,rgb,lsb,xy       .. text: "\"333333\" "
b4,rgb,msb,xy       .. text: "fffU53wwwwww3"
b5p,r,lsb,xy        .. text: "#?AIIH?+"
b5p,rgb,lsb,xy      .. text: "$--6666--$$"
b5p,rgb,msb,xy      .. text: "llK'oooo'"
b6p,rgb,lsb,xy      .. text: "jpzzzzpo"
b8,r,msb,xy         .. text: "ec[;{{{{;"
b8,rgb,lsb,xy       .. text: "rrrssssssssssssrrr"
b8,rgb,msb,xy       .. text: "eeeccc[[[;;;{{{{{{{{{{{{;;;"
b4,rgb,lsb,xy,prime .. text: "33336f3="
b5,r,lsb,xy,prime   .. file: GTA audio index data (SDT)
b8,rgb,msb,xy,prime .. text: "777GGGuuu"
b6p,rgb,lsb,yx      .. text: "u*`eopJ:"
b1,r,msb,yx,prime   .. file: Atari DEGAS Elite compressed bitmap 320 x 200 x 16, color palette 0020 0000 00c0 0080 0000 ...
b2,r,lsb,yx,prime   .. file: GLS_BINARY_MSB_FIRST
b4,r,lsb,yx,prime   .. file: Adobe Photoshop Color swatch, version 0, 175 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (1280), w 0, x 0, y 0, z 0x80                                                                                                                                                      
b4,r,msb,yx,prime   .. file: Adobe Photoshop Color swatch, version 0, 245 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (40960), w 0, x 0, y 0, z 0x1                                                                                                                                                      
b5p,r,lsb,yx,prime  .. file: Adobe Photoshop Color swatch, version 0, 87 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (1280), w 0, x 0, y 0, z 0xc0                                                                                                                                                       
b5p,r,msb,yx,prime  .. file: Adobe Photoshop Color swatch, version 0, 234 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (40960), w 0, x 0, y 0, z 0x3                                                                                                                                                      
b6p,r,lsb,yx,prime  .. file: Adobe Photoshop Color swatch, version 0, 171 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (256), w 0, x 0, y 0, z 0x60                                                                                                                                                       
b6p,r,msb,yx,prime  .. file: Adobe Photoshop Color swatch, version 0, 213 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (32768), w 0, x 0, y 0, z 0x6                                                                                                                                                      
b7p,r,lsb,yx,prime  .. file: Adobe Photoshop Color swatch, version 0, 213 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (256), w 0, x 0, y 0, z 0xb0                                                                                                                                                       
b7p,r,msb,yx,prime  .. file: Adobe Photoshop Color swatch, version 0, 171 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (32768), w 0, x 0, y 0, z 0xd                                                                                                                                                      
b1,rgb,lsb,YX,prime .. file: SIMH tape data
b2,r,msb,YX,prime   .. file: Windows boot log, header size 0x400, 0x1100000 valid bytes; entry size 0, 0 seconds, severity 0, version 0, event 0; entry size 0, 0 seconds, severity 0, version 0, event 0                                                                                                             
b8,rgb,msb,YX,prime .. text: "VVV;;;sss"
b3p,rgb,lsb,Xy      .. text: "%JJJJJJ%"
b3p,rgb,msb,Xy      .. text: "\t[[[[\tR[["
b4,r,lsb,Xy         .. text: "#DUffUC1"
b4,r,msb,Xy         .. text: "z:3233(3"
b4,rgb,lsb,Xy       .. text: "\"333333\" "
b4,rgb,msb,Xy       .. text: "=3wwwwww3SUfff"
b5,r,lsb,Xy         .. text: "xWYNt%)JR"
b5p,r,lsb,Xy        .. text: "8K\\ddcQB"
b5p,r,msb,Xy        .. text: "u5&$&&0&"
b5p,rgb,lsb,Xy      .. text: "$$--6666--$"
b5p,rgb,msb,Xy      .. text: "'oooo'Kll"
b6p,rgb,lsb,Xy      .. text: "opzzzzpj"
b8,r,msb,Xy         .. text: ";{{{{;[ce"
b8,rgb,lsb,Xy       .. text: "rrrssssssssssssrrr"
b8,rgb,msb,Xy       .. text: ";;;{{{{{{{{{{{{;;;[[[ccce"
b4,rgb,lsb,Xy,prime .. text: "DB\"37wwx"
b5,r,lsb,Xy,prime   .. file: GTA audio index data (SDT)
b8,rgb,msb,Xy,prime .. text: "777GGGSSS"
b1,r,msb,yX,prime   .. file: Atari DEGAS Elite compressed bitmap 320 x 200 x 16, color palette 0020 0000 00c0 0000 0000 ...
b2,r,lsb,yX,prime   .. file: GLS_BINARY_MSB_FIRST
b4,r,lsb,yX,prime   .. file: Adobe Photoshop Color swatch, version 0, 175 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (3328), w 0, x 0, y 0, z 0x20                                                                                                                                                      
b4,r,msb,yX,prime   .. file: Adobe Photoshop Color swatch, version 0, 245 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (45056), w 0, x 0, y 0, z 0x4                                                                                                                                                      
b5p,r,lsb,yX,prime  .. file: Adobe Photoshop Color swatch, version 0, 87 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (1280), w 0, x 0, y 0, z 0x90                                                                                                                                                       
b5p,r,msb,yX,prime  .. file: Adobe Photoshop Color swatch, version 0, 234 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (40960), w 0, x 0, y 0, z 0x9                                                                                                                                                      
b6p,r,lsb,yX,prime  .. file: Adobe Photoshop Color swatch, version 0, 171 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (256), w 0, x 0, y 0, z 0x48                                                                                                                                                       
b6p,r,msb,yX,prime  .. file: Adobe Photoshop Color swatch, version 0, 213 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (32768), w 0, x 0, y 0, z 0x12                                                                                                                                                     
b7p,r,lsb,yX,prime  .. file: Adobe Photoshop Color swatch, version 0, 213 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (256), w 0, x 0, y 0, z 0xa4                                                                                                                                                       
b7p,r,msb,yX,prime  .. file: Adobe Photoshop Color swatch, version 0, 171 colors; 1st RGB space (0), w 0, x 0, y 0, z 0; 2nd space (32768), w 0, x 0, y 0, z 0x25                                                                                                                                                     
b2,r,msb,Yx,prime   .. file: Windows boot log, header size 0x400, 0x1300000 valid bytes; entry size 0, 0 seconds, severity 0, version 0, event 0; entry size 0, 0 seconds, severity 0, version 0, event 0          
```
