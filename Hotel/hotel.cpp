#include<iostream>
#include<fstream>

using namespace std;

int main() {

	ifstream inStream("input.txt");
	int numCases;
	int h, w, n;

	int floor;
	int count;

	inStream >> numCases;

	for (int i = 0; i < numCases; i++) {

		inStream >> h;
		inStream >> w;
		inStream >> n;

		count = n / h+1;
		floor = n%h;

		if (floor == 0) {
			floor = h;
			count = count - 1;
		}

		floor = floor * 100;

		cout << floor +count << endl;
	}

	getchar();
	inStream.close();
	return 0;
}