#include <iostream>

using namespace std;

int arr[1000001];
int* arr2;

void merge(int arr[], int left, int mid, int right) {
	int i;//왼쪽 부분배열 인덱스 포인터
	int j;//오른쪽 부분배열 인덱스 포인터
	int k;//정렬 될 배열의 인덱스 포인터
	i = left;
	j = mid + 1;
	k = left;//combine 된 후 배열도 left부터 시작할테니까

	while (i <= mid && j <= right) {//left~mid까지 mid+1~right까지.
		if (arr[i] <= arr[j]) {
			arr2[k++] = arr[i++];
		}//arr[left]<=arr[mid+1] -> 1칸부터 2칸 4칸..올라가는데 몇칸을 합치든
		 //두 부분배열의 왼쪽 첫번째 i(left),j(mid+1)부터 끝까지(i==mid && j==right)
		 //오른쪽이 더 크다면 임시배열에 왼쪽꺼를 넣고
		else
			arr2[k++] = arr[j++];//왼쪽이 더크면 오른쪽꺼를.
		//이걸 left~mid && mid+1~right 로 해준다. 그러면 해당 부분배열의 merge과정이 끝남.
		//k는 arr의 left값을 가지고 있으니까 while문을 다 돌면 k는 left~mid~right해서 k==right index로 남음.
		//이건 merge할때마다 left값을 가져오는거니까 상관없다.
	}

	//if (i > mid) {//만약 왼쪽배열에 작은것들이 많아서, 왼쪽 부분배열을 먼저 arr2에 다 넣었다면
	//			  //위에 while문에서 i++이 반복문에서만 쓰이는 임시변수가 아니라 merge함수의
	//			  //지역변수로 지정 되어있으니까 왼쪽부분배열이 먼저 다 비워졌으면
	//			  //i가 mid보다 1 커진 상태가 됨.
	//	for (int a = j; a <= right; a++)
	//		arr2[k++] = arr[a];//그럴땐 오른쪽 부분배열에 값이 남아있단 얘기니까 a=j부터 right까지
	//						   //임시배열에 넣어준다.
	//}
	//else {//반대의 경우에는 left의 부분배열을 임시배열에 넣어준다.
	//	for (int a = i; i <= mid; a++) {
	//		arr2[k++] = arr[a];
	//	}
	//}

	int tmp = i > mid ? j : i;
	while (k <= right) arr2[k++] = arr[tmp++];

	for (int a = left; a <= right; a++) {
		arr[a] = arr2[a];//그리고 원배열에 임시배열 값들을 복사하는 과정.
	}
}

void merge_sort(int arr[], int left, int right) {
	int mid;

	if (left < right) {//left가 right보다 크면 재귀호출(다시 반 가르는걸로)->left==right될때까지
						//재귀호출 할 예정.
					   
		mid = (left + right) / 2;//반 가르기(divide)
		merge_sort(arr, left, mid);//left~mid까지 mergesort 재귀호출(left==mid될때까지)
		merge_sort(arr, mid + 1, right);//mid+1~right까지 재귀호출(mid+1==right될때까지)
		merge(arr, left, mid, right);//두개를 합침.
	}

	//mid는 배열을 반으로 나눈곳의 인덱스.
	//merge sort는 부분배열이 1이 될때까지 divide 해주는데 이건 left가 mid가 되고 mid+1이 right가
	//될때까지의 조건으로 돌린다.
	//나누는건 left~mid mid+1~right로 나눈다.
	//합치는건 left,mid,right로 mid를 분기로 나눠진 두 부분배열을 합친다.
}

int main() {
	int n;
	cin >> n;

	arr2 = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	////오름차순 정렬 코드.
	////selection sort(input이 많으면 시간 초과)
	//for (int i = 0; i < n-1; i++) {
	//	for (int j = i+1; j < n; j++) {
	//		if (arr[i] > arr[j]) {
	//			int arr2 = arr[i];
	//			arr[i] = arr[j];
	//			arr[j] = arr2;
	//		}
	//	}
	//}
	//merge sort
	merge_sort(arr, 0, n - 1);



	//heap sort
	for (int i = 0; i < n; i++) {
		cout << arr[i] << "\n";
	}
	/*
	줄바꿈을 할때 버퍼를 비워야하는게 아니면 무조건 \n로 하자. 속도 차이가 매우 많이 난다.
	*/
}
