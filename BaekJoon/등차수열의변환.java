/*
브루트 포스로 풀려면 3의10만제곱이라 절대 못품.
등차수열의 특징을 이용, 등차수열의 경우 모든 수열에 공차가 같기때문에,
a[0]과 a[1]의 공차를 각각 -1 0 1 -1 0 1 9가지 경우를 통해서 공차의 경우의 수를 다 구하고,
이 공차를 구했으면 a[2]부턴 -1 0 1했을때 결과가 나오는지 확인만 해주면 된다.

여기서 2중 for문으로 a0과 a1의 설정이 중요한데,

a[0]과 a[1]의 9가지 조합만 마쳐야한다.
일단 d1과 d2가 0이 아닌경우(연산 이루어지는경우) 변화횟수를 1씩 늘려줘야하고
a0에는 d1을
a1에는 d2를 더해주는데
두개의 차이(공차) diff는 a[1]+d2-a[0]-d1이다.
그리고 이 a0에 공차를 더한걸로 시작을 한다.(등차수열이라면 이게 a1이니까)

그래서 i=2~n-1까지
a[i]가 an+diff면 change를 안올리고 진행하고
a[i]+-1이 an+diff면 change를 각각 1씩 올리고 진행하고
나머지 경우엔 break해준다.
그래서 ok가 true인 경우에만 change와 ans의 대소를 따져서 등차수열을 만드는 최소횟수를 구함,
 */
import java.util.*;
public class 등차수열변환 {
    static int n;
    static int[] a;
    static int ans=-1;

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        if(n==1){
            System.out.println(0);
            System.exit(0);
        }
        int ans=-1;
        for(int d1=-1;d1<=1;d1++){
            for(int d2=-1;d2<=1;d2++){
                int change=0;
                if(d1!=0) change++;
                if(d2!=0) change++;
                int a0=a[0]+d1;
                int diff=(a[1]+d2)-a0;//공차.
                boolean ok=true;
                int an=a0+diff;//첫번재 항에 공차를 더함 -> 등차수열이 적용됐다면 2번째항이 되어야함.
                for(int i=2;i<n;i++){
                    an+=diff;
                    if(a[i]==an) continue;
                    if(a[i]-1==an) change++;
                    if(a[i]+1==an) change++;
                    else{
                        ok=false;
                        break;
                    }
                }
                if(ok){
                    if(ans==-1 || ans>change){
                        ans=change;
                    }
                }
            }
        }
        System.out.println(ans);
    }
}
