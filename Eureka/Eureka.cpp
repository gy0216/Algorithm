#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

//주어진 수에서 만들 수 있는 가장 큰 삼각형을 구하는 함수
int maxTra1(double n) {
	int max = 0;

	//cout << "tra1" << n << endl;

	while ((pow(max, 2) + max) / 2 < n) {
		max++;
	}
	//cout << "max" << max << endl;
	return max - 1;
}

int lastTra(double n) {
	int result = 0;
	int max = 1;

	while ((pow(max, 2) + max) / 2 < n) {
		max++;
	}

	if ((pow(max, 2) + max) / 2 == n) result = 1;

	return result;
}

int main() {
	ifstream inStream("input.txt");
	int numCases;
	double num;
	double n1;
	double n2;
	double result;

	double max1;
	double max2;
	double max3;

	inStream >> numCases;

	for (int i = 0; i < numCases; i++) {
		result = 0;
		inStream >> num;
		n1 = num;

		max1 = 1;

		while ((pow(max1, 2) + max1) / 2 < n1) {
			max1++;
		}
		
		max1 = max1 - 1;
		
		while (max1 > 0) {
			n1 = num - (pow(max1, 2) + max1) / 2;

			//cout << "1n" << n << endl;
			max1--;
			
			if (n1 == 1) continue;

			max2 = 1;

			while ((pow(max2, 2) + max2) / 2 < n1) max2++;

			max2 = max2 - 1;

			//cout << "max1" <<max1<< endl;
			

			while (max2 > 0) {
				
				n2 = n1 - (pow(max2, 2) + max2) / 2;

			//	cout << "n" << n << endl;
				max2--;

				max3 = 1;

				while ((pow(max3, 2) + max3) / 2 < n2) max3++;

				//cout << "max2" << max2 << endl;
				//cout << "max3" << max3 << endl;
				
				if ((pow(max3, 2) + max3) / 2 == n2) {
					result = 1;
					//cout << "case" << endl;
				//	cout << "n" << n << endl;
				//	cout << "p" << (pow(max3, 2) + max3) / 2 << endl;
					break;
				}
			}	

			if (result == 1) break;
		}

		cout << result << endl;
	}
	getchar();
	inStream.close();
	return 0;
}