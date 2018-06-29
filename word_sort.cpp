#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

bool compare(const string &a, const string &b) {
	if (a.length() == b.length())
		return (a < b);

	else
		return a.length() < b.length();
}

int main() {
	
	int numCases;
	cin >> numCases;

	string word_list[20000];

	for (int i = 0; i < numCases; i++) {
		cin >> word_list[i];
	}

	sort(word_list, word_list + numCases, compare);

	for (int i = 0; i < numCases; i++) {
		if (i != 0 && word_list[i] == word_list[i - 1]) continue;

		else {
			cout << word_list[i]<<endl;
		}
	}
	cin >> numCases;
	getchar();
	return 0;
}