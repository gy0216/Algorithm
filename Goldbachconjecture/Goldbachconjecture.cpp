#include <iostream>
#include <fstream>

using namespace std;

int main() {

	int numCases;
	int num;
	int half1;
	int j;

	ifstream inStream;
	inStream.open("input.txt");

	inStream >> numCases;

	for (int i = 0; i < numCases; i++) {
		inStream >> num;

		half1 = num / 2;

		while (half1>2) {
			while (half1 > 2) {
				j = 2;
				while (j < half1) {
					if (half1 % j == 0) break;

					j++;
				}

				if (half1 == j) {
					break;
				}
				half1--;
			}
			j = 2;
			while (j < num - half1) {
				if ((num - half1)%j == 0) {
					break;
				}

				j++;
			}
			if (num - half1 == j) break;

			half1--;
		}

		cout << half1 << " " << num - half1 << endl;
	}
	getchar();
	inStream.close();
	return 0;
}