#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
테트로미노
4~500까지 수로 NXM판을 만들고, 각 칸에 가중치를 둠.

테트리스 도형 하나를 놨을때 가중치의 합이 최대가 되게끔 하는 최대값 출력.

테트리스 도형은 회전,대칭 가능->이걸로 총 19가지 경우 나옴.

N M은 500까지 되니까 25만칸까지 됨.
19x25만 ->대략 500만. 1억에 1초 -> brute force로 풀수 o.
*/
int a[500][500];

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (j + 3 < m) {
                int temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i][j + 3];
                if (ans < temp) ans = temp;
            }//xxxx형태 테트로미노(1)
            if (i + 3 < n) {
                int temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 3][j];
                if (ans < temp) ans = temp;
            }//1번형태 세로버전
            if (i + 1 < n && j + 2 < m) {
                int temp = a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 1][j + 2];
                if (ans < temp) ans = temp;
            }//xx
             // x
             // x형태 테트로미노.
            if (i + 2 < n && j + 1 < m) {
                int temp = a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 2][j];
                if (ans < temp) ans = temp;
            }//xxx 형태 테트로미노
             //x
            if (i + 1 < n && j + 2 < m) {
                int temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 2];
                if (ans < temp) ans = temp;
            }//x
             //x
             //xx형태 테트로미노
            if (i + 2 < n && j - 1 >= 0) {
                int temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 2][j - 1];
                if (ans < temp) ans = temp;
            }//  x
             //xxx 형태 테트로미노
            if (i - 1 >= 0 && j + 2 < m) {
                int temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i - 1][j + 2];
                if (ans < temp) ans = temp;
            }// x
             // x
             //xx형태 테트로미노
            if (i + 2 < n && j + 1 < m) {
                int temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 2][j + 1];
                if (ans < temp) ans = temp;
            }//xxx
             //  x형태 테트로미노
            if (i + 1 < n && j + 2 < m) {
                int temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j];
                if (ans < temp) ans = temp;
            }//x
             //x
             //xx형태 테트로미노
            if (i + 2 < n && j + 1 < m) {
                int temp = a[i][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 2][j + 1];
                if (ans < temp) ans = temp;
            }//x
             //xxx형태 테트로미노
            if (i + 1 < n && j + 1 < m) {
                int temp = a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1];
                if (ans < temp) ans = temp;
            }//xx
             //xx형태 테트로미노
            if (i - 1 >= 0 && j + 2 < m) {
                int temp = a[i][j] + a[i][j + 1] + a[i - 1][j + 1] + a[i - 1][j + 2];
                if (ans < temp) ans = temp;
            }//  x
             // xx
             // x  형태 테트로미노
            if (i + 2 < n && j + 1 < m) {
                int temp = a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 2][j + 1];
                if (ans < temp) ans = temp;
            }
            if (i + 1 < n && j + 2 < m) {
                int temp = a[i][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 1][j + 2];
                if (ans < temp) ans = temp;
            }
            if (i + 2 < n && j - 1 >= 0) {
                int temp = a[i][j] + a[i + 1][j] + a[i + 1][j - 1] + a[i + 2][j - 1];
                if (ans < temp) ans = temp;
            }
            if (j + 2 < m) {
                int temp = a[i][j] + a[i][j + 1] + a[i][j + 2];
                if (i - 1 >= 0) {
                    int temp2 = temp + a[i - 1][j + 1];
                    if (ans < temp2) ans = temp2;
                }
                if (i + 1 < n) {
                    int temp2 = temp + a[i + 1][j + 1];
                    if (ans < temp2) ans = temp2;
                }
            }// x                   x
             //xx       or          xx 형태.
             // x                   x
            if (i + 2 < n) {
                int temp = a[i][j] + a[i + 1][j] + a[i + 2][j];
                if (j + 1 < m) {
                    int temp2 = temp + a[i + 1][j + 1];
                    if (ans < temp2) ans = temp2;
                }
                if (j - 1 >= 0) {
                    int temp2 = temp + a[i + 1][j - 1];
                    if (ans < temp2) ans = temp2;
                }
            }//              x   
             //xxx     or   xxx  형태.
             // x
        }
    }
    //이렇게 회전 대칭에 대해서 19가지 테트로미노를 n과 m의 범위 및 0이상이 되게끔 만들어놓고
    //temp에 넣고 temp가 ans보다 크면 ans를 갱신하는 형태로.
    cout << ans << '\n';
    return 0;
}
