import java.util.*;

public class TwoDots {
    static char[][] a;
    static boolean[][] check;
    static int[][] dist;
    static int n,m;
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,1,-1};

    public static boolean go(int x,int y,int cnt,char color){
        //dfs가 x,y를 방문했을때 현재까지 같은색으로 연결된 점의 갯수를 cnt로 두고, 색의 색깔을 color로 둬서 구현.
        if(check[x][y]){
            if(cnt-dist[x][y]>=4){
                return true;
            }
            else{
                return false;
            }
        }
        check[x][y]=true;
        dist[x][y]=cnt;
        //해당 정점을 방문한 경우 사이클의 조건(연결된 점 4개이상)이면 true를 return.
        //아니면 해당 점을 방문한걸로 표시하고, 해당 점까지의 거리는 cnt로 표시.
        for(int k=0;k<4;k++){
            //다음 go 재귀 돌리기 위해 인접한 4개의 칸을 for문으로 돌림.(색깔이 같은 다음칸 찾기)
            int nx=x+dx[k];
            int ny=y+dy[k];
            if(0<=nx && nx<n && 0<=ny && ny<m){
                if(a[nx][ny]==color){//n m범위 내에있고 색이 같다면
                    if(go(nx,ny,cnt+1,color)) {//nx ny의 점에대해 go를 재귀. cnt를 1 올려준 상태에서.
                        //이렇게 재귀하면 위에 코드가 먼저 돌아가서 cnt-dist[nx][ny]가 4이상인 경우에만 true를
                        //return 해주므로, 이경우 끝남.
                        return true;
                    }
                }
            }
        }
        return false;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        a=new char[n][m];
        check=new boolean[n][m];
        for(int i=0;i<n;i++){
            a[i]=sc.next().toCharArray();
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(check[i][j]) continue;
                dist=new int[n][m];
                boolean ok=go(i,j,1,a[i][j]);
                if(ok){
                    System.out.println("Yes");
                    System.exit(0);
                }
            }
            //for문에서는 모든점에대해 go함수를 돌려서 dist를 갱신하고, dist가 4이상=사이클 존재니까 그걸 분기로
            //Yes,No를 구분해서 출력.
        }
        System.out.println("No");
    }
}
