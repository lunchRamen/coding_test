/*
바이러스 유출. 확산을 막기위해 연구소에 벽 설치 예정.

연구소 크기:NxM
각 칸의 의미
0:빈칸 1:벽 2:바이러스

바이러스는 상하좌우로 퍼져나감.
세울수 있는 벽의 갯수는 3개.(고정)

1.벽 3개 세우고,
2.바이러스가 최대로 퍼졌을때 0의 최대 갯수를 return.

조건들
바이러스가 위치한 칸의 갯수는 2~10개.

배열로 만들어서 바이러스 있는 칸의 좌표를 전달해주는걸로.

바이러스는 NxM중 한칸에 설정 X3개->NM의 세제곱
+BFS or DFS (NM) -> NM의 네제곱.


설계
3중 for문으로 NxM 돌면서
0(빈칸)인 곳들 중 3개를 골라서 벽으로 만들고, bfs를 돌리고, 돌린값이 ans보다 크면 갱신하고, 다시 원상태로 복구함

bfs
b배열에 a배열을 복사하고
바이러스가 있는 칸은 q에 더해놓음.
그리고 큐가 빌때까지 remove하면서 상하좌우로 빈칸인 경우 바이러스를 퍼트리고, q에 다시 add
후에 NxM에 대해 for문을 돌려서 0인것만 cnt+=1해서 cnt를 return해주면,

3중 for문으로 빈칸이 벽으로 변신한 상태의 연구소에서, bfs를 돌려서 바이러스가 최대한 퍼져 나갔을때
남은 빈칸의 갯수를 ans와 비교해서 갱신해주는 프로그램 작성 완료.
 */
class Func{
    int x;
    int y;

    public Func(int x,int y) {
        this.x = x;
        this.y=y;
    }
}
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;


public class 연구소 {
    static int n,m;
    static int[][] a=new int[10][10];
    static int[][] b=new int[10][10];
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,1,-1};

    static int bfs(){
        Queue<Func> q=new LinkedList<>();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                b[i][j]=a[i][j];
                if(b[i][j]==2){
                    q.add(new Func(i,j));
                }
            }
        }
        while(!q.isEmpty()){
            Func f=q.remove();
            int x=f.x;
            int y=f.y;
            for(int k=0;k<4;k++){
                int nx=x+dx[k];
                int ny=y+dy[k];
                if(0<= nx && nx<n && 0<=ny && ny<m){
                    if(b[nx][ny]==0){
                        b[nx][ny]=2;
                        q.add(new Func(nx,ny));
                    }
                }
            }
        }
        int cnt=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(b[i][j]==0){
                    cnt+=1;
                }
            }
        }
        return cnt;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        a=new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                a[i][j]=sc.nextInt();
            }
        }
        int ans=0;
        for(int x1=0;x1<n;x1++){
            for(int y1=0;y1<m;y1++){
                if(a[x1][y1]!=0) continue;
                for(int x2=0;x2<n;x2++){
                    for(int y2=0;y2<m;y2++){
                        if(a[x2][y2]!=0) continue;
                        for(int x3=0;x3<n;x3++){
                            for(int y3=0;y3<m;y3++){
                                if(a[x3][y3]!=0) continue;
                                if(x1==x2 && y1==y2) continue;
                                if(x1==x3 && y1==y3) continue;
                                if(x2==x3 && y2==y3) continue;
                                a[x1][y1]=1;
                                a[x2][y2]=1;
                                a[x3][y3]=1;
                                int cur=bfs();
                                if(ans<cur) ans=cur;
                                a[x1][y1]=0;
                                a[x2][y2]=0;
                                a[x3][y3]=0;
                            }
                        }
                    }
                }
            }
        }
        System.out.println(ans);
    }
}
