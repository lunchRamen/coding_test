#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int> > land)
{
    int answer = 0;
    int n=land.size();
    
    for(int i=0;i<n-1;i++){
        land[i+1][0]+=max(land[i][1],max(land[i][2],land[i][3]));
        land[i+1][1]+=max(land[i][0],max(land[i][2],land[i][3]));
        land[i+1][2]+=max(land[i][0],max(land[i][1],land[i][3]));
        land[i+1][3]+=max(land[i][0],max(land[i][1],land[i][2]));
        //이렇게 짜면, 이전행의 같은 열이 최댓값이였는지, 안따져봐도 됨.
    }
    answer=max(land[n-1][0],max(land[n-1][1],max(land[n-1][2],land[n-1][3])));
    return answer;
}
