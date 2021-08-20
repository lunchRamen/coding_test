
/*
현진 치킨에서 판매하는 치킨은 양념 치킨, 후라이드 치킨, 반반 치킨으로 총 세 종류이다.
반반 치킨은 절반은 양념 치킨, 절반은 후라이드 치킨으로 이루어져있다.
양념 치킨 한 마리의 가격은 A원, 후라이드 치킨 한 마리의 가격은 B원, 반반 치킨 한 마리의 가격은 C원이다.

상도는 오늘 파티를 위해 양념 치킨 최소 X마리,
후라이드 치킨 최소 Y마리를 구매하려고 한다.
반반 치킨을 두 마리 구입해 양념 치킨 하나와 후라이드 치킨 하나를 만드는 방법도 가능하다.
상도가 치킨을 구매하는 금액의 최솟값을 구해보자.
 */

/*
내가 문제에서 놓친점

반반 2마리로 후라이드 또는 양념 1마리를 채우는게 더 쌀 수도 있다는 생각을 못함.
반반이 싼 경우, 작은 마릿수로 채워넣고 나머진 무조건 후라이드 혹은 양념으로 더했는데,
반반 2마리가 후라이드+양념보다 싼경우 말고
반반 2마리가 후라이드or양념 "1마리"보다 쌀 수도 있음.

제발 사칙연산 기호 헷갈리지 말자....찾기 너무 힘듬
 */
import java.util.*;

public class 양반후반 {
    public static void main(String[] args) {
        int a,b,c,x,y;
        Scanner sc=new Scanner(System.in);

        a=sc.nextInt();//양념치킨 가격
        b=sc.nextInt();//후라이드 가격
        c=sc.nextInt();//반반 가격
        x=sc.nextInt();//양념 마리수
        y=sc.nextInt();//후라이드 마리수

        long ans=0;
        if(a+b>2*c){
            if(x>y){
                ans+=2*y*c;
                ans+=Math.min((x-y)*a,(x-y)*(c*2));
            }
            else{
                ans+=2*x*c;
                ans+=Math.min((y-x)*b,(y-x)*(c*2));
            }
        }
        else{
            ans+=(x*a+y*b);
        }
        System.out.println(ans);
    }
}
