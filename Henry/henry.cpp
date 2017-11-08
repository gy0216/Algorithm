#include<iostream>
#include<fstream>

using namespace std;

//�ִ������� ���ϴ� �Լ�, ���ڴ� �и𺸴� Ŭ �� ���� ������ ������ b�� �� ũ�ٴ� �����Ͽ� ���
int GCM(int a, int b) {
	int gcm;
	for (int i = a; i >0; i--) {
			if (a%i == 0 && b%i == 0) {
				gcm = i;
				break;
			}
		}
	return gcm;
}

int main() {

	ifstream inStream("input.txt");
	int numCases;
	int deno, num;
	int start;
	int gcm;

	inStream >> numCases;

	for (int i = 0; i < numCases; i++) {
		
		inStream >> num;
		inStream >> deno;

		//��� ��� ���ڰ� 1�� �Ǹ� ��� ����
		while (num!=1) {
			start = deno / num + 1;   //�и� ���ڷ� ���� ���� +1�� �ϸ� �־��� �м����� ���� ū �����м��� ã�� �� ����
			num = num*start - deno;
			deno = start *deno;
			gcm = GCM(num, deno);
			if (gcm == num) {  //���� �ִ������� ���ڶ�� �ᱹ ���ڴ� 1�� �ǹǷ� ��� ����
				deno = deno / num;
				break;
			}
			else if (gcm != 1) {   //�ִ������� 1�� �ƴ� �ٸ� ����� �ִ������� ���ڿ� �и� ���� ������ �ְ� �ٽ� ����� �Ѵ�.
				num = num / gcm;
				deno = deno / gcm;
			}
		}

		cout << deno << endl;
	}
	getchar();
	inStream.close();
	return 0;
}