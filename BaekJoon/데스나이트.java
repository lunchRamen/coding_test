/*
체스에서 새로운 말인 데스나이트 개발.
데스나이트의 이동경로는 dx dy.

크기가 NxN인 체스판이 주어지고, 두칸이 주어졌을때
데스나이트가 한점에서 다른점으로 이동하는 최소횟수 구하기.(체스판 범위 내에서만 이동가능)

이동 불가능하면 -1 return.

while(!q.isEmpty())에서 검사해야될거
1.체스판 범위 내에 있느냐
2.방문한적 있느냐.

그리고 Pair의 경우 객체니까 항상 새로 할당해서 넘겨줘야하는거 주의.
 */

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Func{
    int x;
    int y;

    public Func(int x,int y) {
        this.x = x;
        this.y=y;
    }
}

public class 데스나이트 {
    static int[] dx={-2,-2,0,0,2,2};
    static int[] dy={-1,1,-2,2,-1,1};
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int x1=sc.nextInt();
        int y1=sc.nextInt();
        int x2=sc.nextInt();
        int y2=sc.nextInt();

        boolean[][] c=new boolean[n][n];
        int[][] dist=new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                dist[i][j]=-1;
            }
        }
        Func f1=new Func(x1,y1);
        //Func f2=new Func(x2,y2);

        Queue<Func> q=new LinkedList<>();
        q.add(f1);
        c[f1.x][f1.y]=true;
        dist[f1.x][f1.y]=0;

        while(!q.isEmpty()){
            Func f=q.remove();
            for(int i=0;i<6;i++){
                int nx=f.x+dx[i];
                int ny=f.y+dy[i];
                if(0<=nx && nx<n && 0<=ny && ny<n){
                    if(c[nx][ny]==false){
                        c[nx][ny]=true;
                        dist[nx][ny]=dist[f.x][f.y]+1;
                        Func newF=new Func(nx,ny);
                        q.add(newF);
                    }
                }
            }
        }

        System.out.println(dist[x2][y2]);


    }
}
