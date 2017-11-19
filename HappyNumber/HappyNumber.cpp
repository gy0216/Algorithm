#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int Is_Happy(int num) {
	double n=num;
	int arr[10];
	int flag = 0;
	int devide;
	int count=0;

	while (n!=1) {
		count++;
		int i = 0;
		devide = n;
		n = 0;

		while (true) {
			arr[i] = devide % 10;
			devide = devide / 10;
			if (devide < 10) {
				arr[++i] = devide;
				break;
			}
			i++;
		}
		
		for (int j = 0; j <= i; j++) {
			n += pow(arr[j], 2);
		}

		if (count > 1000) {
			flag = 1;
			break;
		}
		
	}
	return flag;
}

int main() {
	ifstream inStream("input.txt");
	int numCases;
	int num;

	inStream >> numCases;
	int result; 

	for (int i = 0; i < numCases; i++) {
		inStream >> num;
		result = Is_Happy(num);

		if (result == 1) cout << "UNHAPPY" << endl;
		else if (result == 0) cout << "HAPPY" << endl;
	}
	inStream.close();
	return 0;
}