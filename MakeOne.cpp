#include<iostream>
#include<algorithm>

using namespace std;

int main() {
	int num;
	cin >> num;
	int dp[10000];
	dp[1] = 0;
	int max1, max2, max3;
	int Max;
	
	for (int i = 2; i <= num; i++) {
		max1 = dp[i - 1] + 1;
		
		if (i % 3 == 0) {
			max3 = dp[i / 3] + 1;
		}
		else{
			max3 = 1000000;
		}

		if (i % 2 == 0) {
			max2 = dp[i / 2] + 1;
		}
		else {
			max2 = 1000000;
		}
		Max = min(max1, max2);
		dp[i] = min(Max, max3);
		cout <<i<<" "<< dp[i] << endl;
	}

	cout << dp[num] << endl;
	
	return 0;
}