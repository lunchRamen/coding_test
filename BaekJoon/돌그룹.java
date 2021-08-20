import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Three{
    int x;
    int y;
    int z;

    public Three(int x,int y,int z) {
        this.x=x;
        this.y=y;
        this.z=z;
    }

}
/*
이 문제에서 내가 잘못 생각 했던 점
1.bfs에서 check함수 없이 bfs를 돌렸던 점.(이러면 중복 제거가 안되어 무조건 메모리 초과남)
2.check의 경우 수의 최대범위라 1500까지 가능한데, 이걸 내가 한것처럼 3차원으로 다루면 메모리 초과가 남.
sum=x+y+z로 두고 두개만 호출한 다음, check배열을 2차원으로 구현해야했음.
그럼 그룹 2개만 비교해서 안되지 않나? 하는데 결론적으로 돌그룹의 이동은 2개의 그룹끼리 이동이 일어나는 것이고,
x,y,z 세 그룹의 모든 이동이 끝났다면
check[sum/3][sum/3]이 true이면 끝날 일이다.
3차원을 2차원으로 표현하기 위해선
a={x,y,sum-x-y}로 sum을 통한 z표현이 있고,
이후 a[i]<a[j]경우에 대해
돌그룹 이동 이후 재귀호출을 해주면 된다.
항상 첫 두 그룹 재귀를 해주면, 2중 for문으로 모든 돌그룹 순서쌍을 비교하고 대소가 다른경우 재귀해주기때문에, 이렇게 해주면 끝.
*/

public class 돌그룹 {
//    public static void main(String[] args) {
//        int x,y,z;
//        Scanner sc=new Scanner(System.in);
//        x=sc.nextInt();
//        y=sc.nextInt();
//        z=sc.nextInt();
//
//
//        Three t=new Three(x,y,z);
//
//        Queue<Three> q=new LinkedList<>();
//
//        q.add(t);
//        if((x+y+z)%3!=0) System.out.println(0);
//        else {
//            while (!q.isEmpty()) {
//                Three temp = q.remove();
//                int[] a = {temp.x, temp.y, temp.z};
//                Arrays.sort(a);
//                if (a[0] == a[1] && a[0] == a[2]) {
//                    System.out.println(1);
//                    break;
//                } else {
//                    int nx1 = a[0] + a[0];
//                    int ny1 = a[1] - a[0];
//                    int nz1 = a[2];
//                    q.add(new Three(nx1, ny1, nz1));
//                    int nx2 = a[0] + a[0];
//                    int ny2 = a[1];
//                    int nz2 = a[2] - a[0];
//                    q.add(new Three(nx2, ny2, nz2));
//                    int nx3 = a[0];
//                    int ny3 = a[1] + a[1];
//                    int nz3 = a[2] - a[1];
//                    q.add(new Three(nx3, ny3, nz3));
//                }
//            }
//        }
//    }
public static int sum=0;
    public static boolean[][] check=new boolean[1501][1501];
    public static void go(int x,int y){
        if(check[x][y]) return;
        check[x][y]=true;
        int[] a={x,y,sum-x-y};
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                if(a[i]<a[j]){
                    int[] b={x,y,sum-x,y};
                    b[i]+=a[i];
                    b[j]-=a[i];
                    go(b[0],b[1]);
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int z = sc.nextInt();
        sum = x + y + z;
        if (sum % 3 != 0) {//sum이 3의배수가 아니면 정답이 될 수 없음
            System.out.println(0);
            System.exit(0);
        }
        go(x, y);
        if (check[sum / 3][sum / 3]) {
            System.out.println(1);
        } else System.out.println(0);
    }
}
