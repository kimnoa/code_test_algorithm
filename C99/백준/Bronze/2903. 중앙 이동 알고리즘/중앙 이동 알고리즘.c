#include<stdio.h>

int main(void) {
    int n = 0, i = 0, start = 2;
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        start = start * 2 - 1;
    }
    printf("%d", start * start);
    return 0;
}