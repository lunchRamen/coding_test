/*
    서울 지하철 2호선
    2호선은 총 51개의 역.

    순환선+트리.(사이클+트리)

    n을 입력받고
    n개의 양방향 노드를 입력 받으면
    출력으로 1~n까지의 역에 대해 해당 역에서 순환선까지 가는데 걸리는 역의 수를 출력해주는 형태.

    N개의 n-1개의 간선으로 이루어져있는 그래프:트리
    트리의 특징:사이클이 없다. 트리에서 최단 경로:DFS/BFS로 구할 수 있다.(사이클이 없어서 임의의 두 정점 사이의 경로가 1개)

    트리에 간선 하나를 추가하면, 사이클이 된다.

    1.순환선 찾기(DFS)
    2.모든 정점과 순환선사이의 거리.(DFS/BFS)->순환선의 정점을 시작점으로 해서 거리를 계산.

    사이클:시작점부터 시작해서 모든 정점을 방문 후 시작점으로 돌아오는 경로가 있는 트리.

    방문했으면 visited노드에 true로 바꿔줌.

    사이클을 찾는법: 한 정점에서 dfs를 돌렸을때 스택에 시작정점이 들어오면, 스택안에 들어있는 정점들의 집합이 사이클임.



     */
    import java.util.*;
    public class 서울지하철2호선 {
        static ArrayList<Integer>[] a;
        static int[] check;
        static int[] dist;
        static int go(int x,int p){//x:방문한 정점 p:이전 정점. p->x로 오는걸로 재귀를 돌림.
            //-2:사이클은 찾았지만 포함 안됨
            //-1:사이클 못찾음
            //0~n-1:사이클을 찾았고 시작인덱스임
            if(check[x]==1) return x;//해당 정점을 방문했으면 x를 return x는 0보다 클거니까 재귀의 res엔 양수가 들어감
            check[x]=1;//방문 안했다면 방문한걸로 표시 후
            for(int y:a[x]){//x정점에 연결된 모든 정점들에 대해서
                if(y==p) continue;//이전 정점을 재귀호출하면 무한루프에 빠지니까 예외처리 해주고
                int res=go(y,x);//x에 연결된 정점으로 go를 재귀호출함.
                if(res==-2) return -2;//그래서 return된 값이 -2라면 -2를 계속 return
                if(res>=0){//양수라면 ->사이클 도중의 수라는 거니까
                    check[x]=2;//방문한거에 사이클관계인 2로 표시.
                    if(x==res) return -2;//x랑 res랑 같다면 시작정점으로 돌아온거니까, 그때부턴 -2 return
                    else return res;
                }
            }
            return -1;
        }
        public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            int n=sc.nextInt();
            a=new ArrayList[n];
            dist=new int[n];
            check=new int[n];
            for(int i=0;i<n;i++){
                a[i]=new ArrayList<>();
            }//a는 이중 ArrayList로 구성해줌.
            for(int i=0;i<n;i++){
                int u=sc.nextInt()-1;
                int v=sc.nextInt()-1;
                a[u].add(v);
                a[v].add(u);
            }//그래서 양방향 간선을 입력받았을때 a[i]에 접근했을때 나오는 원소들이 정점 i와 연결된 정점들로 나타날수 있게끔.
            go(0,-1);//go 재귀 돌려서 check갱신하고
            Queue<Integer> q=new LinkedList<>();
            //q만들어서 이제 bfs돌릴거.
            for(int i=0;i<n;i++){
                if(check[i]==2){//i번째 정점이 사이클에 포함된 정점이면
                    dist[i]=0;//거리는 0이고(사이클에 포함됐으니까)
                    q.add(i);//i는 q에 넣음.
                }
                else{//아니면 -1로.
                    dist[i]=-1;
                }
            }
            while(!q.isEmpty()){//q에 들어있는 정점들은 모두 사이클에 포함된 정점들만 들어있음.
                int x=q.remove();
                for(int y:a[x]){//그럼 이제 사이클에 포함된 정점들을 하나씩 없애고 그 정점과 연결된 점들에 대해서
                    if(dist[y]==-1){//사이클에 포함 안된 정점이면
                        q.add(y);//그 정점을 q에 다시 넣고
                        dist[y]=dist[x]+1;//y정점이 순환선까지 가는 거리는 0+1.
                        //그리고 y를 다시 q에 넣었으니까 y에 연결된 정점들은 1+1...이렇게 해서 거리가 1씩 늘어나고 저장됨.
                    }
                }
            }
            for(int i=0;i<n;i++){
                System.out.print(dist[i]+" ");
            }
            System.out.println();
        }
    }
