#include <string>
#include <vector>

using namespace std;

bool check(int n,int goal){
    int sum=0;
    //if(sum==goal) return true;
    while(sum<goal){
        sum+=n;
        n++;
        if(sum==goal) return true;
    }
    return false;
}
int solution(int n) {
    int answer = 0;
    vector<int> v(n+1);
    for(int i=0;i<=n;i++){
        v[i]=i;
    }
    for(int i=1;i<=n;i++){
        bool c=check(v[i],n);//i번째부터 연속으로 수를 더해서 n이 되는지 확인하는 함수.
        if(c==true) answer++;
    }
    return answer;
}
