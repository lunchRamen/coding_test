import java.util.Scanner;

/*
스도쿠
9X9 판때기 주어짐
가로,세로에 1~9까지 중복없이 있어야됨
각 3X3 판때기에도 1~9까지 중복 없이 있어야됨.

입력으로 받은 0=넣어야할 숫자로 생각.

경우의 수가 너무 많아서 백트랙킹으로 풀어야함.
NQueen처럼 풀어야함.
어떤 칸에 대해서 열,행,대각선에 대해서 풀어야함.
행:1~9 1개씩
열:1~9 1개씩
3X3:1~9 1개씩.

go(z):z번째 칸을 채우는 함수.

c[i][j]->i행에 숫자 j가 있으면 true
c2[i][j]->i열에 숫자 j가 있으면 true
c3[i][j]->i번 작은 정사각형에 j가 있으면 true.

x행 y열로 했을때
3X3 정사각형을 큰 행 큰 열로 볼수 있음
0 1 2행 0 1 2열이 있는.(3x3이 하나의 행,열)

정답을 찾은 경우:z가 81인 경우.(모든 칸을 다 돌았을때)

다음:빈칸 1~9를 넣어서 다음칸 진행
     수 있으면 아무것도 안하고 다음칸 진행.

brute force에서 중요한점
재귀호출 할때
배열을 바꿀수 있는 조건 준비
배열을 바꿀 호출
배열을 다시 원상복구


 */
public class 스도쿠 {
    public static int square(int x,int y){
        return (x/3)*3+(y/3);
    }
    public static boolean solve(int z,int[][] a,boolean[][] c,boolean[][] c2,boolean[][] c3) {
        if (z == 81) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print(a[i][j] + " ");
                }
                System.out.println();
            }
            return true;
        }
        int x = z / n;//행
        int y = z % n;//열
        if (a[x][y] != 0) {
            return solve(z + 1, a, c, c2, c3);//a[x][y]에 담긴값이 0이 아니면 다음 index로 진행
        } else {//0이면 아래 과정 진행
            for (int i = 1; i <= 9; i++) {
                if (c[x][i] != true && c2[y][i] != true && c3[square(x, y)][i] != true) {
                    c[x][i] = true;
                    c2[y][i] = true;
                    c3[square(x, y)][i] = true;

                    a[x][y] = i;
                    if (solve(z + 1, a, c, c2, c3)) {
                        return true;
                    }
                    a[x][y] = 0;
                    c[x][i] = false;
                    c2[y][i] = false;
                    c3[square(x, y)][i] = false;
                }
            }
            return false;
        }
    }
    static int n=9;

    public static void main(String[] args) {
        int [][] a=new int[9][9];
        boolean [][] c=new boolean[9][10];
        boolean [][] c2=new boolean[9][10];
        boolean [][] c3=new boolean[9][10];
        Scanner sc=new Scanner(System.in);
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                a[i][j]=sc.nextInt();
                if(a[i][j]!=0){
                    c[i][a[i][j]]=true;
                    c2[j][a[i][j]]=true;
                    c3[square(i,j)][a[i][j]]=true;
                    //c:i행에 a[i][j]에 해당하는 숫자를 true로
                    //c2:j열에 a[i][j]에 해당하는 숫자를 true
                    //c3:3x3정사각형에 a[i][j]를 true로.
                }
            }
        }
        solve(0,a,c,c2,c3);
    }
}
