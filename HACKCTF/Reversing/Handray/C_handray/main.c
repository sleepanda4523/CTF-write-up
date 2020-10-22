#include <stdio.h>
#include <stdlib.h>

int main()
{
    char str[35] = "A]`j?NCz?eiHb:R^CkdA.jaP+F+..jb!}";
    int arr[] = {7,4,3,1,4,6,3,1,9,10,11,12,13,14,15,16,1,1,1,2,2,2,3,4,5,2,5,2,2,2,2,2};
    for(int i=0;i<30;i++){
        str[i]=str[i]+arr[i];
    }
    printf("\n%s",str);
    return 0;
}

