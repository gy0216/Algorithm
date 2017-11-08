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

		//2�������� 64�������� ��� ����� �غ�����
		for (int j = 2; j <= 64; j++) {
			num = N;
			answer = 0;
			int k = 0;
			while (true) {   //�ش� ������ ���� ������� arr�� �ִ´�. ���� �����ʹ� �ݴ�� ����� ������ �Ǿ� ����
				arr[k] = num%j;
				num = num / j;
				k++;
				if (num < j) break;
			}
			arr[k] = num;
			
			int n = 0;
			while (true) {    
				if (arr[n] != arr[k]) {  //���� �ٸ� ���� �ִٸ� �ٷ� ��� ����  �ٸ� ������ ���� ����� �����Ѵ�.
					break;
				}

				n++;
				k--;

				if (n > k || n == k) {   //break�� ���� �ʰ� ������ ����� �Ǿ��ٸ�
					answer = 1;     //��� ����� 1�� ���
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