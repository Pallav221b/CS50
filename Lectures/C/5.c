#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);

	printf("\n");

	int s[n];

	for(int i = 0; i < n; i++)
	{
		scanf("%d", &s[i]);
	}

	printf("\n");

	for(int i = 0; i < n; i++)
	{
		printf("%d\t", s[i]);
	}
}