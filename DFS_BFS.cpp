#include<iostream>

using namespace std;

int n;
int map[30][30];
int DFSvisit[30];
int BFSvisit[30];
int rear, front;
int queue[30];

void DFS(int v) {
	DFSvisit[v]=1;

	cout << v << " ";
	for (int i = 1; i <= n; i++) {
		if (map[v][i] == 1 && !DFSvisit[i])
			DFS(i);
	}
}

void BFS(int v) {
	BFSvisit[v] = 1;
	cout << v << " ";
	queue[rear++] = v;
	while (front < rear) {
		v = queue[front++];
		for (int i = 1; i <= n; i++) {
			if (map[v][i] == 1 && !BFSvisit[i]) {
				BFSvisit[i] = 1;
				cout << i << " ";
				queue[rear++] = i;
			}
		}
	}
}

int main() {
	int start, m;
	int v1, v2;

	cin >> n >> m >> start;

	for (int i = 0; i < m; i++) {
		cin >> v1 >> v2;
		map[v1][v2] = map[v2][v1] = 1;
	}
	DFS(start);
	cout << endl;
	BFS(start);

	cin >> start;

	return 0;
}