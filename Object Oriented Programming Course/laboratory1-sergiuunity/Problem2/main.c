#include <stdio.h>
#include <stdlib.h>

// Alice forgot her card’s PIN code.She remembers that her PIN code had 4 digits, all the digits were distinctand in decreasing order, and that the sum of these digits was 24. 
// This C program that prints, on different lines, all the PIN codes which fulfill these constraints. 

int main(int argc, char* argv[]) {
    int m_s = 24;
    short c1, c2, c3, c4;
    for (c1 = 9;c1 >= 3;c1 = c1 - 1) {
        for (c2 = c1 - 1;c2 >= 2;c2 = c2 - 1) {
            for (c3 = c2 - 1;c3 >= 1;c3 = c3 - 1) {
                c4 = m_s - (c1 + c2 + c3);
                if (c4 < c3 && c4 >= 0)
                {
                    printf("%d%d%d%d", c1, c2, c3, c4);
                    printf("\n");
                }
            }
        }
    }
    return 0;
}   
