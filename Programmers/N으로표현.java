import java.util.*;

/*
dp문제를 풀때
재귀로 top down bottom up
dp배열을 만들어서 규칙성을 찾은 후 bottom up
이렇게 있는데, 개인적으론 후자가 나은듯 함.

이 문제 풀이의 경우 후자로 풀었는데,
일반 int형 배열로 dp를 만든게 아니라 HashSet으로 만듬.
그 이유는 사칙연산의 결과값 중 중복을 제거하고, 굳이 인덱스로 다루지 않을 거라 그렇게 만듬.

dp[i]에 해당하는건 N을 i번 썼을때 나오는 모든 결과값들의 경우의 수를 중복없이 dp[i]에 저장하려고 만듬
-> dp[i]를 다시 HashSet으로 만들어서

for문을 2개 만든다음
outer for문에는 N NN NNN...을 쉽게 만들기 위해 String형으로 바꿔서 N을 저장해둔 다음에
i=1인경우엔 dp[1].add(Integer.parseInt(n_))으로 다시 Integer형으로 바꿔서 저장하고
이후에는 n_+=String.valueOf(N)으로 NN...이런 형태를 만들어서 dp[i]에 저장.
->그래서 초기형태의 hashset엔 dp[i]엔 N이 i번 반복되는 수가 들어가 있음.

이후 inner for문에서 j를 1~i-1까지 돌리면서
"calc(j,i)를 돌리는데 calc함수가
dp[j] dp[i-j]로 해당 원소의 hashset을 반복자 돌려서
사칙연산해서 나온 결과를 dp[i]에 저장해서 업데이트 해주는 함수.
->dp[1]~dp[i-1]까지=N~ N이 i-1번 반복되는 경우와 dp[j]=N이 j번 반복되서 만드는 수를
사칙연산 한 결과를 dp[i]에 집어넣는다.->왜냐면 j+i-j=i라서 N을 i번 사용해서 만들수 있는 경우의 수에 해당하기때문."
->이 부분이 가장 중요. dp[i]를 dp[j]+dp[i-j]에 들어있는 모든 수들의 사칙연산 결과를 집어넣어서 업데이트 한다는 점이
엄청 특이함. 보통 이전 index들의 결과들을 조합해서 만드는데, 이건 비슷하지만 다른 느낌.

이걸 dp[j] dp[i-j]에 모든 원소를 돌려서 사칙연산 결과를 dp[i]에 업데이트 하고,
dp[i].contains(number)-> N을 i번 써서 만들수 있는 모든 경우의 수 중 number가 있으면
i가 최소로 쓰는 경우니까 i를 return 하고 8번까지 써서 못만들었으면 -1을 return.
*/

class Solution {
    public static HashSet<Integer>[] dp=new HashSet[9];
    public int solution(int N, int number) {
        int answer = 0;
        if(N==number){
            return 1;
        }
        String n_=String.valueOf(N);
        for(int i=0;i<=8;i++){
            dp[i]=new HashSet<Integer>();
            if(i==1) dp[1].add(Integer.parseInt(n_));
            if(i<2) continue;
            n_+=String.valueOf(N);
            dp[i].add(Integer.parseInt(n_));
            for(int j=1;j<i;j++){
                calc(j,i);
                if(dp[i].contains(number)){
                    return i;
                }
            }
        }
        return -1;
    }
    static void calc(int a,int b){
        Iterator<Integer> listA=dp[a].iterator();
        Iterator<Integer> listB=dp[b-a].iterator();
        
        while(listA.hasNext()){
            int numA=listA.next();
            while(listB.hasNext()){
                int numB=listB.next();
                dp[b].add(numA+numB);
                dp[b].add(numA-numB);
                dp[b].add(numA*numB);
                if(numB!=0) dp[b].add(numA/numB);
            }
            listB=dp[b-a].iterator();
        }
    }
}
