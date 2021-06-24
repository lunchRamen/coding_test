#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    vector<int> a;
    while(n){
        int res=n%10;
        a.push_back(res);
        n=n/10;
    }
    sort(a.begin(),a.end());
    for(int i=0;i<a.size();i++){
        answer=answer+a[i]*pow(10,i);
    }
    return answer;
}
