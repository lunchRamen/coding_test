import java.util.*;

public class 숫자판점프 {
    static int[] dx={1,-1,0,0};
    static int[] dy={0,0,1,-1};
    static int[][] a;
    static HashSet<Integer> ans=new HashSet<>();
    static int sum=0;
    static void go(int x,int y,int num,int len){
        if(len==6){
            ans.add(num);
            return;
        }
        for(int k=0;k<4;k++){
            int nx=x+dx[k];
            int ny=y+dy[k];
            if(nx>=0 && nx<5 && ny>=0 && ny<5){
                go(nx,ny,num*10+a[nx][ny],len+1);
                //문자열로 나타내는 대신에, 원래 숫자의 x10하고 a[nx][ny]를 하는방식으로 자릿수를 지킴.
            }
        }
    }
    public static void main(String[] args) {
        a=new int[5][5];

        Scanner sc=new Scanner(System.in);

        for(int i=0;i<5;i++){
            for(int j=0;j<5;j++){
                a[i][j]=sc.nextInt();
            }
        }

        for(int i=0;i<5;i++){
            for(int j=0;j<5;j++){
                go(i,j,0,0);
            }
        }

        System.out.println(ans.size());

    }
}
