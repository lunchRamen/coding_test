import java.util.Scanner;
/*
1.  if(index==n) return;
        if(sum==m) {
            cnt++;
            return;
        }에서 순서를 바꿔서 실행했더니 결과값이 이상하게 나오는데, index검사부터 해야하는 이유?


연속한 숫자의 합이 m이 되게끔
->for문을 각 인덱스부터 시작해서 solve 함수 돌림
index가 n인데 sum이 m이면 추가
sum이 m이면 추가
sum<m이면 재귀
sum>m이면 return

 */

public class 수들의합2 {
    static int n,m;
    static int cnt=0;
    public static void solve(int[] a,int sum,int index){
        if(index==n) {
            if(sum==m) cnt+=1;
            return;
        }
        if(sum==m) {
            cnt+=1;
            return;
        }
        if(sum<m){
            solve(a,sum+a[index],index+1);
        }
        if(sum>m){
            return;
        }
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        int[] a=new int[n];

        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        for(int i=0;i<n;i++){
            solve(a,0,i);
        }
        System.out.println(cnt);
    }
}
