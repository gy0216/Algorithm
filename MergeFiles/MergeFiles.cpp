#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>

//#define max 50;

using namespace std;

int Sum(int i, int j, int k, int P[][50], int M[][50]) {
	if (i == j)
		return 0;

	else
		return Sum(i, k, P[i][k], P, M) + Sum(k + 1, j, P[k + 1][j], P, M) + M[i][k] + M[k + 1][j];
}

int minmult(int n, const int* d) {
	int M[50][50];
	int P[50][50];
	int matrix[50][50];

	for (int i = 1; i <= n; ++i) {
		M[i][i] = d[i];
		P[i][i] = i;
		matrix[i][i] = d[i];
		//cout << M[i][i] << endl;
	}

	//M[1][n] = 0;

	for (int d = 1; d <= n - 1; ++d) {
		for (int i = 1; i <= n - d; ++i) {
			int j = i + d;
			int min = INT_MAX;
			for (int k = i; k <= j - 1; ++k) {

				//cout << i << " " << j << " " << k << endl;
				int sum = Sum(i, j, k, P, matrix);

				//int sum = 0;
				if (sum < min) {
					//cout << "ch" << sum << endl;
					M[i][j] = sum;
					min = sum;
					P[i][j] = k;
					matrix[i][j] = matrix[i][k] + matrix[k + 1][j];
				}
			}
		}
	}
	/*
	for (int i = 1; i <= n; i++) {
		for (int j = i; j <= n; j++) {
			cout << M[i][j] << " " << endl;
		}
	}
	*/
	return M[1][n];
}

int main() {

	ifstream inStream;
	inStream.open("input.txt");
	int numCases;
	inStream >> numCases;
	int count;
	int C[50];
	int result;

	for (int i = 0; i < numCases; i++) {

		inStream >> count;

		for (int j = 1; j <= count; j++) {
			inStream >> C[j];
		}

		result = minmult(count, C);
		//cout << endl;
		cout << result << endl;
		//cout << endl;
	}

	inStream.close();
	getchar();
	return 0;
}