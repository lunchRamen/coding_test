/*
n+1번째 되는날 퇴사. 그전까지 최대한 많은 상담.
day를 1부터 시작해서
해당 날짜의 상담을 진행했으면
go(day+t[day],sum+p[day])
상담을 진행 안하고 다음날로 넘어가면
go(day+1,sum)
으로 재귀.
이 재귀가 멈추는 포인트는
day==n+1인 경우는 if(ans<sum)인 경우 정답 업데이트
day>n+1인 경우 범위를 넘었으므로 return.
 */
import java.util.*;

public class 퇴사 {
    static int[] t;
    static int[] p;
    static int n;
    static int ans=-10000000;
    static void go(int day,int sum){
        if(day==n+1){
            if(ans<sum) ans=sum;
            return;
        }
        if(day>n+1) return;
        go(day+1,sum);
        go(day+t[day],sum+p[day]);
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        t= new int[n+1];
        p= new int[n+1];
        for(int i=1;i<=n;i++){
            t[i]=sc.nextInt();
            p[i]=sc.nextInt();
        }
        go(1,0);
        System.out.println(ans);
    }
}
