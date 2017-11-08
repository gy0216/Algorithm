#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void) {
	
	ifstream inStream("input.txt");

	if (!inStream) {
		cout << "Error. No file" << endl;
		exit(1);
	}

	int numCases;
	int N;
	int arr[20];
	int num;
	int answer;

	inStream >> numCases;

	for (int i = 0; i < numCases; i++) {
		inStream >> N;
		num = N;

		//2진수부터 64진수까지 모두 계산을 해봐야함
		for (int j = 2; j <= 64; j++) {
			num = N;
			answer = 0;
			int k = 0;
			while (true) {   //해당 진수에 따라서 순서대로 arr에 넣는다. 실제 진수와는 반대로 결과가 저장이 되어 있음
				arr[k] = num%j;
				num = num / j;
				k++;
				if (num < j) break;
			}
			arr[k] = num;
			
			int n = 0;
			while (true) {    
				if (arr[n] != arr[k]) {  //만약 다른 수가 있다면 바로 계산 종료  다른 진수에 대한 계산을 진행한다.
					break;
				}

				n++;
				k--;

				if (n > k || n == k) {   //break가 되지 않고 끝까지 계산이 되었다면
					answer = 1;     //계산 결과는 1을 출력
					break;
					cout << j << endl;
				}
			}
			if (n > k || n == k) {
				break;
			}
		}
	
		cout << answer << endl;
	}

	getchar();
	return 0;
}