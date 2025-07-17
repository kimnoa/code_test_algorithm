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
    
    cin >> A;

    for (int i = 0; i < A; i++)
    {
        cin >> c;
        d[0] = c[0];
        arr[0] = c[0];
        B = 1, m=0;

        for (int j = 1; j < strlen(c); j++)
        {
            if (c[j] != d[0]) //다른 문자가 올 때
            {
                for (int k = 0; k < B; k++) //배열을 기준으로 비교
                {
                    if (c[j] == arr[k]) //만약 기존 배열에 있으면 그룹이 아님
                    {
                        m = -1; //판별 값
                        break;
                    }
                }

                if (m != -1) //배열에 없다면 새로운 문자임
                {
                    arr[B++] = c[j]; //배열에 추가
                    d[0] = c[j]; //비교 문자 교체
                }

                else //판별되면 더 비교할 필요 없음 (이미 그룹 아님)
                    break;
            }

        }
        if (m != -1) //끝까지 했을 때 떨어지는 문자 없다면
            n++; //그룹 문자 개수 추가
    }


    //cout.precision(10);
    cout << n;
    return 0;
}