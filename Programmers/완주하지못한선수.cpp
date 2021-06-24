#include <string>
#include <vector>
#include <map>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    map<string,int> m;
    
    for(string name:participant){
        m[name]++;
    }
    for(string name:completion){
        m[name]--;
    }
    for(pair p:m){
        if(p.second>0) return p.first;
    }
    /*
    map에 대해서 participant(마라톤 참여자)에 대해 m의 각 index에 출발 했다 표시 -> +1
    
    */
    
    //return answer;
}
