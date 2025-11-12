#include <iostream>

using namespace std;

int main(){
    long num = 0;
    long long ans = 1;
    cin >> num;
    for (int i=1; i<=num; i++) ans*=i;
    cout << ans;
}