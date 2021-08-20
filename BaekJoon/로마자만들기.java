/*
로마 숫자에서는 수를 나타내기 위해서 I, V, X, L을 사용한다.
각 문자는 1, 5, 10, 50을 의미하고, 이 문제에서 다른 문자는 사용하지 않는다.

하나 또는 그 이상의 문자를 이용해서 수를 나타낼 수 있다.
문자열이 나타내는 값은, 각 문자가 의미하는 수를 모두 합한 값이다. 예를 들어, XXXV는 35, IXI는 12를 의미한다.

실제 로마 숫자에서는 문자의 순서가 중요하지만, 이 문제에서는 순서는 신경쓰지 않는다.
예를 들어, 실제 로마 숫자에서 IX는 9를 의미하지만, 이 문제에서는 11을 의미한다.

로마 숫자를 N개 사용해서 만들 수 있는 서로 다른 수의 개수를 구해보자.
 */

/*
이건 우리가 생각하는 로마숫자 체계가 아니라,
각 문자들의 합을 수로 나타낸 것.

각 자리에 I V X L 4 개중 하나가 들어 갈 수 있는걸로 생각해서 4의 20승 생각해도 되지만,
n을 입력받았을 때,

I의 갯수를 a
V의 갯수를 b
X의 갯수를 c
L의 갯수를 n-a-b-c로 두고

i의 갯수를 0~n개까지
v의 갯수를 0~n-i개까지
x의 갯수를 0~n-i-v개까지
l은 n-i-v-x로 두고
sum에 각 숫자를 더한 다음 check index에 true로 만들면 됨.

처음 생각한 재귀 호출로 구하는건 10까진 바로 나오는데, 20을 입력해보니 답이 안나올정도로 시간이 오래걸림(시간초과)
->더 단축시킬 방법은 3중for문으로 각 로마 숫자의 갯수를 지정해줘서 한번에 더해주는 것.
 */

import java.util.*;

public class 로마숫자만들기 {
    static boolean[] check=new boolean[1001];
    static int cnt=0;
    static void go(int num,int sum,int n){
        if(num==n) {
            check[sum]=true;
            return;
        }

        go(num+1,sum+1,n);
        go(num+1,sum+5,n);
        go(num+1,sum+10,n);
        go(num+1,sum+50,n);


    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        //int[] roma={0,0,0,0};//I V X L 사용횟수
//        go(0,0,n);
//
//        int ans=0;
//        for(int k=1;k<=1000;k++){
//            if(check[k]) ans++;
//        }
        int ans=0;
        for(int i=0;i<=n;i++){
            for(int v=0;v<=n-i;v++){
                for(int x=0;x<=n-i-v;x++){
                    int l=n-i-v-x;
                    int sum=1*i+v*5+x*10+l*50;
                    check[sum]=true;
                }
            }
        }
        for(int i=1;i<=1000;i++){
            if(check[i]) ans+=1;
        }
        System.out.println(ans);
    }
}
