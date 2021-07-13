/*
N개의 에너지 구슬이 일렬로.
i번째 에너지구슬의 무게는 W(i)
에너지 모으는 방법(반복가능)
1.에너지 구슬을 고른다. 번호를 x라고 함.(첫번째와 마지막은 못 고름)
2.x번째 에너지 구슬을 제거
3.W(x-1)*W(x+1)의 에너지를 모을 수 있다.
4.n을 1감소시키고 에너지구슬을 다시 1~n까지로 번호 매김.
n과 에너지구슬의 무게가 주어졌을때 모을수 있는
에너지의 최대값.

->n이 2가 될때까지 solve를 돌려야할듯.
ex) 1 2 3 4
3을 빼고 2*4를 모음
1 2 4
2를 뺴고 1*4를 모음
1 4
처음과 마지막 구슬만 남아서 더이상 못뺌.
총 덧셈 결과는 12.이렇게.
->계속 배열을 업데이트 해줘야하니까 ArrayList로 구현.

객체로 만든 변수는 무조건 새로 객체 생성 후 인자로 넘기기.

 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class 에너지모으기 {
    static int n;
    static ArrayList<Integer> max;

    static int solve(ArrayList<Integer> a){
        int m=a.size();
        if(m==2){
            return 0;
        }
        //2~n-1번째 구슬 없애고 그 인근 두개 합 곱한걸
        //sum에 더해서 재귀호출.
        int ans=0;
        for(int i=1;i<m-1;i++){
            int temp=a.get(i-1)*a.get(i+1);
            ArrayList<Integer> nextA=new ArrayList<>(a);
            nextA.remove(i);

            temp=temp+solve(nextA);
            if(ans<temp) ans=temp;
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        ArrayList<Integer> a=new ArrayList<>();
        Integer[] arr=new Integer[n];
        for(int i=0;i<n;i++){
            arr[i]=(Integer)sc.nextInt();
        }
        //for(int i=0;i<n;i++){
        //    a.add(arr[i]);
        //}
        a=new ArrayList<>(Arrays.asList(arr));

        System.out.println(solve(a));
    }
}
