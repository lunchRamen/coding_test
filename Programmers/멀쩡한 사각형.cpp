#include <algorithm>

using namespace std;
int gcd(int a,int b){
    while(b!=0){
        int temp=b;
        b=a%b;
        a=temp;
    }
    return a;
    
}
long long solution(int w,int h) {
    long long answer = 1;
    int k=gcd(w,h);
    answer=(long long)w *(long long)h -(w+h-k);
    return answer;
}
