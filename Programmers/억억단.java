/*
s~e까지 수 중 가장 많이 등장한 수를 답해야한다.
입출력 예 설명을 통해, s~e까지 등장횟수를 나타내는건, 해당 수의 약수의 갯수라는걸 추론해내야함.
약수의 갯수인걸 알았다면, 약수를 구하는 최소의 시간복잡도를 구해야하는데,
여기선 int(num**0.5)+1 대신에 i씩 커지는 for loop을 돌린다. 이게 훨씬 시간복잡도가 낮던데
왜그런진 잘 모르겠음.

이렇게 각 숫자의 약수의 갯수를 구했다면,
어차피 끝은 e이기때문에, starts[i]에 대한 i~e까지 수 중 가장 많이 등장한 수를
찾으면 된다.
이것 또한, 그냥 통으로 다 구함.
e-1 ~ 0까지 i로 역으로 순회하면서 numbers[i](= i에 대한 약수의 갯수)가 numbers[dp[i+1]](= i+1까지 최적화한 e-1 ~ i+1까지 약수의 갯수의 최대값에 해당하는 숫자의 약수의 갯수)
보다 크거나 같다면 -> 같은 약수의 갯수를 가졌다면 작은 수를 추가해야하기때문에 dp[i] = i (i까지 최대 약수의 갯수를 가진 수는 i라고 저장)
아니라면, dp[i] = dp[i+1] (i+1까지 구한 최대 약수의 갯수를 가진 숫자를 덮어쓰기)

그래서 starts를 순회한다면, dp[starts[i]]로 starts[i]~e까지 최대 약수의 갯수를 갖는 숫자를 return한다.
*/
import java.util.*;
class Solution {
    public int[] solution(int e, int[] starts) {
        int[] answer = new int[starts.length];
        
        int[] numbers = new int[e+1];
        
        for (int i=2;i<=e;i++){
            for (int j=i*2;j<=e;j+=i){
                numbers[j]+=1;
            }
        }
        
        int[] dp = new int[e+1];
        dp[e] = e;
        for (int i=e-1;i>0;i--){
            if (numbers[i]>= numbers[dp[i+1]]){
                dp[i]=i;
            }
            else{
                dp[i]=dp[i+1];
            }
        }
        
        
        for (int i=0;i<starts.length;i++){
            answer[i]=dp[starts[i]];
        }
        
        
        return answer;
    }
}
