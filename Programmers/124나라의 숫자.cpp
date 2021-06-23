#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer = "";
    int m=n;
    int res;
    while(m){
        res=m%3;
        m=m/3;
        
        if(res==0){
            answer="4"+answer;
            m--;
        }
        if(res==1){
            answer="1"+answer;
        }
        if(res==2){
            answer="2"+answer;
        }
    }
    return answer;
}
