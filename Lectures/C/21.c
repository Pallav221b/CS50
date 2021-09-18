#include <stdio.h>

int main(void)
{
	FILE *file = fopen("Phonebook.txt", "a");

	char name[50];
	printf("Name: ");
	gets(name);
	char number[50];
	printf("Number: ");
	gets(number);

	fprintf(file, "%s, %s\n", name, number);

	fclose(file);
}