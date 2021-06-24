#include <string>
#include <vector>

using namespace std;

string calculate(int n,int num){
    string ret="";
    if(n==0) {
        ret="0"+ret;
        return ret;
    }
    while(n>0){
        int remain=n%num;
        n/=num;
        if(remain>=0 && remain<=9){
            ret=to_string(remain)+ret;
        }
        if(remain>=10 && remain<=15){
            if(remain==10){
               ret="A"+ret; 
            }
            if(remain==11){
                ret="B"+ret;
            }
            if(remain==12){
                ret="C"+ret;
            }
            if(remain==13){
                ret="D"+ret;               
            }
            if(remain==14){
                ret="E"+ret;
            }
            if(remain==15){
                ret="F"+ret;
            }
        }
    }
    return ret;
}

string solution(int n, int t, int m, int p) {
    string answer = "";
    string temp="";
    for(int i=0;i<t*m;i++){
        temp=temp+calculate(i,n);
    }
    int numP=p-1;
    while(t){
        answer=answer+temp[numP];
        numP+=m;
        t--;
    }
    
    return answer;
}
