#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(),citations.end());
    
    int inyoung=1;
    int h_index_num=0;
    
    while(1){
        for(int i=0;i<citations.size();i++){
            if(citations[i]>=inyoung) h_index_num++;
        }
        if(inyoung>=h_index_num){
            answer=h_index_num;
            break;
        }
        else {
            inyoung++;
            h_index_num=0;
        }
    }
    return answer;
}
