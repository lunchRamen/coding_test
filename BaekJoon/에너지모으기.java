/*
N개의 에너지 구슬이 일렬로.
i번째 에너지구슬의 무게는 W(i)
에너지 모으는 방법(반복가능)
1.에너지 구슬을 고른다. 번호를 x라고 함.(첫번째와 마지막은 못 고름)
2.x번째 에너지 구슬을 제거
3.W(x-1)*W(x+1)의 에너지를 모을 수 있다.
4.n을 1감소시키고 에너지구슬을 다시 1~n까지로 번호 매김.
n과 에너지구슬의 무게가 주어졌을때 모을수 있는
에너지의 최대값.

->n이 2가 될때까지 solve를 돌려야할듯.
ex) 1 2 3 4
3을 빼고 2*4를 모음
1 2 4
2를 뺴고 1*4를 모음
1 4
처음과 마지막 구슬만 남아서 더이상 못뺌.
총 덧셈 결과는 12.이렇게.
->계속 배열을 업데이트 해줘야하니까 ArrayList로 구현.

객체로 만든 변수는 무조건 새로 객체 생성 후 인자로 넘기기.

/*
기본 자료형의 객체자료형도, 재귀 함수 호출시 모두 함께 업데이트 되니까 항상 새로 객체 생성 후 인자 넘기기
또한, 객체를 삭제 수정해서 재귀 넘길때도 새로 객체 지정해서 삭제 수정 후 넘겨야 업데이트 되는걸 방지 해줄수 있다.
객체의 경우 정의만하고 쓰지 않으면 NPE가 발생할 수 있다. 정의 후 선언도 같이 해주자.

그리고 객체의 size로 for문을 돌릴때도, 항상 int형으로 받아서 for문을 돌리는 버릇 들이자.
그리고 ArrayList의 객체 자료형의 기본자료형으로도 for문을 자동으로 돌릴수 있다.(unboxing)

c++의 벡터를 ArrayList로 구현시
1.선언의 경우
vector<int> a=> ArrayList<Integer> a=new ArrayList<>();
c++의경우 정의만하고 따로 선언해도 됐지만, 자바의 경우 정의와 선언을 같이 해줘야 NPE가 안난다.

2.함수 호출
void go(vector<int> a){
a.push_back(1);
go(a);
}

static void go(ArrayList<Integer> a){
ArrayList<Integer> b=new ArrayList<>(a);
b.add(1);
go(b);
}
c++의 경우 vector자료구조를 그냥 그대로 쓰면 되지만, 자바의 경우 인자로 넘긴 자료구조가 객체를 원소로 가지는 경우
항상 그전에 새로 정의해서 인자로 받은 자료구조를 복사하고 그걸 수정,삭제,복사해서 재귀 인자로 넘겨줘야 생각한대로 구현이 된다.

void go(vector<int> &a){
a.push_back(1);
go(a);
}
static void go(ArrayList<Integer> a){
a.add(1);
go(a);
}
이렇게 인자로 넘긴 자료구조의 업데이트를 공유하고 싶은경우에는 오히려 자바가 더 편리할 수 있지만, PS의 경우 항상 업데이트
해서 자료구조 넘기는게 중요하기 때문에 위의 경우로 생각하고 밑의 경우를 예외로 두고 생각하도록 하자.
 */

 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class 에너지모으기 {
    static int n;
    static ArrayList<Integer> max;

    static int solve(ArrayList<Integer> a){
        int m=a.size();
        if(m==2){
            return 0;
        }
        //2~n-1번째 구슬 없애고 그 인근 두개 합 곱한걸
        //sum에 더해서 재귀호출.
        int ans=0;
        for(int i=1;i<m-1;i++){
            int temp=a.get(i-1)*a.get(i+1);
            ArrayList<Integer> nextA=new ArrayList<>(a);
            nextA.remove(i);

            temp=temp+solve(nextA);
            if(ans<temp) ans=temp;
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        ArrayList<Integer> a=new ArrayList<>();
        Integer[] arr=new Integer[n];
        for(int i=0;i<n;i++){
            arr[i]=(Integer)sc.nextInt();
        }
        //for(int i=0;i<n;i++){
        //    a.add(arr[i]);
        //}
        a=new ArrayList<>(Arrays.asList(arr));

        System.out.println(solve(a));
    }
}
