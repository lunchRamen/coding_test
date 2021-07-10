import java.util.Scanner;

/*
입력받은 수들의 집합으로 나타낼수 없는 수 출력.

입력받은 집합을 선택으로 풀면 됨.


 */
public class 부분수열의합2 {
    public static boolean ok=true;
    public static int n;
    public static int[] arr=new int[20];
    public static boolean[] check=new boolean[20*100000+10];
    //숫자는 최대 20개 주어질 수 있고, 숫자 하나당 최대값은 10만.
    //그래서 20*10만을 해주고
    //그 이후부터 1~false가 나올때까지 for문을 돌려서 solve진행.
    //solve로 arr배열의 원소 0~n까지 돌면서 n개 다 방문했으면
    //check[sum]을 true로 바꿔주고
    //그전엔 재귀로 index+1,합에 arr[index]한 경우, 안더한경우로 재귀를 돌려줌.
    public static void solve(int start,int sum){
        if(start==n){
            check[sum]=true;
            return;
        }
        solve(start+1,sum+arr[start]);
        solve(start+1,sum);
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        solve(0,0);
        
        for(int i=1;;i++){
            if(check[i]==false){
                System.out.printf("%d\n",i);
                break;
            }
        }

    }
}
