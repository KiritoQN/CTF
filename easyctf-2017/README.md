#   EASYCTF 2017
## (updating)
## Forensic
### scisnerof 70 points
I found weird file! [elif](https://github.com/KiritoQN/CTF/tree/master/easyctf-2017/elif)

```python
print 'scisnerof'[::-1] #forensics
```
file elif -> HxD
```
m = ['hexa', ....]
n = m[::-1]
```
copy hex (n) -> HxD -> png
it's a file [png](https://github.com/KiritoQN/CTF/tree/master/easyctf-2017/file)
Flag is easyctf{r3v3r5ed_4ensics}

### Zooooooom 85 points
[Hekkerman](https://github.com/KiritoQN/CTF/tree/master/easyctf-2017/hekkerman.jpg) is looking awfully spooky. That hekker glare could pierce a firewall. What can he see that you can't?

Use to exiftool:
```bash
exiftool Hekkerman.jpg
```
Have some information:
```
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 905x624
Thumbnail Image                 : (Binary data 25242 bytes, use -b option to extract)
```
Then Thumbnail Image:
```bash
exiftool -thumbnailimage -b Hekkerman.jpg > thumb.jpg
exiftool thumb.jpg #Thumbnail ...
exiftool -thumbnailimage -b thumb.jpg > thumb1.jpg
```
file thumb1.jpg [here](https://github.com/KiritoQN/CTF/tree/master/easyctf-2017/thumb1.jpg)
Flag is easyctf{d33p_zo0m_HeKker_2c1ae5}

### Petty Difference 75 points

Flag is easyctf{th1s_m4y_b3_th3_d1ff3r3nc3_y0u_w3r3_l00k1ng_4}



## Revert Engineering
### Phunky Python I 30 points
The other day we happened upon a dusty old laptop covered in duct tape and surrounded by several papers with notes scrawled all over them. Upon inspection, we found that the laptop contained several python files labeled phunky.
We've determined that each of the files contains a mini reversing challenge. The first task is simple: Find the value of x such that the program prints out easyctf (make sure it's lowercase!).
```python
x = 0 # REDACTED
digs = [3260918797648513985, 3260918797648513981, 3260918797648513999, 3260918797648514005, 3260918797648513983, 3260918797648514000, 3260918797648513986]
out = ""
for letter in reversed(digs):
    out = chr(letter - x) + out
print out
```
Find x:
```python
	#326091879xxxx
for x in range(7648513800,7648513900):
    digs = [7648513985, 7648513981, 7648513999, 7648514005, 7648513983, 7648514000, 7648513986]
    out = ""
    for letter in reversed(digs):
        out = chr(letter - x) + out
    if(out=='easyctf' or out == 'EASYCTF'):
            print x
            print out
            break
```
output: 7648513884 with #326091879xxxxxxxxxxx
Flag is 3260918797648513884

### Useless Python 50 points 
Boredom took over, so I wrote this python file! I didn't want anyone to see it though because it doesn't actually run, so I used the coolest base-16 encoding to keep it secret. [python](https://github.com/KiritoQN/CTF/tree/master/easyctf-2017/UselessPython.txt)

base16 -> print m -> ...
```
chr(102)+chr(108)+chr(97)+chr(103)+chr(32)+chr(61)+chr(32)+chr(39)+chr(101)+chr(97)+chr(115)+chr(121)+chr(99)+chr(116)+chr(102)+chr(123)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110)+chr(95)+chr(51)+chr(120)+chr(51)+chr(99)+chr(95)+chr(101)+chr(120)+chr(101)+chr(99)+chr(95)+chr(51)+chr(120)+chr(101)+chr(99)+chr(95)+chr(101)+chr(120)+chr(51)+chr(99)+chr(125)+chr(39)+chr(10)+chr(112)+chr(114)+chr(105)+chr(105)+chr(110)+chr(116)+chr(32)+chr(102)+chr(108)+chr(97)+chr(103)
```
output: "flag = 'easyctf{python_3x3c_exec_3xec_ex3c}'\npriint flag"
Flag is easyctf{python_3x3c_exec_3xec_ex3c}

## Cryptography
### Flip My Letters 20 points
```
I dropped my alphabet on its head, can you help me reassemble it? easyctf{r_wlmg_vevm_mvvw_zm_zhxrr_gzyov}
```

Have to alphabet
``` python
abcdefghijklmnopqrstuvwxyz
zyxwvutsrqponmlkjihgfedcba
```
Flag is easyctf{i_dont_even_need_an_ascii_table}
### Clear and Concise Commentary on Caesar Cipher 20 points
```
RNFLPGS{LBHTBGVG}
```

Use to ROT13
EASYCTF{YOUGOTIT} use lowercase
Flag is easyctf{yougotit} 

### RSA 1 50 points
```
p: 35266420919404254191518386016025341974633078431265874906340154002614735903544731
q: 33807892218183588857272342283850192867087438095370793339781097004896897315076507
e: 65537
c: 1067712451787400803562379425809071898242825569913660069623893262373330718829976387893558829998677398703394375335812975519575680539304905678909564062892506029513
```

Code python:
```python
import gmpy
p = 35266420919404254191518386016025341974633078431265874906340154002614735903544731
q = 33807892218183588857272342283850192867087438095370793339781097004896897315076507
e = 65537
c = 1067712451787400803562379425809071898242825569913660069623893262373330718829976387893558829998677398703394375335812975519575680539304905678909564062892506029513

n= q*p
phi = (p-1) * (q-1)
d = gmpy.invert(e,phi)
m = hex(pow(c,d,n))[2:]
flag = m.decode('hex')

print flag
```

Flag is easyctf{wh3n_y0u_h4ve_p&q_RSA_iz_ez_bf3a54ef}

### Let Me Be Frank 75 points
```
I was talking to one of my friends but I couldn't quite understand what he was saying. I think it might be important so here it is: Nwh whdjwh qm uepen, T tjb fsmt tixgi jsrsh sigm gs mpzp xwqf iahxpv iw fslkt. pehgpxf{qtextz_glacz_elt_neinrw_qsg_bums_dcp}
```
Vigenere:
We test key [here](http://rumkin.com/tools/cipher/vigenere.php)
I find the key is: pineapple
```
You should be happy, I put some extra words here to make this easier to solve. easyctf{better_thank_the_french_for_this_one}
```
Flag is easyctf{better_thank_the_french_for_this_one}

### RSA 2 80 points
```
n: 100821463735952707218390829733528491278257
e: 65537
c: 12773618100271283204637208433783479711219
```
Factor n [here](http://factordb.com/index.php?query=100821463735952707218390829733528491278257)
```
p = 217035194916753221149
q = 464539697234930678693
```
```python
import gmpy
p = 217035194916753221149
q = 464539697234930678693
e = 65537
c = 12773618100271283204637208433783479711219

n= q*p
phi = (p-1) * (q-1)
d = gmpy.invert(e,phi)
m = hex(pow(c,d,n))[2:]
flag = m.decode('hex')

print flag
```
Flag is flag{l0w_n_921d}

### Decode Me 100 points

Someone I met today told me that they had a perfect encryption method. To prove that there is no such thing, I want you to decrypt this [encrypted flag](https://github.com/KiritoQN/CTF/tree/master/easyctf-2017/DecodeMe.txt) he gave me.

Try to base64 decode
```python
import base64

f = open("DecodeMe.txt","r")
m = f.read()
for i in range(22):
        m = base64.b64decode(m)
        if(m[0:7] == 'easyctf'):
                break
print m
```
Flag is easyctf{what_1s_l0v3_bby_don7_hurt_m3}

### Hash On Hash 100 points

There's a lot of hex strings here. Maybe they're hiding a message? [hexstrings](https://github.com/KiritoQN/CTF/tree/master/easyctf-2017/HashOnHash.txt)

One line is a hash a character, use to [MD5](https://hashkiller.co.uk/md5-decrypter.aspx) decode:
Start line #1119 - #1159
```
e1671797c52e15f763380b45e841ec32 MD5 : e
0cc175b9c0f1b6a831c399e269772661 MD5 : a
03c7c0ace395d80182db07ae2c30f034 MD5 : s
415290769594460e2e485922904f345d MD5 : y
4a8a08f09d37b73795649038408b5f33 MD5 : c
e358efa489f58062f10dd7316b65649e MD5 : t
8fa14cdd754f91cc6554c9e71929cce7 MD5 : f
f95b70fdc3088560732a5ac135644506 MD5 : {
c4ca4238a0b923820dcc509a6f75849b MD5 : 1
b14a7b8059d9c055954c92674ce60032 MD5 : _
2510c39011c5be704182423e3a695e91 MD5 : h
cfcd208495d565ef66e7dff9f98764da MD5 : 0
83878c91171338902e0fe0fb97a8c47a MD5 : p
eccbc87e4b5ce2fe28308fd9f2a7baf3 MD5 : 3
b14a7b8059d9c055954c92674ce60032 MD5 : _
415290769594460e2e485922904f345d MD5 : y
cfcd208495d565ef66e7dff9f98764da MD5 : 0
7b774effe4a349c6dd82ad4f4f21d34c MD5 : u
b14a7b8059d9c055954c92674ce60032 MD5 : _
8277e0910d750195b448797616e091ad MD5 : d
c4ca4238a0b923820dcc509a6f75849b MD5 : 1
8277e0910d750195b448797616e091ad MD5 : d
7b8b965ad4bca0e41ab51de7b31363a1 MD5 : n
8f14e45fceea167a5a36dedd4bea2543 MD5 : 7
b14a7b8059d9c055954c92674ce60032 MD5 : _
8277e0910d750195b448797616e091ad MD5 : d
cfcd208495d565ef66e7dff9f98764da MD5 : 0
b14a7b8059d9c055954c92674ce60032 MD5 : _
8f14e45fceea167a5a36dedd4bea2543 MD5 : 7
2510c39011c5be704182423e3a695e91 MD5 : h
a87ff679a2f3e71d9181a67b7542122c MD5 : 4
8f14e45fceea167a5a36dedd4bea2543 MD5 : 7
b14a7b8059d9c055954c92674ce60032 MD5 : _
92eb5ffee6ae2fec3ad71c777531578f MD5 : b
415290769594460e2e485922904f345d MD5 : y
b14a7b8059d9c055954c92674ce60032 MD5 : _
2510c39011c5be704182423e3a695e91 MD5 : h
a87ff679a2f3e71d9181a67b7542122c MD5 : 4
7b8b965ad4bca0e41ab51de7b31363a1 MD5 : n
8277e0910d750195b448797616e091ad MD5 : d
cbb184dd8e05c9709e5dcaedaa0495cf MD5 : }
```

Flag is easyctf{1_h0p3_y0u_d1dn7_d0_7h47_by_h4nd}
```python
-_- i can't code... so f*cking noob!
``` 
### RSA3 135 points

We came across another [message](https://github.com/KiritoQN/CTF/tree/master/easyctf-2017/RSA3.txt) that follows the same cryptographic schema as those other RSA messages. Take a look and see if you can crack it.

Same RSA 2...
```
p = 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780869
q = 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780871

```
```python
import gmpy

n = int(0x27335d21ca51432fa000ddf9e81f630314a0ef2e35d81a839584c5a7356b94934630ebfc2ef9c55b111e8c373f2db66ca3be0c0818b1d4eda7d53c1bd0067f66a12897099b5e322d85a8da45b72b828813af23)
e = int(0x10001)
c = int(0x9b9c138e0d473b6e6cf44acfa3becb358b91d0ba9bfb37bf11effcebf9e0fe4a86439e8217819c273ea5c1c5acfd70147533aa550aa70f2e07cc98be1a1b0ea36c0738d1c994c50b1bd633e3873fc0cb377e7)

p = 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780869
q = 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780871

phi = (p-1) * (q-1)
d = gmpy.invert(e,phi)
m = hex(pow(c,d,n))[2:]
flag = m.decode('hex')

print flag
```

Flag is easyctf{tw0_v3ry_merrry_tw1n_pr1m35!!_417c0d}

## Web
## Programing
## Exploit

