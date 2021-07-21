
/*
단어 수학문제는 N개의 단어로 이루어짐. 각 단어는 대문자로만 구성. 각 대문자를 0~9까지 숫자중 하나로 바꿔서
N개의 수를 합하는 문제.
"같은 알파벳은 같은 숫자" "다른 알파벳은 다른 숫자"

->입력받은 알파벳에 숫자 0~9까지를 "중복없이" mapping해줘야함.
->입력이 10 이하니까 그냥 재귀 돌려도 됨.
->각 문자에 대해 0~9까지 돌려서 max와 비교 한 후, max보다 크면 갱신하는 형태로.

재귀 설계
break(return) point->재귀호출->원상복구

나는 보통의 문제처럼 '문자'로 풀려고 했는데,
String으로 받아서 중복 처리 후 순열을 돌리고 그 문자에 맞는 수를 더해주면 되는 문제.

 */

import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class 단어수학 {
    static int n;


    static boolean next_permutation(int[] a){
        int i=a.length-1;
        while(i>0 && a[i-1]>=a[i]){
            i-=1;
        }
        if(i<=0) return false;
        int j=a.length-1;
        while(a[j]<=a[i-1]){
            j-=1;
        }
        int temp=a[i-1];
        a[i-1]=a[j];
        a[j]=temp;

        j=a.length-1;
        while(i<j){
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
            i+=1;
            j-=1;
        }
        return true;
    }//순열 함수.
    //순열은 현재 집합의 수에서 다음 큰수(크면서 가장 작은수)를 찾는 과정
    //수의 역전관계를 찾고, 다음 바꿔줄 수(역전관계에 있는 수 보다 큰 수)를 찾고
    //그 사이의 모든 수를 역전시키면 됨.
    static int[] alpha=new int[256];
    //문자 배열의 인덱스에 숫자를 매핑시킬 배열.
    static int calc(String[] a,Character[] letters,int[] d){
        int m=letters.length;
        int sum=0;
        for(int i=0;i<m;i++){
            alpha[letters[i]]=d[i];
        }
        for(String s:a){
            int now=0;
            for(char x:s.toCharArray()){
                now=now*10+alpha[x];
            }//한 문자열 배열당 문자단위로 쪼개서 합을 구하는 과정.
            //alpha[x]는 문자열 s의 한 문자가 매핑된 숫자로 반환됨.(위의 for문때문에)
            sum+=now;
        }
        return sum;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        String[] a=new String[n];
        HashSet<Character> s=new HashSet<>();
        for(int i=0;i<n;i++){
            a[i]=sc.next();
            for(char x:a[i].toCharArray()){
                s.add(x);
            }
        }
        //줄단위로 입력받은뒤 중복 제거해서 s에 글자 단위로 넣기
        Character[] letters=s.toArray(new Character[s.size()]);
        //그렇게 넣은걸 문자객체 배열로 만들어서 다시 넣기
        int m=letters.length;
        int[] d=new int[m];
        //d는 문자랑 숫자 매핑해줄 배열
        for(int i=0;i<m;i++){
            d[i]=9-i;
        }
        Arrays.sort(d);
        int ans=0;
        do{
            int now=calc(a,letters,d);
            if(ans<now) ans=now;
        }while(next_permutation(d));
        System.out.println(ans);

    }
}
