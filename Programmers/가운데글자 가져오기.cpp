#include <string>
#include <vector>
#include <cmath>

using namespace std;

string solution(string s) {
    string answer = "";
    int n=s.size();
    if(n%2==0){
        int idx=n/2-1;
        answer+=s[idx];
        idx=n/2;
        answer+=s[idx];
    }
    if(n%2!=0){
        int idx=n/2;
        answer+=s[idx];
    }
    return answer;
}
