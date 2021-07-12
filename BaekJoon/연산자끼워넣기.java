import java.lang.reflect.Array;
import java.util.*;
/*
최소값과 최대값을 한번에 받아서 비교할수 있는
Pair 클래스 정의

후에 Pair를 return type으로 받는 calc함수 정의
calc함수에는 숫자배열,숫자배열 index,현재 합계(sum),+-*%갯수를 넘겨줌

index가 n에 다다르면 현재 합계를 최소와 최대로 return해줌.
아닌 경우라면, ArrayList res를 Pair자료형 형태로 만들어서
재귀를 돌릴건데,
각 사칙연산의 수가 0이 될때까지 돌아감.
res.add()형태로 넣어줘서
index가 n이 된 경우에 그때까지 사칙연산 한 총 합계인 cur를 최소와 최대에 넣어서 return된걸 res의 원소로 넣는 것.

이 사칙연산 재귀가 다 마친 후에,
Pair ans=res.get(0);으로 res의 0번째원소를 얻은 다음에
for each문을 돌려서 ArrayList res의 모든 원소를 둘러봐서 ans의 min보다 작으면 update,ans의 max보다 크면 update
해서 ans를 return해주면 입력받은 연산자의 갯수로 만들 수 있는 최대 최소값이 ans에 저장돼서 return되는 꼴.
 */
class Pair{
    int max;
    int min;
    public Pair(int min,int max){
        this.min=min;
        this.max=max;
    }
}
public class 연산자끼워넣기 {
    static Pair calc(int[] a,int index,int cur,int plus,int minus,int times,int div){
        int n=a.length;
        if(index==n){
            return new Pair(cur,cur);
        }
        ArrayList<Pair> res=new ArrayList<>();
        if(plus>0){
            res.add(calc(a,index+1,cur+a[index],plus-1,minus,times,div));
        }
        if(minus>0){
            res.add(calc(a,index+1,cur-a[index],plus,minus-1,times,div));
        }
        if(times>0){
            res.add(calc(a,index+1,cur*a[index],plus,minus,times-1,div));
        }
        if(div>0){
            res.add(calc(a,index+1,cur/a[index],plus,minus,times,div-1));
        }
        Pair ans=res.get(0);
        for(Pair p:res){
            if(ans.max<p.max) ans.max=p.max;
            if(ans.min>p.min) ans.min=p.min;
        }
        return ans;
    }
    static int n;
    //숫자가 11개까지면 그 사이에 들어 갈 수 있는 연산자는 10개.
    static int plus;
    static int minus;
    static int times;
    static int div;
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        int[] a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        plus=sc.nextInt();
        minus=sc.nextInt();
        times=sc.nextInt();
        div=sc.nextInt();

        Pair ans=calc(a,1,a[0],plus,minus,times,div);
        System.out.println(ans.max);
        System.out.println(ans.min);
    }
}
