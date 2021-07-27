import java.util.Scanner;

/*
방법의 수 : 4의 5승 -> brute force로 구현 가능.
방법의 수를 만들고, 시뮬레이션 해주면 됨.

방향 지정하면-> 끝까지 올라가서 같은수를 만나면 수를 합침.
한번 합쳐진 수는, 그 턴에서 다시 합쳐질 수 없다.
해당 방향 이동 역순으로 합쳐진다.

같은방향으로 이동하는게 의미를 가짐. 반대방향도 의미를 가짐.

모든 경우의 수에 대해 방향배열을 생성 하고
그 방향배열과 입력받은 숫자 배열을 인자로 check함수 돌린 return값을 ans에 받아서 최대값 update

check함수:보드 a를 dir방향대로 이동.

check함수엔 int형 배열 a 복사본 d, 합쳐진 적이 있는지 확인하는 merged배열을 boolean형으로.
(규칙의 한번 합친건 그 턴에서 다시 합칠수 없고, 위의 숫자부터 합쳐줘야한다는걸 확인하는 용도로)

dir에 해당하는 원소들이 0,1,2,3인지 확인후
0(아래) 1(위) 2(왼) 3(오)로 이동하는것에 대한 처리 구현.
이때, 합쳐지는건 방향의 역순으로 처리해줘야함.
0의 경우 열에 대한 outer for문 시작이 n-2인데 그 이유가 위에 나온 역순 합체때문이고,
n-1이 아니고 n-2부터 시작하는 이유는 맨밑(n-1)은 어차피 안움직이니까.
0~n-1이 아니라 n-2~0으로 구현하는 이유.

해당 수가 없으면 넘어가고
해당 수는 있는데 다음수가 없다면, 밑으로 내려가고 원래 있던곳을 0으로.
해당 수와 다음 수가 모두 있고, 값도 같다면 -> 그 두수가 합쳐진적 있는지 merged확인하고
밑에수에다가 *2해주고, 합쳐진적 있다고 true로 바꿔주고 원래 수엔 0을 넣어준다.
1,2,3도 똑같이 해주면 됨.

그다음 o

 */
public class easy2048 {
    static final int LIMIT=5;
    static int[] gen(int k){
        int[] a=new int[LIMIT];
        for(int i=0;i<LIMIT;i++){
            a[i]=(k&3);
            k>>=2;
        }
        return a;
    }
    static int check(int[][] a,int[] dirs){
        int n=a.length;
        int[][] d=new int[n][n];
        boolean[][] merged=new boolean[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                d[i][j] = a[i][j];
            }
        }

        for(int dir:dirs){
            boolean ok=false;
            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    merged[i][j]=false;
                }
            }
            while(true){
                ok=false;
                if(dir==0){
                    for(int i=n-2;i>=0;i--){
                        for(int j=0;j<n;j++){
                            if(d[i][j]==0){
                                continue;
                            }
                            if(d[i+1][j]==0){
                                d[i+1][j]=d[i][j];
                                merged[i+1][j]=merged[i][j];
                                d[i][j]=0;
                                ok=true;
                            }
                            else if(d[i+1][j]==d[i][j]){
                                if(merged[i][j]==false && merged[i+1][j]==false){
                                    d[i+1][j]*=2;
                                    merged[i+1][j]=true;
                                    d[i][j]=0;
                                    ok=true;
                                }
                            }
                        }
                    }
                }
                else if(dir==1){
                    for(int i=1;i<n;i++){
                        for(int j=0;j<n;j++){
                            if(d[i][j]==0) continue;
                            if(d[i-1][j]==0){
                                d[i-1][j]=d[i][j];
                                merged[i-1][j]=merged[i][j];
                                d[i][j]=0;
                                ok=true;
                            }
                            else if(d[i-1][j]==d[i][j]){
                                if(merged[i-1][j]==false && merged[i][j]==false){
                                    d[i-1][j]*=2;
                                    merged[i-1][j]=true;
                                    d[i][j]=0;
                                    ok=true;
                                }
                            }
                        }
                    }
                }
                else if(dir==2){
                    for(int j=1;j<n;j++){
                        for(int i=0;i<n;i++){
                            if(d[i][j]==0) continue;
                            if(d[i][j-1]==0){
                                d[i][j-1]=d[i][j];
                                merged[i][j-1]=merged[i][j];
                                d[i][j]=0;
                                ok=true;
                            }
                            else if(d[i][j-1]==d[i][j]){
                                if(merged[i][j]==false && merged[i][j-1]==false){
                                    d[i][j-1]*=2;
                                    merged[i][j-1]=true;
                                    d[i][j]=0;
                                    ok=true;
                                }
                            }
                        }
                    }
                }
                else if(dir==3){
                    for(int j=n-2;j>=0;j--){
                        for(int i=0;i<n;i++){
                            if(d[i][j]==0) continue;
                            if(d[i][j+1]==0){
                                d[i][j+1]=d[i][j];
                                merged[i][j+1]=merged[i][j+1];
                                d[i][j]=0;
                                ok=true;
                            }
                            else if(d[i][j+1]==d[i][j]){
                                if(merged[i][j]==false && merged[i][j+1]==false){
                                    d[i][j+1]*=2;
                                    merged[i][j+1]=true;
                                    d[i][j]=0;
                                    ok=true;
                                }
                            }
                        }
                    }
                }
                if(ok==false) break;
            }
        }
        int ans=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(ans<d[i][j]) ans=d[i][j];
            }
        }
        return ans;
    }

    public static void main(String[] args) {

        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        int[][] a=new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                a[i][j]=sc.nextInt();
            }
        }//n이랑 nXn배열에 숫자까지 입력 완료.

        int ans=0;
        for(int k=0;k<(1<<(LIMIT*2));k++){
            int[] dir=gen(k);
            int cur=check(a,dir);
            if(ans<cur) ans=cur;
        }
        System.out.println(ans);
    }
}
