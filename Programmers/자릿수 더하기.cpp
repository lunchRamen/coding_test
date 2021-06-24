#include <iostream>

using namespace std;
int solution(int n)
{
    int answer = 0;

    while(n){
        int res=n%10;
        answer+=res;
        n=n/10;
    }

    return answer;
}
