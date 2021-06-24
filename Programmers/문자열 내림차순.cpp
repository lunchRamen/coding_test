#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<char> c;
    for(int i=0;i<s.size();i++){
        c.push_back(s[i]);
    }
    sort(c.begin(),c.end(),greater<>());
    for(int i=0;i<c.size();i++){
        answer+=c[i];
    }
    return answer;
}
