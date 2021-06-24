#include <string>
#include <vector>

using namespace std;

int countOne(int n){
    int ret=0;
    for(int i=0;i<31;i++){
        if(n&(0x01<<i)) ret++;
    }
    return ret;
}

int solution(int n) {
    int answer = 0;
    int k=n+1;
    while(1){
        if(countOne(n)==countOne(k)){
            answer=k;
            break;
        }
        k++;
    }
    return answer;
}
