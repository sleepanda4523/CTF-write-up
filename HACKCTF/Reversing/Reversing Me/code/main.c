#include <stdio.h>
#include <string.h>

int main() {
	int i;
	char *serial = "H`cjCUFzhdy^stcbers^D1_x0t_jn1w^r2vdrre^3o9hndes1o9>}";
	char enter[54];
	printf("Ű�� �Է��Ͻð� : ");
	scanf("%s", enter);
	if (strlen(enter) == strlen(serial)) {
		for (i = 0; i < strlen(serial) && (enter[i] ^ (i % 2)) == serial[i]; i++);
		if (i - 1 == strlen(enter))
			printf("�����ϼ�!\n");
	}
	else
		printf("�װ� �ƴҼ�...\n");
		exit(0);

}
