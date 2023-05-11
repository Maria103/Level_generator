#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main(){
    queue<vector<ptrdiff_t>> q;
    vector<ptrdiff_t> c = {1, 0};
    q.push(c);
    
    c = {1, 1};
    q.push(c);
    q.pop();
    vector<ptrdiff_t> cur_c = q.front();
    cout << cur_c[0] << ' ' << cur_c[1] << '\n';
    if (q.empty()) cout << "kek";
}