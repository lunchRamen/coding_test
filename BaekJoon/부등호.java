/*
부등호의 갯수가 주어지고 부등호 기호들이 주어졌을때, 이 부등호로 만들수 있는 가장 큰 숫자랑 가장 작은 숫자.
숫자는 0~9까지 됨.
ex) 2
    < >  -> 897이 최대 012가 최소. 부등호 갯수는 최대 9개.

첫번째 부등호가 중요한듯.
첫번째 부등호가 >이면 9시작(최대) 1시작(최소) <면 0시작(최소) 8시작(최대)

index가 n+1이 되는 경우 모든 숫자가 다 찼기때문에 각 부등호 방향마다 숫자의 대소비교를 해서 하나라도 틀리면
false, 다 맞으면 true를 반환하는 ok함수 만들고

for문으로 0~9까지 숫자를 방문,안방문으로 따져서
go(index+1,num+Integer.toString(i))로 문자열 num에 각 숫자를 더해서 재귀호출.
재귀가 n+1까지 가서 return되면 각 방문 숫자를 다시 false로 하기위해 c[i]=false; 설정.
 */
import java.util.*;
public class 부등호 {
    static int n;
    static char[] a=new char[20];
    static ArrayList<String> ans=new ArrayList<>();
    static boolean[] check=new boolean[10];
    static boolean ok(String num){
        for(int i=0;i<n;i++){
            if(a[i]=='<'){
                if(num.charAt(i)>num.charAt(i+1)) return false;
            }
            if(a[i]=='>'){
                if(num.charAt(i)<num.charAt(i+1)) return false;
            }
        }
        return true;
    }
    static void go(int index,String num){
        if(index==n+1){
            if(ok(num)) ans.add(num);
            return;
        }
        for(int i=0;i<=9;i++){
            if(check[i]) continue;
            check[i]=true;
            go(index+1,num+Integer.toString(i));
            check[i]=false;
        }
    }
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        n=sc.nextInt();
        for(int i=0;i<n;i++){
            a[i]=sc.next().toCharArray()[0];
        }
        go(0,"");
        Collections.sort(ans);
        int m=ans.size();
        System.out.println(ans.get(m-1));
        System.out.println(ans.get(0));
    }
}
