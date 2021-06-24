#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    int cnt=0;
    queue<pair<int,int>> q;//우선순위,인덱스 순
    priority_queue<int> pq;
    for(int i=0;i<priorities.size();i++){
        q.push(make_pair(priorities[i],i));
        pq.push(priorities[i]);
    }
    while(1){
        pair<int,int> temp=q.front();
        q.pop();
        if(temp.first==pq.top()){
            pq.pop();
            cnt++;
            if(temp.second==location){
                answer=cnt;
                break;
            }
        }
        else q.push(temp);
    }
    return answer;
}
