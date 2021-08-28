/*
처음 생각
순열을 쓴다길래 그냥 순열 구현하면 될 줄 알았는데,
"B보다 작은것 중에서 제일 큰것"을 구해야 하는 조건을 순열과 같이 써야하기 때문에,
숫자->문자열->숫자의 과정이 필요한데 순열+숫문숫을 합치는 과정에서 어떻게 코드를 짜야할지 애먹고, 실패함.

->강사님 두번째 코드를 보면
순열로 돌릴 a를 그냥 String으로 받고,
그걸 charAt(i)-'0'으로 a배열에 각자리 수 숫자로 넣은 다음 재귀로 구현.(순열이 아니라)

재귀함수에선 기본 자료형만 씀(재귀시 배열 정보 공유가 안된 독립시행이니까)

키포인트: 다음 자리 수 넘어갈때 나머지연산 이런게 아니라,
789인 경우
a[0]=7 a[1]=8 a[2]=9여서 idx를 추가할때마다 num*10을 한 다음 a[i]을 더하면
7 -> 78 -> 789 이렇게 똑같은 숫자로 만들 수 있음.

이 풀이의 경우 순열처럼
1234 1243 1324.. 이런식으로 전수조사가 아니라
1
2
3
4 부터 해서 다음 자리를 랜덤하게 가져감.

또한 ans 기본값을 -1로 해둠으로써 재귀가 한번도 안돌아간(조건에 맞지 않는) 케이스는 그대로 -1을 출력해줌.
 */

import java.util.*;

public class 숫자재배치 {
    static int[] a;
    static boolean[] check;
    static int b;
    static int n;
    static int go(int idx,int num){
        if(idx==n){
            return num;
        }
        int ans=-1;
        for(int i=0;i<n;i++){
            if(check[i]==true) continue;
            if(idx==0 && a[i]==0) continue;
            check[i]=true;
            int temp=go(idx+1,num*10+a[i]);
            if(temp<b){
                if(ans==-1 || ans<temp){
                    ans=Math.max(ans,temp);
                }
            }
            check[i]=false;
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String num=sc.next();
        n=num.length();
        a=new int[n];
        check=new boolean[n];
        for(int i=0;i<n;i++){
            a[i]=num.charAt(i)-'0';
        }
        b=sc.nextInt();
        System.out.println(go(0,0));
    }
}
