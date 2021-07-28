/*
Deque 실제 구현.
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
덱의 기능들.
 */


import javax.security.sasl.SaslClient;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.Scanner;

public class 덱 {
    public static void main(String[] args) {
        int n;
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        Deque<Integer> d=new ArrayDeque<>();
        for(int i=0;i<n;i++){
            String s=sc.next();
            if(s.equals("push_front")){
                int a=sc.nextInt();
                d.addFirst(a);
            }
            else if(s.equals("push_back")){
                int a=sc.nextInt();
                d.addLast(a);
            }
            if(s.equals("size")){
                System.out.println(d.size());
            }
            else if(s.equals("empty")){
                if(d.size()==0){
                    System.out.println(1);
                }
                else{
                    System.out.println(0);
                }
            }
            else if(s.equals("front")){
                if(d.peekFirst()==null){
                    System.out.println(-1);
                }
                else{
                    System.out.println(d.peekFirst());
                }
            }
            else if(s.equals("back")){
                if(d.peekLast()==null){
                    System.out.println(-1);
                }
                else{
                    System.out.println(d.peekLast());
                }
            }
            else if(s.equals("pop_front")){
                Integer a=d.peekFirst();
                if(a==null) System.out.println(-1);
                else {
                    System.out.println(a);
                    d.remove(a);
                }
            }
            else if(s.equals("pop_back")){
                Integer b=d.peekLast();
                if(b==null) System.out.println(-1);
                else {
                    System.out.println(b);
                    d.remove(b);
                }
            }
        }
        System.out.println();
    }
}
