import java.util.*;

/*
number에 대해서 약수의 갯수를 numbers 배열에 저장하고, numbers[i] > limit -> numbers[i]=power;하고 합을 return.
*/
class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        
        int[] numbers = new int[number+1];
        
        for (int i=1;i<=number;i++){
            for (int j=i;j<=number;j+=i){
                numbers[j]+=1;
            }
        }
        
        for (int i=1;i<=number;i++){
            if (numbers[i]>limit) numbers[i] = power;
        }
        
        return Arrays.stream(numbers).sum();
    }
}
