#include<iostream>
#include<fstream>
using namespace std;

int main() {
	ifstream inStream("input.txt");
	int numCases;
	int num[1000];
	inStream >> numCases;
	int Sum;
	int Max;

	for (int i = 0; i < numCases; i++) {
		inStream >> num[i];
	}
	Sum = num[0];
	Max = num[0];

	if (Sum < 0)
		Sum = 0;

	for (int i = 1; i < numCases; i++) {
		Sum += num[i];
		if (Max < Sum)
			Max = Sum;
		if (Sum < 0)
			Sum = 0;
	}

	cout << Max << endl;

	inStream.close();
	getchar();
	return 0;
}