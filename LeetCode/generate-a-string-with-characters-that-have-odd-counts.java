import java.util.*;
class Solution {
    /*
    n이 주어졌을 때, 길이가 n인 문자열을 return 하는데, 문자열의 문자의 등장횟수가 모두 홀수개가 되도록 하게끔.
    
    a~z까지에 대한 hashmap을 만들고, 이것에 대해 n을 홀수개씩 줄여가면서 문제를 해결하려고했는데, 이러면 처리해줘야할 조건들이 너무 많다.
    -> 그냥 짝수인 경우 1과 n-1 홀수인 경우 1,1,n-2로 홀수로 나타낸다음, a,b.   a,b,c로 할당해주면 끝남.
    n==1인 경우만 그냥 a를 return하게끔.
     */
    public String generateTheString(int n) {
        String answer = "";
        if (n == 1) return "a";
        if (n%2 == 0){
            answer += "a" + "b".repeat(n-1);
        }
        else{
            answer += "a"+"b" + "c".repeat(n-2);
        }
        return answer;
    }
}
