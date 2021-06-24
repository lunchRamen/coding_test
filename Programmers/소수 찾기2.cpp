#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
//    for(int i=3;i<=n;i++){
//        bool pn=true;
//        for(int j=2;j<i;j++){
//           if(i%j==0) {
//               pn=false;
//               break;
//          }
//        }
//        if(pn==true) answer++;
//    }
    //에라토스테네스의 체
    vector<bool> visit(n+1);
    visit[0]=visit[1]=true;
    for(int i=2;i*i<=n;i++){
        for(int j=i+i;j<=n;j+=i){
            visit[j]=true;
        }
    }
    for(int i=1;i<=n;i++){
        if(visit[i]==false) answer++;
    }
    return answer;
}
