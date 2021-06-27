import java.util.*;

/*
NXM 격자판에 값들 입력.
k개를 고를건데, 고르는 칸들은 인접하면 안됨(인접:상 하 좌 우)
최대값을 ans에 넣고 출력.

배열판 a랑 해당 칸을 방문했는지 확인하는 c
인접한걸 확인해줄 방향벡터 dx dy
go함수는 선택한 칸 갯수, 합계로 진행되고 재귀로 호출.
cnt==k면 ans<sum인경우에 ans=sum으로 갱신 후 return
아니라면,
nxm 칸 모두 돎. 근데 if(c[i][j])로 방문했는지 확인해서 방문했으면 continue해서 다음칸으로
만약 방문 안했다면 boolean변수 ok를 만들어서
방향벡터로 nx, ny만든 다음 nx ny가 n과 m범위 이내고 c[nx][ny]가 방문한 상태라면 ok를 false로 만듬.

ok가 true인 경우.-> c[i][j]도 방문 안했고, 방향벡터로 인접한 점도 방문이 안됐으면, 해당 점을 선택해도 괜찮다.
->c[i][j]를 true로 놓고
go(cnt+1,sum+a[i][j])로 재귀호출함.
그다음 c[i][j]는 다시 false로 만듬. 그래야 cnt==k까지 가서 재귀가 끝났을때 2중 for문의 다음 시작점에서 시작할 때
c[i][j]의 방문여부를 초기화 해줄수 있다.
 */
public class NM과K1 {
    static int n,m,k;
    static int ans=0;
    static int[][] a=new int[10][10];
    static boolean[][] c= new boolean[10][10];
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};
    static void go(int cnt,int sum){
            if(cnt==k){
                if(ans<sum) ans=sum;
                return;
            }
            for(int i=0;i<n;i++){
                for(int j=0;j<m;j++){
                    if(c[i][j]) continue;
                    boolean ok=true;
                    for(int x=0;x<4;x++){
                        int nx=i+dx[x];
                        int ny=j+dy[x];
                        if(0<=nx && nx<n && 0<=ny && ny<m){
                            if(c[nx][ny]) ok=false;
                        }
                    }
                    if(ok){
                        c[i][j]=true;
                        go(cnt+1,sum+a[i][j]);
                        c[i][j]=false;
                    }
                }
            }
        }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        k=sc.nextInt();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                a[i][j]=sc.nextInt();
            }
        }
        go(0,0);
        System.out.println(ans);
    }
}
