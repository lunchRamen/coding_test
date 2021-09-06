/*
N명의 사람이 있고, 여기서 세 사람 A, B, C를 고르려고 한다. 세 사람은 모두 친구여야 한다.

세 사람을 고르는 방법은 매우 많이 있을 수 있다.
이때, A의 친구 수 + B의 친구 수 + C의 친구 수가 최소가 되어야 한다.
친구 수의 합을 계산할 때, 세 사람은 빼고 계산해야 한다.
즉, A의 친구 수를 계산할 때, B와 C는 빼고 계산해야 하고,
B의 친구 수를 계산할 때는 A와 C, C의 친구 수를 계산할 때는 A와 B를 빼고 계산해야 한다.
 */

/*
나는 처음에 치킨배달 문제처럼 Pair클래스로 따져서, 문제를 풀려고했는데, 원하는대로 안됨.
순열은 n!문제라 애초에 n이 너무 커서 쓸 수 없었음-> 다른 문제풀이 방법을 생각해야 했음.

그냥 a를 boolean으로 두고, true=친구 false=친구 x로 두고 풀면, n제곱 +mn으로 풀 수 있었다.
"애초에 brute force라도, 순열을 쓰는 n!로는 문제를 풀 수 없었음.

그리고 해당 vertex의 degree를 따로 배열로 나타내서, 친구로 됐으면, a[i][j] a[j][i]를 true로 표시하고
d[i]+1 d[j]+1해서 해당 사람의 친구수를 +1 해줌.

제일 중요했던 점은,
a[i][j] a[j][i]로 서로 친구여부를 true로 따져줬기 때문에,
a[i][j]고 a[i][k], a[j][k]면 i와 j와 k는 친구라는 이산논리를 따질줄 알아야함.

그리고 d에 저장된건 해당 정점 사람의 친구 수니까
위에 세 친구의 친구 수가 추가된 6만 빼면 원하는 정답이 나온다.

 */

import java.util.*;
public class 세친구 {
    static int n,m;
    static boolean[][] a;
    static int[] d;

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();

        a=new boolean[n+1][n+1];
        d=new int[n+1];

        for(int i=0;i<m;i++){
            int u=sc.nextInt();
            int v=sc.nextInt();

            a[u][v]=true;
            a[v][u]=true;
            d[u]+=1;
            d[v]+=1;
        }

        int ans=-1;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(a[i][j]){//i랑 j가 친구라면
                    for(int k=1;k<=n;k++){
                        if(a[i][k] && a[j][k]){//그리고 i랑 k도 친구고 j랑 k도 친구라면->셋 다 친구 조건 달성.
                            int sum=d[i]+d[j]+d[k]-6;
                            //-6을 해주는 이유
                            //i j k가 서로 친구기때문에
                            //a[i][j] a[i][k] a[j][i] a[j][k] a[k][i] a[k][j]로 해당 정점의 친구 수 추가한거를
                            //2씩 3번 빼줘야 하기때문.
                            if(ans==-1 || ans>sum) ans=sum;
                        }
                    }
                }
            }
        }

        System.out.println(ans);
    }
}
