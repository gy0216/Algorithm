#include <iostream>
using namespace std;

int main() {

	int numCases;
	int num;
	int T[500][501];
	int Max;
	int result=0;
	cin >> numCases;

	for (int i = 0; i < numCases; i++) {
		for (int j = 0; j <= i; j++) {
			cin >> num;
			T[i][j] = num;
		}
	}

	for (int i = 1; i < numCases; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0)
				T[i][j] += T[i - 1][j];
			else if (j == i)
				T[i][j] += T[i - 1][j - 1];
			else {
				if (T[i - 1][j - 1] > T[i - 1][j])
					Max = T[i-1][j - 1];
				else Max = T[i - 1][j];
				T[i][j] += Max;
			}
		}
	}


	for (int i = 0; i < numCases; i++) {
		if (result < T[numCases-1][i])
			result = T[numCases-1][i];
	}

	cout << result << endl;
	return 0;
}