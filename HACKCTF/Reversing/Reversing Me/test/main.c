#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *serial = "H`cjCUFzhdy^stcbers^D1_x0t_jn1w^r2vdrre^3o9hndes1o9>}";
    char enter[54];
    for(int i=0;i<strlen(serial);i++){
        enter[i] = serial[i] ^ (i%2);
    }
    printf("%s",enter);
    return 0;
}
