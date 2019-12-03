#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  int n;
  cin >> n;
  int adjacency_matrix[n + 1][n + 1];
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      cin >> adjacency_matrix[i][j];
    } 
  }
  int vs[n + 1];
  for (int i = 1; i <= n; i++) {
      cin >> vs[i];
  }

  int deleted[n + 1];
  int output[n + 1];
  for (int i = 1; i <= n; i++) {
    deleted[i] = 0;
    output[i] = 0;
  }

  for (int e = 1; e <= n; e++) {
    int d[n + 1][n + 1];
    for (int di = 1; di <= n; di++) {
        for (int dj = 1; dj <= n; dj++) {
          d[di][dj] = adjacency_matrix[di][dj];
        }
    }
    for (int k = 1; k <= n; k++) {
      if (deleted[k]) {continue;}
      for (int i = 1; i <= n; i++) {
        if (deleted[i]) {continue;}
        for (int j = 1; j <= n; j++) {
          if (deleted[j]) {continue;}
          d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        }
      }
    }
    int s = 0;
    for (int row = 1; row <= n; row++) {
      if (deleted[row]) {continue;}
      for (int col = 1; col <= n; col++) {
          if (deleted[col]) {continue;}
          s += d[row][col];
      }
    }
    output[e] += s;
    deleted[vs[e]] = 1;
  }
  
  for (int i = 1; i < n; i++) {
      cout << output[i] <<  " ";
  }
  cout << output[n] << endl;
  return 0;
}
