#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
    
    vector<pair<char,int>> c;
    for(int i=0;i<strings.size();i++){
        c.push_back(make_pair(strings[i][n],i));
    }
    sort(c.begin(),c.end());
    for(int i=0;i<strings.size()-1;i++){
        //if(c[i].first==c[i+1].first){
        //    if(strings[c[i].second].compare(strings[c[i+1].second])>0){
        //        swap(c[i],c[i+1]);
        //    }
        //}
        for(int j=i+1;j<strings.size();j++){
            if(c[i].first==c[j].first){
                if(strings[c[i].second].compare(strings[c[j].second])>0){
                    swap(c[i],c[j]);
                }
            }
        }
    }
    for(int i=0;i<strings.size();i++){
        answer.push_back(strings[c[i].second]);
    }
    return answer;
}
