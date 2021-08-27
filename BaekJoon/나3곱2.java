import java.util.*;
class Pair_ implements Comparable<Pair_>{
    int three;
    long num;
    Pair_(int three,long num){
        this.three=three;
        this.num=num;
    }
    public int hashCode(){
        return Objects.hash(three,num);
    }
    public boolean equals(Object o){
        if(o instanceof Pair_){
            Pair_ that=(Pair_) o;
            if(this.three==that.three && this.num==that.num){
                return true;
            }
            else return false;
        }
        else return false;
    }
    public int compareTo(Pair_ that){
        if(this.three>that.three) return -1;
        else if (this.three==that.three){
            if(this.num<that.num) return -1;
            else if(this.num==that.num) return 0;
            else return 1;
        }
        else return 1;
    }
}

/*
메인에서 구현
n을 입력받고 나3곱2를 진행할 수열 B를 입력받음
근데 이 수열 B는 그냥 배열이 아니라, 내가 구현한 Pair클래스.
Pair 클래스 역할
->입력받은 원소가 3으로 몇번이나 나눠지는지 검사해서
three(3으로 나눠진 횟수),num(해당 원소)를
넣는다.

그다음 Arrays.sort를 썼는데,
Pair a에 대한 정렬이기 때문에
hashCode,equals,compareTo 메서드를 재정의 해서
내가 원하는 순서대로 정렬해줌.
중요한 것은 equals와 compareTo인데

equals의 경우 Pair객체인 경우에만 두개가 같은지 비교해주고,
compartTo의 경우 three(3으로 나눈 횟수)가 큰 순서대로 정렬
같으면, num(실제 숫자크기) 비교해서 정렬 하게끔해줌.


메인 아이디어
뒤로 갈수록 3의배수가 아니면 나3연산을 할 수 없음
그래서 나3 연산이 가능한 3의배수 횟수가 많은 숫자부터
앞에 배치함.
만약 나3연산이 가능한 횟수가 같으면,숫자 크기가
작은 순서대로(=오름차순) 정렬을 해주면 된다.
 */
public class 나3곱2 {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        Pair_[] a=new Pair_[n];
        for(int i=0;i<n;i++){
            long num=sc.nextLong();
            int three=0;
            for(long j=num;j%3==0;j/=3){
                three+=1;
            }
            a[i]=new Pair_(three,num);
        }
        Arrays.sort(a);
        for(int i=0;i<n;i++){
            System.out.print(a[i].num+" ");
        }
        System.out.println();

    }
}
