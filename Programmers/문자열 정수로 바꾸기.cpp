#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    if(s[0]=='-'){
        string s1;
        for(int i=1;i<s.size();i++){
            s1+=s[i];
        }
        answer=-stoi(s1);
    }
    else{
        string s2;
        for(int i=0;i<s.size();i++){
            s2+=s[i];
        }
        answer=stoi(s2);
    }
    return answer;
}
