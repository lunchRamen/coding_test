#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days(progresses.size(),0);
    for(int i=0;i<speeds.size();i++){
        while(progresses[i]<100){
            progresses[i]+=speeds[i];
            days[i]+=1;
        }
    }
    int s=days[0];
    int cnt=0;
    for(int i=0;i<days.size();i++){
        if(s<days[i]){
            answer.push_back(cnt);
            cnt=1;
            s=days[i];
        }
        else cnt++;
        if(i==days.size()-1) answer.push_back(cnt);
    }
    return answer;
}
