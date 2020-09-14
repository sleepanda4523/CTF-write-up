## 풀이    
이 문제도 앞 문제와 비숫하게 접근하면 되는데,    
일단 IDA로 까보면    
![IDAVIEW](/HACKCTF/Pwnable/Basic_BOF_2/IDAview.PNG)   
일단 s는 ebp-8C, v5는 ebp-C에 위치해 있다.   
그럼 코드로 보자.   
![pseudocode](/HACKCTF/Pwnable/Basic_BOF_2/pseudocode.PNG)   
이번에는 v5가 int형이 아니라 함수 포인터이다.   
그리고 sup라는 함수를 포인팅 하고 있는데,   
sup함수는 
![sup](/HACKCTF/Pwnable/Basic_BOF_2/sup.PNG)  
그냥 s를 출력해주는 함수이다.   
>  이때 문제를 한번 실행해보면 알겠지만 s는 main내 s가 아니라 정적변수인 s다.  
>  아마 nc에 접속해보면 뭔 하아아아아아아아아앙 이라고 뜰거다.    

그리고 자세히 살펴보니 shell이라는 대놓고 쉘이라는 함수가 있다.   
![shell](/HACKCTF/Pwnable/Basic_BOF_2/shell.PNG)  
그렇다면 이것도 BOF를 일으켜 v5에 담겨있는 sup의 함수 주소를 shell의 주소로 바꿔버리면 된다!   
일단 shell의 주소를 확인해보면    
![addr](/HACKCTF/Pwnable/Basic_BOF_2/addr.PNG)   
0x0804849B이다.    
자 그럼 s에서 부터 v5까지 거리를 구해보자. 이번에도 그림을 그려보았다.    
![mem](/HACKCTF/Pwnable/Basic_BOF_2/mem.PNG)  
s의 위치가 0x8C고, v5는 0x0C이니까   
0x8C - 0x0C = 0x80 = 128byte만큼 떨어져 있음을 알 수 있다.   
fgets함수를 보면 최대 133byte까지 입력 받을 수 있으니    
128byte만큼 아무값이나 (용어를 쓰자면 더미값이라고 한다.)넣고,   
그 뒤에 shell함수의 주소를 넣으면 끝!    
열심히 풀어보자!