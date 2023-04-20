#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Substitution cipher or Caesar’s cipher.

// This program which reads a natural number n and a string s. The string s is encoded using Caesar’s cipher with a displacement of n (either positive or negative).
// The program decodes the message and display it on the screen. Punctuation marks and numbers are left as they are.

int main(int argc, char* argv[]) {

	int step, nr;
	char message[256], current;
	scanf("%d\n", &step);
	step %= 26;
	fgets(message, 256, stdin);
	for (int i = 0;i < strlen(message);i++)
	{
		current = message[i];
		nr = (int)(current);
		if (nr >= 65 && nr <= 90)
		{
			nr += step;
			if (nr < 65) nr += 26;
			else
				if (nr > 90)
					nr -= 26;
		}
		else
			if (nr >= 97 && nr <= 122)
			{
				nr += step;
				if (nr < 97) nr += 26;
				else
					if (nr > 122)
						nr -= 26;
			}
		current = (char)(nr);
		printf("%c", current);
	}
	return 0;
}
