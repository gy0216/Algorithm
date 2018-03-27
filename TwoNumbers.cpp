#include<iostream>
#include<algorithm>
#include<math.h>

using namespace std;

#define MIN 100000000;

int main() {
	
	int num;
	int Arr[10001];
	int numCases, left, right, min, k, sum, count;
	cin >> numCases;
	for (int j = 0; j < numCases; j++) {
		cin >> num;
		left = 0;
		right = num - 1;
		min = MIN;
		cin >> k;
		sum = 0;
		count = 0;

		for (int i = 0; i < num; i++) {
			cin >> Arr[i];
		}

		sort(Arr, Arr + num);

		while (left < right) {
			if (k > Arr[right] + Arr[left]) {
				sum = abs(Arr[right] + Arr[left] - k);
				left++;
			}
			else if (k < Arr[right] + Arr[left]) {
				sum = abs(Arr[right] + Arr[left] - k);
				right--;
			}
			else {
				left++, right--;
				sum = 0;
			}

			if (min > sum) {
				min = sum;
				count = 1;
			}
			else if (min == sum) {
				count++;
			}
			
		}

		cout << count << endl;
	}


	return 0;
}