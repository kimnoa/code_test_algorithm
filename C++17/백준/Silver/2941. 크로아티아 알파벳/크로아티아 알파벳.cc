#include <iostream>
#include <string.h>
#include <string>
#define MAXINT 10000000

using namespace std;

int main(void) {

    char c[60];
    char d[3];
    //char* C = new char[101];
    //char* D = new char[100];
    int* arr = new int[26];
    string S, Q;
    int A = 0, B=0, m=0, n=0, o=0, p=0;
    //double F = 0.0f, F2 = 0.0f, sum = 0.0f;
    memset(arr, 0, 26*sizeof(int));
    
    //A: 개수, B= index
    cin >> S;

    int i = 0;
        B = S.find("c=", i); //찾으면 index 반환
        while (B != -1)
        {
            A++;
            B = S.find("c=", (B + 1));
        }

        B = S.find("c-", i); //찾으면 index 반환
        while (B != -1)
        {
            A++;
            B = S.find("c-", (B + 1));
        }

        B = S.find("dz=", i); //찾으면 index 반환
        while (B != -1)
        {
            A++;
            B = S.find("dz=", (B + 1));
        }

        B = S.find("d-", i); //찾으면 index 반환
        while (B != -1)
        {
            A++;
            B = S.find("d-", (B + 1));
        }

        B = S.find("lj", i); //찾으면 index 반환
        while (B != -1)
        {
            A++;
            B = S.find("lj", (B + 1));
        }

        B = S.find("nj", i); //찾으면 index 반환
        while (B != -1)
        {
            A++;
            B = S.find("nj", (B + 1));
        }

        B = S.find("s=", i); //찾으면 index 반환
        while (B != -1)
        {
            A++;
            B = S.find("s=", (B + 1));
        }

        B = S.find("z=", i); //찾으면 index 반환
        while (B != -1)
        {
            A++;
            B = S.find("z=", (B + 1));
        }
    



    //cout.precision(10);
    cout << S.size() - A;
    return 0;
}