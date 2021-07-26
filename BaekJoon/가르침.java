
/*
남극=antatica.

남극언어의 단어는 anta+XXXX+tica형태.
남극언어의 단어는 N개 있다고 가정.
K개의 글자를 가르칠수 있다고 가정.
->어떤 K개의 글자를 가르쳐야 학생들이 읽을수 있는 단어의 갯수가 최대가 되는지.

입력에서 N=3 K=6으로 받았을때(입력받을 단어의 갯수는 3개 가르칠수 있는 글자수는 6개)
ex)anta rc tica
   anta hello tica
   anta car tica
기본적으로 가르쳐야하는거 a,n,t,i,c ->5개.
이후에 1개를 더 가르칠수 있음
근데, c,a,는 이미 알고있으니 r을 하나 더 가르치면 2개의 단어를 알수 있다.-> 답 2출력

N<=50 k<=26(0도 가능)

내가 했던 풀이랑 같은점
2차원 문자배열로 받기보단 문자열로 받아서 작동함(자바가 문자열에 더 특화되어있으니까)
a,n,t,i,c에 해당하는 문자의 경우 따로 처리를 해줘서 count를 안하게끔.

내가 했던 풀이랑 다른점
문자를 아스키코드로 취급해서 index로 다뤘음.
->해당 문자에 항상 'a'를 빼주면, a:0~ z:26으로 매핑됨.
그래서, learn은 boolean 26개로 표현해서 해당 문자를 썼으면 true로 바꾸면 된다.
그래서, index가 26개로 찼으면 다 방문한거니까 count를 써줘서
count함수의 구현처럼 words의 모든 배열에 각 문자에 learn[x-'a']가 false이면넘어가고 true이면 cnt를 +1씩해서
cnt를 return 해주면 몇개의 문자를 썼는지 나온다.

k는 쓸 수 있는 단어의 갯수니까 k가 음수가 나오면 return 0으로 예외처리를 해주고,
index에 해당하는 숫자가 a,n,t,i,c에 해당하는 index이면 go(index+1,k,words)로 재귀
                                        하지 않는 index이면 go(index+1,k-1,words)로 재귀
                                        새로운 문자를 쓸때마다 쓸수있는 문자 k의 갯수를 하나씩 빼줘야함.

실수 했던부분
1.a n t i c에 해당하는 index는 true 재귀 false할 필요 없음.
2.a n t i c에 해당하는 재귀와 해당하지 않는 재귀에 대해 각각 if(ans<t1)을 해줘야함.
3.각 단어에 대해 learn[x-'a']가 하나라도 false가 있다면 그 단어를 배울수 없으므로 cnt+=1은 word의 모든 문자가
true인 경우에만 해줘야하기때문에 inner for문 바깥에 if(ok)를 만들어줘야함.

 */

import java.util.Scanner;

public class 가르침 {
    static boolean[] learn=new boolean[26];
    static int count(String[] words){
        int cnt=0;
        for(String word:words){
            boolean ok=true;
            for(char x:word.toCharArray()){
                if(!learn[x-'a']){
                    ok=false;
                    break;
                }
            }
            if(ok) cnt+=1;
        }
        return cnt;
    }
    static int go(int index,int k,String[] words){
        if(k<0) return 0;
        if(index==26){
            return count(words);
        }
        int ans=0;
        learn[index]=true;
        int t1=go(index+1,k-1,words);
        learn[index]=false;
        if(ans<t1) ans=t1;
        if(index!='a'-'a'&&index!='n'-'a'&&index!='t'-'a'&&index!='c'-'a'&&index!='i'-'a'){
            t1=go(index+1,k,words);
            if(ans<t1) ans=t1;
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt();
        String[] words=new String[n];
        for(int i=0;i<n;i++){
            words[i]=sc.next();
        }
        System.out.println(go(0,k,words));
    }
}
