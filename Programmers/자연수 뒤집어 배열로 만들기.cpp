#include <string>
#include <vector>

using namespace std;

vector<int> solution(long long n) {
    vector<int> answer;
    while(n){
        int res=n%10;
        answer.push_back(res);
        n=n/10;
    }
    return answer;
}
