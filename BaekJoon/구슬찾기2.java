import java.util.Scanner;

/*
nxm직사각형 보드에 빨간구슬 1개 파란구슬 1개를 넣은 다음 "빨간 구슬"을 구멍으로 빼내는 놀이.
가장 바깥 행과 열은 모두 막혀있고 중력으로 위 아래 오른쪽 왼쪽으로 굴려서 빼내야함. 파란색은 빼내면 안됨.
각각의 동작에서 두 구슬은 연속적으로 움직임.(독립적x)
빨간색이 먼저 떨어지면 성공
파란색이 먼저 떨어지면 실패. 빨파 동시에 떨어져도 실패.
몇번만에 빨간 구슬을 빼낼 수 있는지 구하는 문제.

10번이하로 빼낼 수 있으면, 해당 숫자를, 10번을 넘으면 -1을 출력. 못빼내도 -1.

기울인다-> 벽에 부딪힐때까지 구슬이 가는것.
기울인 한턴에 같은 구슬이 빠진것도 동시에 떨어진걸로 판단.


#:막힘
.:빈칸(움직일수 있음)
#:벽(못움직임)
O:구멍
R:빨간구슬
B:파랑구슬

-> 입력받은 문자배열에 대해서
0,1,2,3 4진법으로 위 아래 왼쪽 오른쪽으로 설정해서 bitmask로 gen함수를 구현하고
이 함수가 최소횟수를 달성할 방향들로 구성되었는데 valid함수로 검사하고(같은방향 연속 2번 or 서로 반대방향)
이것도 통과했으면, 빨간구슬을 hole에 넣는 최소횟수를 반환하는 check함수로 값을 받아서 ans와 비교한 후 최소값이면 업데이트.
check함수의 경우 빨,파,구멍 위치를 찾고 dir에 들어있는 방향들로 움직이면서 cnt1개 늘리고, hole1=빨 hole2=파
빨간구슬과 파란구슬이 제대로 작동하는지 simulate함수를 구현해서 빨강구슬이 빠졌는지 확인해줌.(혹은 구슬 두개 모두 이동하지 않는지)
hole1만 true이면 cnt를 반환 아니면 -1반환.

simulate는 해당 구슬이 이동했는가? 구멍에 빠졌는가? 에 대한 검사를 구현해주는 함수.
x,y에 대해 nx ny를 dx dy를 더해서 구현.(k(방향))에 대한 인덱스로 이동.
moved가 false면 움직이지 않음. hole이 false면 구멍에 빠지지 않음.
check는 cnt값 반환.
 */
class Result{
    boolean moved,hole;
    int x,y;
    Result(boolean moved,boolean hole,int x,int y){
        this.moved=moved;
        this.hole=hole;
        this.x=x;
        this.y=y;
    }
}
public class 구슬탈출2 {
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,1,-1};//방향 벡터
    static final int LIMIT=10;
    static int[] gen(int k){//k를 4진법으로 변환해서 return
        int[] dir=new int[LIMIT];
        for(int i=0;i<LIMIT;i++){
            dir[i]=(k&3);
            k>>=2;
        }//bitmask bit연산하는 방식.
        //4진수 표현: 해당 수랑 3을 and연산 -> 나머지가 0~3으로 나옴. k를 2개씩 비트 shift->2의제곱씩이동.
        return dir;
    }
    static Result simulate(char[][] a,int k,int x,int y){
        int n=a.length;
        int m=a[0].length;
        if(a[x][y]=='.') return new Result(false,false,x,y);
        boolean moved=false;
        while(true){
            int nx=x+dx[k];
            int ny=y+dy[k];
            if(nx<0 || nx>=n || ny<0 || ny>=m){
                return new Result(moved,false,x,y);
            }//이거 없어도 문제는 풀 수 있음. 보드의 가장자리는 벽이라고 문제에 설명되어있으니까.
            char ch=a[nx][ny];
            if(ch=='#'){//벽일때 더이상 이동 못하니까 return
                return new Result(moved,false,x,y);
            }
            else if(ch=='R'|| ch=='B') return new Result(moved,false,x,y);//구슬일때도 그냥 return해줌.
            else if(ch=='.'){//두개의 문자를 바꿔줌 -> temp이용.
                char temp=a[nx][ny];
                a[nx][ny]=a[x][y];
                a[x][y]=temp;
                x=nx;
                y=ny;
                moved=true;//움직였다고 표시
            }
            else if(ch=='O'){//구멍일때 빈칸처리 후 return.
                a[x][y]='.';
                moved=true;
                return new Result(moved,true,x,y);//hole은 구멍인 경우에만 true로 return된다.
            }
        }
    }
    static int check(char[][] a,int[] dir){//보드배열과 dir로 입력받은 방향.(
        int n=a.length;
        int m=a[0].length;
        int hx=0;
        int hy=0;
        int rx=0;
        int ry=0;
        int bx=0;
        int by=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(a[i][j]=='O'){
                    hx=i;
                    hy=j;
                }
                else if(a[i][j]=='R'){
                    rx=i;
                    ry=j;
                }
                else if(a[i][j]=='B'){
                    bx=i;
                    by=j;
                }
            }
        }
        int cnt=0;
        for(int k:dir){
            cnt+=1;
            boolean hole1=false;
            boolean hole2=false;
            while(true){
                Result p1=simulate(a,k,rx,ry);
                rx=p1.x;
                ry=p1.y;
                Result p2=simulate(a,k,bx,by);
                bx=p2.x;
                by=p2.y;
                if(p1.moved==false && p2.moved==false) break;
                if(p1.hole) hole1=true;
                if(p2.hole) hole2=true;
            }//for문:구슬에 이동에 해당 검사.
            if(hole2) return -1;
            if(hole1) return cnt;//구멍에 빠진 구슬이 뭔지 검사.
        }
        return -1;
    }
    static boolean valid (int[] dir){//유효검사 같은방향 연속 2번 or 반대방향은 소용 없음.
        int l=dir.length;
        for(int i=0;i+1<l;i++){
            if(dir[i]==0 && dir[i+1]==1) return false;
            if(dir[i]==1 && dir[i+1]==0) return false;//0위 1 아래
            if(dir[i]==2 && dir[i+1]==3) return false;//2왼쪽 3오른쪽
            if(dir[i]==3 && dir[i+1]==2) return false;
            if(dir[i]==dir[i+1]) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        int n,m;
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        String[] map=new String[n];
        char[][] a=new char[n][m];
        for(int i=0;i<n;i++){
            map[i]=sc.next();
        }
        int ans=-1;
        for(int k=0;k<(1<<LIMIT*2);k++){//모든 k를 만듦. 4의 10승 -> 2의 20승이니까.
            int[] dir=gen(k);//k에 대한 모든 dir를 만들고
            if(!valid(dir)) continue;//dir가 유효한지(0,1,2,3으로만 이루어졌는지) 확인
            for(int i=0;i<n;i++){
                a[i]=map[i].toCharArray();
            }
            int cur=check(a,dir);//a배열에 dir방향으로 이동시켜서 빨간 구슬만 떨어지는 cnt값을 return받고
            if(cur==-1) continue;
            if(ans==-1 || ans>cur) ans=cur;//최소값이면 갱신한다.
        }
        System.out.println(ans);
    }
}
