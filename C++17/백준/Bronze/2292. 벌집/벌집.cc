#include <iostream>

using namespace std;

int main(void){

    int n = 0, ans = 1, bound = 0;

    cin >> n;

	while (n > (6 * bound + 1)){
		bound += ans++;
	}

	cout << ans;

	return 0;
}