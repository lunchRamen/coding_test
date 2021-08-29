/*
연산자 우선순위
괄호 -> 곱 뺄 덧(여기 다 동일)

주어진 식은 괄호가 없는 형탠데, 괄호를 적절히 넣어 연산값의 최대값을 출력해주게끔.
n<=19라서 가능.

나눗셈 연산은 안나옴.

항상 올바른 수식이 주어지기때문에, 정수가 n개 있으면, 연산자는 n-1개가 있으므로
n은 항상 홀수로 주어짐.

->연산자가 우선순위를 만들어준다고 생각하고 문제를 풀면 됨.

이것도 비슷한 생각을 하긴 함. 괄호 연산을 할 연산자를 방문했다고 치면 되는데,
나는 앞뒤 숫자도 방문했다고 쳤고, 그 이후에 이 연산자를 이용해 계산한 결과를 어떻게 처리할지 몰라
답지를 봄.

그냥 연산한 결과를 앞 숫자에 넣고, 뒤에 0을 집어넣어주면 된다.(연산자는 +로 바꿔주고)

 */
import java.util.*;

class Term{
    int num;
    int op;
    Term(int num, int op) {
        this.num = num;
        this.op = op;
    }
}
public class 괄호추가하기 {
    static int n;
    static Term[] a;
    static boolean[] c;

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        a=new Term[n];
        String s=sc.next();
        for(int i=0;i<n;i++){
            if(i%2==0){//숫자의 경우
                a[i]=new Term(s.charAt(i)-'0',0);
            }
            else{//연산자의 경우 1은 덧 2는 뺄 3은 곱
                int op=1;
                if(s.charAt(i)=='-') op=2;
                else if(s.charAt(i)=='*') op=3;
                a[i]=new Term(0,op);
            }
        }
        int m=(n-1)/2;
        //배열을 쓰는게 아니라 그냥 비트마스크로 연산자 사용 여부를 확인.
        //문자열 길이가 N이면 숫자의 갯수는 n+1/2 연산자의 갯수는 n-1/2이기때문에.
        int ans=-2147483648;
        for(int i=0;i<(1<<m);i++){
            boolean ok=true;
            for(int j=0;j<m-1;j++){
                if((i&(1<<j))>0 && (i&(1<<(j+1)))>0 ){
                    /*
                    비트마스크로 i를 0~511까지 진행. (2진법으로 계산됨)
                    그래서 j for문을 하나 더 돌려서 숫자 i에 대해 각 비트가 연산자 사용 여부라서
                    i번째 숫자에서 j번째 bit와 j+1번째 bit를 같이 사용하는건 피하게끔 먼저 조치.
                     */
                    ok=false;
                }
            }
            if(!ok) continue;//이래서 밑에 코드 건너뛰게끔.
            Term[] b=new Term[n];
            for(int j=0;j<n;j++){
                b[j]=new Term(a[j].num,a[j].op);//a는 객체라서 반복문 안에서 쓸수 있게끔 새로 복사.
            }
            for(int j=0;j<m;j++){
                if((i&(1<<j))>0){//계산 for문 둘중 첫번째의 차이점. 위에
                    //i for문에서 숫자 i에 대해서 연산자 기준 괄호 사용 여부가 정해지기에
                    //첫번째 계산 for문엔 괄호로 간주되어 먼저 계산되어야하는 것들 먼저 연산 해준다.
                    int k=2*j+1;
                    //j가 m까지이고 m은 (n-1)/2라서 b배열에 실제 접근할 인덱스 사용은
                    //위에걸 n으로 만들어줘야해서 k는 2*j+1이 된다.
                    if(b[k].op==1){
                        b[k-1].num+=b[k+1].num;
                        b[k+1].num=0;
                    }
                    else if(b[k].op==2){
                        b[k-1].num-=b[k+1].num;
                        b[k+1].num=0;
                        b[k].op=1;
                    }
                    else if(b[k].op==3){
                        b[k-1].num*=b[k+1].num;
                        b[k+1].num=0;
                        b[k].op=1;
                    }
                }
            }
            int res=b[0].num;
            for(int j=0;j<m;j++){
                //그다음 이제 그냥 돌려서 res에 숫자들 연산해줌.
                int k=2*j+1;
                if(b[k].op==1){
                    res+=b[k+1].num;
                }
                else if(b[k].op==2){
                    res-=b[k+1].num;
                }
                else if(b[k].op==3){
                    res*=b[k+1].num;
                }
            }
            if(ans<res) ans=res;
        }
        System.out.println(ans);

    }
}
