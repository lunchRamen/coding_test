class Solution:
    """
    주어진 "리스트 숫자들"이 하나의 숫자로써 판단.
    해당 숫자+1한 값을 다시 리스트 숫자로 변환시켜 return.

    파이써닉한 코드를 사용하면, 2줄 혹은 1줄로 풀이가 가능하다.
    주어진 배열의 원소들을 str형으로 변환시키는 list comprehension과
    이걸 하나의 문자열로 합친 후, int로 변환시킨 다음 +1 시키고,
    이걸 다시 str로 형변환하여 list로 만들고, 다시 각 원소를 int로 형변환한다.

    파이써닉하게 풀면 좋은 문제.
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(i) for i in list(str(int("".join([str(digit) for digit in digits]))+1))]
