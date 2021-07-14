import java.util.Scanner;

/*
N*N 체스판 위에 퀸 N개를 서로 공격할 수 없게 하는 경우의 수를 구하는 문제
ex) 8*8체스판의 경우 퀸 8개를 서로 공격할수 없게 만드는 경우의 수 -> 92개.

백트랙킹.
기본:brute force.
근데 재귀 호출시에 원하는 조건 만족하면 return해서 함수호출 중단.
재귀 호출시 if문으로 재귀할지말지 결정함.

Q을 공격할수 없게 둘수 있는 경우의 수
-> 같은줄(가로,세로,대각선)에 못놓음.

가로(퀸을 선택한곳과 같은 행)->한 행에 놓을수 있는 Q 1개.
세로(퀸을 선택한곳과 같은 열)->한 열에 놓을수 있는 Q 1개.

대각선(퀸을 선택한곳과 i-1 j-1 i-2 j-2..
                       i+1 j+1 i+2 j+2..


 */
public class NQueen {
    static boolean check(int row,int col){
        for(int i=0;i<n;i++){
            if(i==row) continue;
            if(a[i][col]) return false;
            //같은 열에 true=Q이 존재하면 false를 return해서 재귀호출 안되게끔.
        }
        int x=row-1;
        int y=col-1;
        while(x>=0 && y>=0){
            if(a[x][y]==true) return false;
            x-=1;
            y-=1;
        }
        //왼쪽 위 대각선. x와 y가 0이될때까지 왼쪽 위 대각선 타고 올라가서
        //Q이 있으면 false return
        x=row-1;
        y=col+1;
        while(x>=0 && y<n){
            if(a[x][y]==true) return false;
            x-=1;
            y+=1;
        }
        //오른쪽 위.
        return true;
    }
    //위의 문제에서 check 구현시,모든 칸에 대해서 열,대각선2개 검사.
    static void calc(int row){
        if(row==n) ans+=1;
        for(int col=0;col<n;col++){
            a[row][col]=true;
            if(check(row,col)) calc(row+1);
            //row행의 col열에 Q을 놓았을때,이전 Q과 공격하는 배치인지 검사하는 함수.
            //check는 0~row까지만 검사하면 된다.
            a[row][col]=false;
        }
    }
    static int n;
    static boolean[][] a;
    static int ans=0;
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        a=new boolean[15][15];
        calc(0);
        System.out.println(ans);
    }
}
