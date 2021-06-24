#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;

    for(int i=0;i<arr.size();i++){
        if(arr[i]==arr[i+1]) {
            for(int j=i+1;arr[i]==arr[j];j++)
                arr[j]=-1;
        }
    }
    for(int i=0;i<arr.size();i++){
        if(arr[i]!=-1) answer.push_back(arr[i]);
    }
    return answer;
}
