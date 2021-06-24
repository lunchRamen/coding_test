#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int nump=0;
    int numy=0;
    for(int i=0;i<s.size();i++){
        if(s[i]=='p' || s[i]=='P') nump++;
        if(s[i]=='y'|| s[i]=='Y') numy++;
    }
    if(nump==numy) answer=true;
    else answer=false;
    return answer;
}
