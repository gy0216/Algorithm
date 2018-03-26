#include<iostream>
#include<algorithm>
#include<math.h>

using namespace std;

int main(void) {

	int numCases;
	cin >> numCases;
	int n, m;
	int score[1003];
	int lose[1003];
	double result[1003];

	int ft, st;
	int fp, sp;
	int max, min;

	for (int i = 0; i < numCases; i++) {
		cin >> n >> m;

		for (int j = 1; j <= n; j++) {
			score[j] = 0;
			lose[j] = 0;
			result[j] = 0;
		}

		for (int j = 0; j < m; j++) {
			cin >> ft >> st;
			cin >> fp >> sp;
			score[ft] += fp;
			score[st] += sp;
			lose[ft] += sp;
			lose[st] += fp;
		}


		for (int j = 1; j <= n; j++) {
			if (score[j] == 0 && lose[j] == 0) {
				result[j] = 0;
				continue;
			}

			result[j] = (pow(score[j], 2) / (pow(score[j], 2) + pow(lose[j], 2))) * 1000;
		}

		max = result[1];
		min = result[1];

		for (int j = 2; j <= n; j++) {
			if (max < result[j])
				max = result[j];
			if (min > result[j])
				min = result[j];
		}

		cout << max << endl;
		cout << min << endl;
	}

	return 0;
}