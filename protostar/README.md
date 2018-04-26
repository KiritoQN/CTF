# Stack0
```c
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];

  modified = 0;
  gets(buffer);

  if(modified != 0) {
      printf("you have changed the 'modified' variable\n");
  } else {
      printf("Try again?\n");
  }
}
```
gdb-peda$ pdisass main
Dump of assembler code for function main:
   0x080483f4 <+0>:     push   ebp
   0x080483f5 <+1>:     mov    ebp,esp
   0x080483f7 <+3>:     and    esp,0xfffffff0
   0x080483fa <+6>:     sub    esp,0x60
   0x080483fd <+9>:     mov    DWORD PTR [esp+0x5c],0x0 --> modified = 0
   0x08048405 <+17>:    lea    eax,[esp+0x1c]
   0x08048409 <+21>:    mov    DWORD PTR [esp],eax
   0x0804840c <+24>:    call   0x804830c <gets@plt> --> get(buffer)
   0x08048411 <+29>:    mov    eax,DWORD PTR [esp+0x5c] --> pointer
   0x08048415 <+33>:    test   eax,eax
   0x08048417 <+35>:    je     0x8048427 <main+51>
   0x08048419 <+37>:    mov    DWORD PTR [esp],0x8048500
   0x08048420 <+44>:    call   0x804832c <puts@plt>
   0x08048425 <+49>:    jmp    0x8048433 <main+63>
   0x08048427 <+51>:    mov    DWORD PTR [esp],0x8048529
   0x0804842e <+58>:    call   0x804832c <puts@plt>
   0x08048433 <+63>:    leave
   0x08048434 <+64>:    ret
End of assembler dump.
gdb-peda$ b*main+9
Breakpoint 1 at 0x80483fd: file stack0/stack0.c, line 10.
gdb-peda$ b*main+29
Breakpoint 2 at 0x8048411: file stack0/stack0.c, line 13.
gdb-peda$ x/wx $esp+0x5c
0xffffd50c:     0x00000000    --> address var modified 0xffffd50c
gdb-peda$ c
Continuing.
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
gdb-peda$ x/40wx $esp
--> address       0 1 2 3         4 5 6 7         8 9 a b         c d e f
--------------------------------------------------------------------------
0xffffd4b0:     0xffffd4cc      0xffffd554      0xf7fb5000      0x00009f17
0xffffd4c0:     0xffffffff      0x0000002f      0xf7e0fdc8      0x41414141
0xffffd4d0:     0x41414141      0x41414141      0x41414141      0x41414141
0xffffd4e0:     0x41414141      0x41414141      0x41414141      0x08004141
0xffffd4f0:     0xf7fb5000      0xf7fb5000      0x00000000      0xf7e31c0b
0xffffd500:     0xf7fb53dc      0x080481e8      0x0804845b      0x00000000
0xffffd510:     0xf7fb5000      0xf7fb5000      0x00000000      0xf7e1b637
0xffffd520:     0x00000001      0xffffd5b4      0xffffd5bc      0x00000000
0xffffd530:     0x00000000      0x00000000      0xf7fb5000      0xf7ffdc04
0xffffd540:     0xf7ffd000      0x00000000      0xf7fb5000      0xf7fb5000
