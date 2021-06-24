#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;

    stack<char> stk;
    
    for(int i=0;i<s.size();i++){
        if(s[i]=='(') stk.push(s[i]);
        if(s[i]==')'){
            if(stk.empty()) return false;
            else stk.pop();
        }
    }
    if(!stk.empty()) answer=false;
    return answer;
}
