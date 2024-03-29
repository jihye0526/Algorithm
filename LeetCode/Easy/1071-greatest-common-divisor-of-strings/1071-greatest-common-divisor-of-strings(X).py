class Solution:
    # 다른 사람 풀이
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 두 문자를 각각 더했을 때 결과가 다르다면 반복되지 않는 경우라는 것
        if str1 + str2 != str2 + str1:
            return ""

        # 겹치는 문자의 길이는 무조건 두 문자의 길이의 최대공약수
        length = math.gcd(len(str1), len(str2))
        return str2[:length]