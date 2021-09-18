#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
	if (argc != 2)
	{
		printf("misssing command-line argument\n");
		return 1;
	}

	printf("hello, %s\n", argv[1]);
	return 0;
}