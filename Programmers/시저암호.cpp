#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == ' ') continue;
        //char temp=s[i];
        //s[i]=s[i]+n;
        //if(temp>='A' && temp<='Z' && s[i]>'Z') s[i]=s[i]-26;
        //if(temp>='a' && temp<='z' && s[i]>'z') s[i]=s[i]-26;
        char temp = s[i];
        if (temp >= 'a' && temp <= 'z') {
            //char start = 'a';
            //s[i] = (s[i] + n - start) % 26 + start;
            s[i] = s[i] + n;
            if (s[i] > 'z') s[i] -= 26;
        }
        else if (temp >= 'A' && temp <= 'Z') {
            //char start = 'A';
            //s[i] = (s[i] + n - start) % 26 + start;
            s[i] = s[i] + n;
            if (s[i] > 'Z') s[i] -= 26;
        }
    }
    answer=s;
    return answer;
}
