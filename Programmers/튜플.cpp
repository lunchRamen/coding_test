#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    
    vector<pair<int,int>> v(100001,{0,0});
    string temp;
    for(int i=2;i<s.size()-1;i++)
    {
        if(s[i]>='0' && s[i]<='9'){
            temp+=s[i];
        }
        else{
            if(temp.size()!=0){
                v[stoi(temp)].second=stoi(temp);
                v[stoi(temp)].first++;
                temp="";
                //temp.clear();
            }
        }
    }
    sort(v.begin(),v.end(),greater<pair<int,int>>());
    for(int i=0;i<v.size();i++){
        if(v[i].first==0) break;
        answer.push_back(v[i].second);
    }
//    for(auto a:v){
//        if(a.first==0) break;
//        answer.push_back(a.second);
//    }
    return answer;
}
