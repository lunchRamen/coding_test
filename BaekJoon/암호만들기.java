import java.util.*;

/*
암호 만들기. 암호의 조건: 자음이 2개이상 모음이 1개이상 -> 길이는 3이상부터 가능
check 함수로 따로 뺌.
a e i o u 면 모음 +1 이외엔 자음+1해서 mo>=1 && ja>=2를 return.

go는 재귀함수로 만들건데 sort한 string 배열의 처음부터 해당배열 글자를 선택/선택 안함으로 진행
빈 문자열 password에 채워나가는데, password의 길이가 n이면 check함수를 돌려서 true인 경우 print해줌. 아니면 return
a.length(문자열의 길이)<=i면 범위 초과니까 return.
이외엔 go(n,a,password+a[i],i+1) go(n,a,password,i+1)로 i번째 인덱스 선택. 선택 안함 두개로 재귀 호출.

**c++과 자바의 차이점
자바는 foreach문을 쓰기 편리한데, char배열 for문으로 만들 수 없음.
charAt이나 문자열로 배열 만든 다음에, .toCharArray()로 문자로 만들어서 탐색.
그리고 배열에 변수 값을 넣어서 배열 만들수 있다.
sort할 때 null값이 들어있으면 nullpointerexception이 난다. 주의하자.

 */
public class 암호만들기 {
    static int l,c;

    public static boolean check(String password){
        int ja=0;
        int mo=0;
        for(char x:password.toCharArray()){
            if(x=='a'|| x=='e'|| x=='i'|| x=='o'||x=='u'){
                mo+=1;
            }
            else ja+=1;
        }
        return ja>=2 && mo>=1;
    }
    public static void go(int n,String[] a,String password,int i){
        if(password.length()==n){
            if(check(password)){
                System.out.println(password);
            }
            return;
        }
        if(i>=a.length) return;
        go(n,a,password+a[i],i+1);
        go(n,a,password,i+1);
    }
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        l=sc.nextInt();
        c=sc.nextInt();
        String a[]=new String[c];
        for(int i=0;i<c;i++){
            a[i]=sc.next();
        }
        Arrays.sort(a);

        go(l,a,"",0);
    }
}
