#include <string>
#include <vector>
#include <algorithm>

using namespace std;
//1번 수포자: mod 5 1,2,3,4,5 반복
//2번 수포자: mod 8 2,1,2,3,2,4,2,5 반복
//3번 수포자: mod 10 3,3,1,1,2,2,4,4,5,5 반복
vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int point[3]={0,0,0};
    int num1[5]={1,2,3,4,5};
    int num2[8]={2,1,2,3,2,4,2,5};
    int num3[10]={3,3,1,1,2,2,4,4,5,5};
    
    for(int i=0;i<answers.size();i++){
        if(answers[i]==num1[i%5]) point[0]++;
        if(answers[i]==num2[i%8]) point[1]++;
        if(answers[i]==num3[i%10]) point[2]++;
    }  
    int maxNum=max({point[0],point[1],point[2]});
    for(int i=0;i<3;i++){
        if(point[i]==maxNum) answer.push_back(i+1);
    }
    return answer;
}
