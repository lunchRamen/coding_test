/*
입력받은 숫자들
1:우 cctv
2:좌우 cctv
3:상우 cctv
4:좌상우 cctv
5:상하좌우 cctv

중요점
cctv가 감시하는 방향을 "정수"형태로 나타내서, 방향벡터의 인덱스로 써서 정수 하나로
어떤 방향을 감시할지 나타내는 생각.

문제의 예시처럼 cctv가 감시하는 범위를 #으로 나타내어야한다는 강박관념
->이러면 cctv는 숫잔데, 감시범위는 문자여서 구현을 어떻게해야할지 꼬임.
->항상 가장 간단하게 구현하는 생각을 해보자.




 */

import java.util.*;

class CCTV{
    int x;
    int y;
    int type;
    int dir;

    public CCTV(int x, int y, int type) {
        this.x = x;
        this.y = y;
        this.type = type;
        this.dir = 0;
        //dir은 0 1 2 3으로 0 90 180 270도. cctv 기준 방향.
    }
}

public class 감시 {
    static int n,m;
    static int[][] a;
    static int[] dx={1,0,-1,0};
    static int[] dy={0,-1,0,1};
    //상 하 좌 우
    static void check(int[][] a,int[][] b,int x,int y,int dir){
        int n=a.length;
        int m=a[0].length;
        int i=x;
        int j=y;
        while(0<=i &&i<n && 0<=j && j<m){
            if(a[i][j]==6) break;
            b[i][j]=a[x][y];
            //cctv에 감시받으면 해당 cctv 숫자로 바꿔줌-> 나중에 return해줄때 b[i][j]가 0인 경우만
            //cnt+=1해서 return 해주면 됨. 굳이 문제처럼 #로 해서 문자로 나타내줘야한다는
            //강박관념때문에 int와 char형에서 구현을 고민하고 있었는데,
            //더 간단하게 구현하자는 중요점을 항상 기억해두면 될듯.

            i+=dx[dir];
            j+=dy[dir];
            //입력받은 기준방향으로만 쭉 뻗어나가게끔.
        }
    }
    static int go(int[][] a,ArrayList<CCTV> cctv,int idx){
        if(idx==cctv.size()){
            int n=a.length;
            int m=a[0].length;
            int[][] b=new int[n][m];
            for(int i=0;i<n;i++){
                for(int j=0;j<m;j++){
                    b[i][j]=a[i][j];
                }
            }
            for(CCTV c:cctv){
                int what=c.type;
                int x=c.x;
                int y=c.y;
                int dir=c.dir;
                if(what==1){
                    check(a,b,x,y,dir);
                    //한방향.
                }
                else if(what==2){
                    check(a,b,x,y,dir);
                    check(a,b,x,y,(dir+2)%4);
                    //양방향. 근데 다른방향이 180도 차이.
                }
                else if (what==3){
                    check(a,b,x,y,dir);
                    check(a,b,x,y,(dir+1)%4);
                    //두방향. 근데 방향이 90도차이.
                }
                else if(what==4){
                    check(a,b,x,y,dir);
                    check(a,b,x,y,(dir+1)%4);
                    check(a,b,x,y,(dir+2)%4);
                    //세방향. 시작부터 90도 180도.
                }
                else if(what==5){
                    check(a,b,x,y,dir);
                    check(a,b,x,y,(dir+1)%4);
                    check(a,b,x,y,(dir+2)%4);
                    check(a,b,x,y,(dir+3)%4);
                    //4방향 모두. 이래서 check를 돌려주는 횟수가 다름.
                }
            }
            int cnt=0;
            for(int i=0;i<n;i++){
                for(int j=0;j<m;j++){
                    if(b[i][j]==0) cnt+=1;
                }
            }
            return cnt;
        }
        int ans=100;
        for(int i=0;i<4;i++){
            cctv.get(idx).dir=i;//cctv 방향 설정
            int temp=go(a,cctv,idx+1);//후 재귀호출. idx는 cctv갯수만큼만 돌아가니까 상관 무.
            if(ans>temp) ans=temp;
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();

        a=new int[n][m];
        ArrayList<CCTV> cctv=new ArrayList<>();

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                a[i][j]= sc.nextInt();
                if(a[i][j]>=1 && a[i][j]<=5){
                    cctv.add(new CCTV(i,j,a[i][j]));
                }
            }
        }

        System.out.println(go(a,cctv,0));
    }
}
