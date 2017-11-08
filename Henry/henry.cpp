#include<iostream>
#include<fstream>

using namespace std;

//최대공약수를 구하는 함수, 분자는 분모보다 클 수 없기 때문에 무조건 b가 더 크다는 전제하에 계산
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

		//계산 결과 분자가 1이 되면 계산 종료
		while (num!=1) {
			start = deno / num + 1;   //분모를 분자로 나눈 값에 +1을 하면 주어진 분수보다 가장 큰 단위분수를 찾을 수 있음
			num = num*start - deno;
			deno = start *deno;
			gcm = GCM(num, deno);
			if (gcm == num) {  //만약 최대공약수가 분자라면 결국 분자는 1이 되므로 계산 종료
				deno = deno / num;
				break;
			}
			else if (gcm != 1) {   //최대공약수가 1이 아닌 다른 수라면 최대공약수로 분자와 분모를 각각 나누어 주고 다시 계산을 한다.
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