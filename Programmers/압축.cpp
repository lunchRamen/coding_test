#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(string msg) {
    vector<int> answer;
    unordered_map<string,int> m;
    int index;
    string temp="";
    for(index=1;index<=26;index++){
        temp+='A'+index-1;
        m.emplace(temp,index);
        temp="";
    }
    for(int i=0;i<msg.size();i++){
        string temp="";
        temp+=msg[i];
        int count=0;
        int j=i;
        while(m.find(temp)!=m.end()){
            count++;
            j++;
            temp+=msg[j];
        }
        i+=count-1;
        m.emplace(temp,index++);
        temp.pop_back();
        answer.push_back(m[temp]);
    }
    return answer;
}
