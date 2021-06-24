#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){//s[i]가 공백문자인 경우
            answer+=s[i];//answer에 공백문자를 더하기만하고 넘김.
            continue;
        }
        else{
            //이전 문자가 공백인지 확인함으로써, 문자 토큰화나 split을
            //안써도 된다.(이 경우에만 해당 되는듯)
            //단순하게 모든 문자를 돌아서 공백문자인 경우 정답에 더하고
            //넘기고, 나머지 경우 i가 0인데 소문자인 경우
            //i-1번째가 공백문자인데 소문자인 경우
            //나머지 경운데 대문자인 경우 대->소 소->대로 변환시켜주면 됨.
            if(s[i-1]==' ' || i==0){
                if(s[i]>='a' && s[i]<='z'){
                    s[i]=s[i]-'a'+'A';
                    //s[i]이전 문자가 공백이거나 i가 0인경우
                    //s[i]가 소문자인 경우에 대문자로 변환
                }
            }
            else{//나머지 모든 경우
                if(s[i]>='A' && s[i]<='Z'){
                    s[i]=s[i]-'A'+'a';
                }
            }
        }
        answer+=s[i];
    }
    return answer;
}
