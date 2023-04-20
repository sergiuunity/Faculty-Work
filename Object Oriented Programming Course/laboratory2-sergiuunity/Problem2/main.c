#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Write a program that takes a single command line argument: 
// the path to a file.This file is actually a dictionary that contains, on each line, a word from the given language.
// You can consider that the maximum size of a word is 50 characters.
// Display the frequency table of the letters from this file, and then the word with the maximum number of letters, the word with the maximum number of vowels and the word with the maximum number of consonants

void frequency_table(char **all_words, int total_words) {
	int frequency[26], total = 0;
	for (int i = 0; i < 26; i++)
	{
		frequency[i] = 0;
	}
	for (int i = 0; i < total_words; i++)
		for (int j = 0; j < strlen(all_words[i]); j++)
		{
			frequency[(char)((int)((all_words[i])[j]) - 97)]++;
		}
	for (int i = 0; i < 26; i++)
	{
		total += frequency[i];
	}
	if (total != 0) {
		for (int i = 0; i < 26; i++)
		{
			float percentage = ((float)frequency[i] / total) * 100;
			printf("%c  %.2f%c\n", (char)(97 + i), percentage, '%');
		}
	}
}

int main(int argc, char* argv[]) {
	FILE* dictionary;
	fopen_s(&dictionary, argv[1], "r");
	int number_of_words = 100;
	int i = 0;
	char** words;
	char line[100];
	words = malloc(100 * sizeof(char) * number_of_words);
	if (dictionary != NULL)
	{
		while (fgets(line, 100, dictionary)) {
			words[i] = malloc(100 * sizeof(char));
			line[strlen(line) - 1] = '\0';
			strcpy(words[i], line);	
			i++;
			if (i == number_of_words - 1) {
				number_of_words *= 2;
				words = realloc(words, 100 * sizeof(char) * number_of_words);
			}
		}
	}
	//for (int j = 0; j < i; j++) {
	//	printf("%s\n", words[j]);
	//}
	frequency_table(words, i);
	free(words);
	return 0;
}