#include <string>
#include <vector>

using namespace std;

string solution(vector<string> seoul) {
    string answer = "";
    string ans="Kim";
    int ansNum=0;
    for(int i=0;i<seoul.size();i++){
        if(ans.compare(seoul[i])==0) {
            string s=to_string(i);
            answer="김서방은 "+s+"에 있다";
        }
    }
    return answer;
}
