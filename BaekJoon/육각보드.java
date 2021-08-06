/*
사각 보드에서 dx dy방향벡터를 이용해서 다음 nx ny 구한거처럼
육각 보드에서 dx dy방향벡터를 설정 후 다음 nx ny를 조건에 따라 구해줘서 재귀 호출하면 됨.

색칠할때 나눌 조건

a[x][y]='X'인 원소들이 모두 인접하지 않으면 정답은 1.
 */

import java.util.Scanner;

public class 육각보드 {
    static int[] dx={-1,-1,0,0,1,1};
    static int[] dy={0,1,-1,1,-1,0};
    static char[][] a;
    static int[][] c;
    static int n;
    static int ans;
    static void go(int x,int y,int cnt){
        c[x][y]=cnt;
        ans=Math.max(ans,1);
        //함수가 호출된거 자체가 색칠할 칸이 있어서 최소 1이라 그걸 설정해줌.
        for(int k=0;k<6;k++){
            int nx=x+dx[k];
            int ny=y+dy[k];
            if(0<=nx && nx<n && 0<=ny &&ny<n){//범위 안에 있고
                if(a[nx][ny]=='X'){//다음 칸도 색칠해야되는 경우
                    if(c[nx][ny]==-1){//그 칸이 색칠되지 않았으면
                        go(nx,ny,1-cnt);//인접한 칸이 존재하는 경우.
                        //c[x][y]를 cnt로 넣는데 cnt에 1을 넣음.-> 다른색을 넣음.
                    }
                    ans=Math.max(ans,2);//그때는 이제 색깔이 2개 들어감.
                    if(c[nx][ny]==cnt){
                        ans=Math.max(ans,3);//다음 정점이 이미 색칠 되어짐.->그색과 다른 색을 칠해야되니까 3.
                    }
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        a=new char[n][n];
        c=new int[n][n];
        for(int i=0;i<n;i++){
            a[i]=sc.next().toCharArray();
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                c[i][j]=-1;
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(a[i][j]=='X' && c[i][j]==-1){//색칠되어야 하는 칸인데 아직 색칠을 안했으면 재귀 시작.
                    go(i,j,0);
                }
            }
        }
        System.out.println(ans);
    }
}
