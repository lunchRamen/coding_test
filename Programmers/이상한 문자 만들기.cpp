#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    
    int idx=0;
    for(int i=0;i<s.size();i++){
        if(s[i]==' ') {
            idx=0;
            continue;
        }
        if(idx%2==0){//인덱스가 짝수 ->대문자로
            if(s[i]>='a' && s[i]<='z'){
                s[i]=s[i]-'a'+'A';
                //idx++;
            }
        }
        if(idx%2!=0){//인덱스가 홀수 -> 소문자로
            if(s[i]>='A' && s[i]<='Z'){
                s[i]=s[i]-'A'+'a';
                //idx++;
            }
        }
        idx++;
    }
    answer=s;
    return answer;
}
