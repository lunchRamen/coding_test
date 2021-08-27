/*
원래 내 생각

각각의 스티커를 Pair형태 x y좌표로 받아 ArrayList에 넣고
2중 for문을 돌려서 모든 스티커 비교 한 후 모눈종이 범위 안, 겹치지 않는 최대 범위를 구하려고 했는데
마음대로 되지 않음.

강사님 문제 풀이

i번째 스티커의 가로,세로를 각각 다른 배열에 저장-> 2차원 배열 1개 or Pair클래스가 아닌 1차원 배열 2개.

그리고 90도 회전했을때 가능한 경우를 계산하는걸
rot(회전) for문 2개를 만들어서 4가지 경우(0, 90 180 270)에 대해 다 계산 하는듯.

r1,c1은 r[i] c[i] 에서
r2,c2는 r[j] c[j] 에서( 내가 생각한것과 동일한 범위)

근데, rot에서 첫번째 스티커가 그냥, 90도 돌린경우 두번째 스티커가 그냥,90도 돌린경우 이렇게 4가지 경우를 다 비교해서
범위 내에 있는지(h,w) 검사하는데,
해당 스티커가 그냥 그냥 그냥 90 90 그냥 90 90로 붙어서 있을 수 있는 범위는
내가 생각했던 첫번째 스티커는 (0,0)부터 두번째 스티커는 (h-1,w-1)부터가 아닌(이러면 붙어있는 경우가 안나옴)
가로 중 큰게 h보다 작으면 -> 두개의 세로를 더한게 w보다 작은경우
두개의 가로를 더한게 h보다 작으면 -> 세로중 큰게 h보다 작은경우
이렇게 도형을 놓고 봐야 스티커를 붙일 수 있는 최대범위를 구할 수 있게 된다.


 */
import java.util.*;

public class 두스티커_sol {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int h=sc.nextInt();
        int w=sc.nextInt();
        int n=sc.nextInt();

        int[] r=new int[n];
        int[] c=new int[n];

        for(int i=0;i<n;i++){
            r[i]=sc.nextInt();
            c[i]=sc.nextInt();
        }//i번째 스티커의 길이,높이 저장.

        int ans=0;
        for(int i=0;i<n;i++){
            int r1=r[i];
            int c1=c[i];
            for(int j=i+1;j<n;j++){
                int r2=r[j];
                int c2=c[j];
                for(int rot1=0;rot1<2;rot1++){
                    for(int rot2=0;rot2<2;rot2++){
                        if(r1+r2<=h && Math.max(c1,c2)<=w){
                            int temp=r1*c1+r2*c2;
                            if(ans<temp) ans=temp;
                        }
                        if(Math.max(r1,r2)<=h && c1+c2<=w){
                            int temp=r1*c1+r2*c2;
                            if(ans<temp) ans=temp;
                        }
                        int t2=r2;
                        r2=c2;
                        c2=t2;
                    }
                    int t1=r1;
                    r1=c1;
                    c1=t1;
                }
            }
        }
        System.out.println(ans);
    }
}
