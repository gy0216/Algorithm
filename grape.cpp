#include<iostream>
#include<algorithm>
#include<fstream>

using namespace std;

int main() {
	fstream inStream("input.txt");
	int num;
	int result;
	int n[100];
	int dp[100];
	int max1, max2, max3;
	int Max;

	inStream >> num;
	for (int i = 0; i < num; i++) {
		inStream >> n[i];
	}

	dp[0] = n[0];
	if(num==2)
		dp[1] = n[1]+n[0];
	else if (num > 2) {
		dp[1] = n[1] + n[0];

		max1 = n[0] + n[1];
		max2 = n[1] + n[2];
		max3 = n[0] + n[2];

		Max = max(max1, max2);
		dp[2] = max(Max, max3);
		cout << dp[2] << endl;
	}

	for (int i = 3; i < num; i++) {
		max1 = n[i] + dp[i - 2];
		max2 = n[i] + n[i - 1] + dp[i - 3];
		max3 = dp[i - 1];
		Max = max(max1, max2);
		dp[i] = max(Max, max3);
		cout << dp[i] << endl;
	}

	result = dp[num - 1];

	cout << result << endl;
	getchar();
	return 0;
}