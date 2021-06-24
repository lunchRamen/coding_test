#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string numbers) {
    int answer = 0;
    vector<char> v;
    vector<int> nums;
    vector<bool> check(10000000,true);
    check[0]=false;
    check[1]=false;
    
    for(int i=2;i*i<10000000;i++){
        for(int j=i*i;j<10000000;j+=i){
            check[j]=false;
        }
    }
    
    for(int i=0;i<numbers.size();i++){
        v.push_back(numbers[i]);
    }
    sort(v.begin(),v.end());
    do{
        string temp="";
        for(int i=0;i<v.size();i++){
            temp.push_back(v[i]);
            nums.push_back(stoi(temp));
        }
    }while(next_permutation(v.begin(),v.end()));
    
    sort(nums.begin(),nums.end());
    nums.erase(unique(nums.begin(),nums.end()),nums.end());
    
    for(int i=0;i<nums.size();i++){
        if(check[nums[i]]) answer++;
    }
    return answer;
}
