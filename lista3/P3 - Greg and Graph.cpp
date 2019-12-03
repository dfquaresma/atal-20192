#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  int n;
  cin >> n;
  long long adjacency_matrix[505][505];
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= n; ++j) {
      cin >> adjacency_matrix[i][j];
    } 
  }
  long long vs[505];
  for (int i = 1; i <= n; ++i) {
      cin >> vs[i];
  }
  long long output[505];
  for (int k = n; k > 0; --k) {
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][vs[k]] + adjacency_matrix[vs[k]][j]);
    for (int i = k; i <= n; ++i)
        for (int j = k; j <= n; ++j)
            output[k] += adjacency_matrix[vs[i]][vs[j]];
  }
  for (int i = 1; i < n; i++) {
      cout << output[i] <<  " ";
  }
  cout << output[n] << endl;
  return 0;
}
