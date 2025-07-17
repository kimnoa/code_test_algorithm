#include <iostream>
#include <string.h>
#include <string>
#define MAXINT 10000000

using namespace std;

int main(void) {

    char c[60];
    char d[5];
    //char* C = new char[101];
    //char* D = new char[100];
    int* arr = new int[26];
    string S, Q;
    int A = 0, B=0, m=0, n=0, o=0, p=0;
    double F = 0.0f, F2 = 0.0f, sum = 0.0f;
    memset(arr, 0, 26*sizeof(int));
    
    for (int i = 0; i<20; i++)
    {
        cin >> c >> F >> S;

        if (S == "A+") sum += 4.5 * F;
        else if (S == "A0") sum += 4.0 * F;
        else if (S == "B+") sum += 3.5 * F;
        else if (S == "B0") sum += 3.0 * F;
        else if (S == "C+") sum += 2.5 * F;
        else if (S == "C0") sum += 2.0 * F;
        else if (S == "D+") sum += 1.5 * F;
        else if (S == "D0") sum += 1.0 * F;
        else if (S == "F") sum += 0.0 * F;

        if (S != "P") F2 += F;
    }
    cout.precision(10);
    cout << sum / F2;
    return 0;
}