# include <bits/stdc++.h>
using namespace std;
 
int slen;
string a, b;
 
bool compare_ranges(int a_init, int b_init, int size) {
  for (int i = 0; i < size; i++) {
    if (a[a_init+i] != b[b_init+i]) {
      return false;
    }    
  }
  return true;
}

bool compare(int a_init, int b_init, int size){
  if (compare_ranges(a_init, b_init, size)) {
    return true;
  }
  if (size % 2 != 0){
    return false;
  }
 
  int mid = size / 2;
  int amid = a_init + mid;
  int bmid = b_init + mid;
  bool c2a1 = compare(a_init, b_init, mid);
  if (c2a1 && compare(amid, bmid, mid)){
    return true;
  } 
 
  bool c2b1 = compare(a_init, bmid, mid);
  return c2b1 && compare(amid, b_init, mid);
}

int main() {  
  ios::sync_with_stdio(false);
  cin >> a;
  cin >> b;
  slen = a.length();
  if (compare(0, 0, slen)){
    cout << "YES";
  } else {
    cout << "NO";
  }
  return 0;
}
