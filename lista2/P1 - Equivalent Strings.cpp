# include <bits/stdc++.h>
using namespace std;

string a;
string b;
int slen;

void compare_odd_sized_string();
void compare_pair_sized_string();
bool compare(int a_init, int a_end, int b_init, int b_end);

int main() {  
  ios::sync_with_stdio(false);
  cin >> a;
  cin >> b;
  slen = a.length();
  compare_odd_sized_string();
  compare_pair_sized_string();
}

void compare_odd_sized_string() {
  if (slen % 2 != 0){
    if(a.compare(b) == 0){
      cout << "YES";
    } else {
      cout << "NO";
    }
  }
}

void compare_pair_sized_string() {
  if (slen % 2 == 0){
    int end_index = slen - 1;
    if (compare(0, end_index, 0, end_index)){
      cout << "YES";
    } else {
      cout << "NO";
    }
  }
}

bool compare(int a_init, int a_end, int b_init, int b_end){
  if (abs(a_end - a_init) == 0){
    return a[a_init] == b[b_init];
  }
  int amid = (a_init + a_end) / 2;
  int bmid = (b_init + b_end) / 2;
  bool c2a1 = compare(a_init, amid, b_init, bmid);
  bool c2a2 = compare(amid + 1, a_end, bmid + 1, b_end);
  bool c2a = c2a1 and c2a2;
  if (c2a){
    return true;
  } 
  bool c2b1 = compare(a_init, amid, bmid + 1, b_end);
  bool c2b2 = compare(amid + 1, a_end, b_init, bmid);
  bool c2b = c2b1 and c2b2;
  return c2b;
}
