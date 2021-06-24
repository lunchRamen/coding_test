#include <string>
#include <vector>

using namespace std;

//string week[7]={"FRI","SAT","SUN","MON","TUE","WED","THU"};
int month[12]={31,29,31,30,31,30,31,31,30,31,30,31};

string solution(int a, int b) {
    string answer = "";
    int sum=0;
    for(int i=0;i<a-1;i++){
        sum+=month[i];
    }
    sum+=b;
    //answer=week[sum%7-1];
    if(sum%7==1) answer="FRI";
    if(sum%7==2) answer="SAT";
    if(sum%7==3) answer="SUN";
    if(sum%7==4) answer="MON";
    if(sum%7==5) answer="TUE";
    if(sum%7==6) answer="WED";
    if(sum%7==0) answer="THU";
    return answer;
}
