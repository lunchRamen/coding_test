/*
십자가는 가운데에 '*'가 있고, "상하좌우 방향으로 모두 같은 길이"의 '*'가 있는 모양이다.
십자가의 크기는 가운데를 중심으로 상하좌우 방향으로 있는 '*'의 개수이다. 십자가의 크기는 1보다 크거나 같아야 한다.

아래 그림은 크기가 1, 2, 3인 십자가이고, 빈 칸은 '.'이다.

              ...*...
      ..*..   ...*...
.*.   ..*..   ...*...
***   *****   *******
.*.   ..*..   ...*...
      ..*..   ...*...
              ...*...
크기가 N×M이고, '.'과 '*'로 이루어진 격자판이 주어진다.
이때, 십자가만을 이용해서 격자판과 같은 모양을 만들 수 있는지 구해보자.
십자가는 서로 겹쳐도 된다. 사용할 수 있는 십자가의 개수는 N×M이하이어야 한다.
격자판의 행은 위에서부터 1번, 열은 왼쪽에서부터 1번으로 번호가 매겨져 있다.
 */

/*

 */

import java.lang.reflect.Array;
import java.util.*;
public class 십자가찾기 {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n,m;
        n=sc.nextInt();
        m=sc.nextInt();

        boolean[][] check=new boolean[n][m];
        char[][] a=new char[n][m];

        for(int i=0;i<n;i++){
            a[i]=sc.next().toCharArray();
        }
        ArrayList<Integer> ans_x=new ArrayList<>();
        ArrayList<Integer> ans_y=new ArrayList<>();
        ArrayList<Integer> ans_l=new ArrayList<>();

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(a[i][j]=='*'){
                    int l=0;//십자가의 크기
                    for(int k=1;;k++){//k를 증가시키면서 위치가 존재하고 *이면 십자가 크기를 늘림.
                        if(i+k<n && i-k>=0 && j+k<m && j-k>=0){
                            if(a[i+k][j]=='*' && a[i-k][j]=='*' && a[i][j+k]=='*' && a[i][j-k]=='*'){
                                l=k;
                            }
                            else break;
                        }
                        else break;
                    }
                    if(l>0){
                        ans_x.add(i+1);
                        ans_y.add(j+1);
                        ans_l.add(l);
                        check[i][j]=true;
                        for(int k=1;k<=l;k++){
                            check[i+k][j]=true;
                            check[i-k][j]=true;
                            check[i][j+k]=true;
                            check[i][j-k]=true;
                        }
                    }
                }
            }
        }
        //여기까지 n m 보드판을 돌면서 십자가가 생길수 있는 모든 경우에 대해 십자가에 대한 정보들을 ans_x,y,l에 저장하고
        //방문여부도 체크해둠. 이러면 for문 자체가 n*m만큼만 도니까 십자가의 최대갯수도 n*m개까지만 나옴
        //->큰 십자가 밑에 작은 십자가의 중복을 방지해 줄 수 있다.

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(a[i][j]=='*' && check[i][j]==false){//불가능한 경우
                    System.out.println(-1);
                    System.exit(0);
                }
            }
        }
        System.out.println(ans_x.size());
        for(int i=0;i<ans_x.size();i++){
            int x=ans_x.get(i);
            int y=ans_y.get(i);
            int l=ans_l.get(i);
            System.out.println(x+" "+y+" "+l);
        }
    }
}
