#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int cor=0;
    //최고순위
    for(int i=0;i<lottos.size();i++){
        if(lottos[i]==0) {
            cor++;
            continue;
        }
        for(int j=0;j<win_nums.size();j++){
            if(lottos[i]==win_nums[j]) cor++;
        }
    }
    if(cor==6) answer.push_back(1);
    if(cor==5) answer.push_back(2);
    if(cor==4) answer.push_back(3);
    if(cor==3) answer.push_back(4);
    if(cor==2) answer.push_back(5);
    if(cor<2) answer.push_back(6);
    
    cor=0;
    //최저순위
    for(int i=0;i<lottos.size();i++){
        for(int j=0;j<win_nums.size();j++){
            if(lottos[i]==win_nums[j]) cor++;
            if(lottos[i]==0) continue;
        }
    }
    if(cor==6) answer.push_back(1);
    if(cor==5) answer.push_back(2);
    if(cor==4) answer.push_back(3);
    if(cor==3) answer.push_back(4);
    if(cor==2) answer.push_back(5);
    if(cor<2) answer.push_back(6);
    return answer;
}
