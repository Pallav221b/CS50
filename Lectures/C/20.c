#include <stdio.h>

int main(void)
{
	char s[5];
	printf("s: ");
	gets(s);
	printf("s: %s\n", s);
}