import java.util.*;

import static java.lang.System.exit;

/*
상도시의 차량 번호판 형식이 주어졌을 때, 가능한 차량 번호판의 개수를 구해보자.

번호판에 사용할 수 있는 숫자는 0, 1, 2, ..., 8, 9이다.
사용할 수 있는 문자는 a, b, c, d, ..., y, z이다.
차량 번호판의 형식은 최대 4글자이고, c와 d로 이루어진 문자열로 나타낼 수 있다.
c는 문자가 위치하는 자리, d는 숫자가 위치하는 자리이다.
같은 문자 또는 숫자가 연속해서 2번 나타나면 안 된다.
예를 들어, 형식이 "cd"이면, a1, d4, h5, k4 등이 가능하다.
형식이 "dd"인 경우에 01, 10, 34, 69는 가능하지만, 00, 11, 55, 66은 같은 숫자가 2번 연속해서 불가능하다.
 */

/*
번호판의 경우의 수 : 10
문자의 경우의 수 :26(소문자만 사용 가능)

번호판은 최대 4글자(최대 26의 4승)->완전탐색 가능

같은 문자 또는 숫자 연속 x.
 */

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String n=sc.next();//c면 문자가 d면 숫자가 위치해야함.
        char[] c=n.toCharArray();

        char idx=c[0];
        int sum=0;
        if(idx=='c') sum+=26;
        if(idx=='d') sum+=10;

        if(c.length==1){
            System.out.println(sum);
            exit(0);
        }
        for(int i=1;i<c.length;i++){
            if(c[i]=='c'){
                if(idx=='c'){
                    sum*=25;
                }
                else{
                    sum*=26;
                }
                idx=c[i];
            }
            else if(c[i]=='d'){
                if(idx=='d'){
                    sum*=9;
                }
                else{
                    sum*=10;
                }
                idx=c[i];
            }
        }
        System.out.println(sum);
    }
}
