import java.util.Scanner;

/*
N*M크기의 보드와 4개의 버튼으로 이루어진 게임.
보드는 1칸으로 이루어짐 각 칸은 벽이거나 비어있음.
두개의 빈칸에는 동전이 하나씩 있고, 위치는 다름
버튼은 왼 오 위 아래 4가지가 있음(4개의 버튼)
버튼을 누르면 두 동전이 버튼에 쓰여있는 방향으로
"동시에"이동.

조건
동전이 이동하려는 칸이 벽이면, 이동 안함
동전이 이동하려는 방향에 칸이 없으면, 보드 바깥으로 떨어짐
그 외에는 이동하려는 방향으로 한칸씩 이동.(이동하려는 칸에 동전이 있어도 이동)

두 동전 중 하나만 보드에서 떨어뜨리려면, 버튼을 최소 몇번 눌러야하는지.


***객체의 경우 재귀함수로 구현할때, 모든 함수에 객체가 동시에
업데이트 되므로, 새 객체를 만든다음에 재귀함수의 인자로 넘겨줘야함.
 */
class Pair2{
    int x;
    int y;
    public Pair2(int x,int y){
        this.x=x;
        this.y=y;
    }
    public Pair2(Pair2 pair){
        this.x=pair.x;
        this.y=pair.y;
    }
}
public class 두동전 {
    static int n,m;
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};

    static int solve(char[][] a,int buttonNum,Pair2 firstO,Pair2 secondO){
        if(buttonNum==11) return -1;
        boolean fall1=false;
        boolean fall2=false;
        if(firstO.x<0 || firstO.x>=n ||firstO.y<0 ||firstO.y>=m) fall1=true;
        if(secondO.x<0 || secondO.x>=n ||secondO.y<0 ||secondO.y>=m) fall2=true;
        if(fall1 && fall2) return -1;
        if(fall1 || fall2) return buttonNum;
        int ans=-1;
        for(int i=0;i<4;i++){
            int nx1=firstO.x+dx[i];
            int ny1= firstO.y+dy[i];
            int nx2= secondO.x+dx[i];
            int ny2=secondO.y+dy[i];
            Pair2 nextFirstO=new Pair2(firstO);
            Pair2 nextSecondO=new Pair2(secondO);
            if(0<= nx1 && nx1<n && 0<=ny1 &&ny1<m && a[nx1][ny1]=='#'){
                nextFirstO.x= firstO.x;
                nextFirstO.y= firstO.y;
            }
            else{
                nextFirstO.x=nx1;
                nextFirstO.y=ny1;
            }
            if(0<=nx2 && nx2<n && 0<=ny2 && ny2<m && a[nx2][ny2]=='#'){
                nextSecondO.x= secondO.x;
                nextSecondO.y= secondO.y;
            }
            else{
                nextSecondO.x=nx2;
                nextSecondO.y=ny2;
            }
            int temp=solve(a,buttonNum+1,nextFirstO,nextSecondO);
            if(temp==-1) continue;
            if(ans==-1 ||ans>temp) ans=temp;
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        char[][] a=new char[n][m];
//        for(int i=0;i<n;i++){
//            for(int j=0;j<m;j++){
//                a[i][j]=sc.next().charAt(j);
//            }
//        }
        Pair2 firstO=new Pair2(-1,-1);
        Pair2 secondO=new Pair2(-1,-1);
        for(int i=0;i<n;i++){
            a[i]=sc.next().toCharArray();
            for(int j=0;j<m;j++){
                if(a[i][j]=='o') {
                    if(firstO.x==-1){
                        firstO.x=i;
                        firstO.y=j;
                    }
                    else{
                        secondO.x=i;
                        secondO.y=j;
                    }
                    a[i][j]='.';
                }
            }
        }
        System.out.println(solve(a,0,firstO,secondO));
        //여기서 이제 버튼 횟수,벽,빈칸,동전을 고려해야함.
        //여기서 중요한 점은 방향 버튼을 눌렀을때 두 동전이 같은 방향으로 동시에 움직임.
        //그리고, 동전 두개가 동시에 떨어지면, 원하는 결과값이 아님.

    }
}
