from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #리스트로 선언
        letters, digits = [], []
        for log in logs:
            #split()으로 나누어 1번째 원소가 숫자라면
            if log.split()[1].isdigit():
                #digits에 넣는다
                digits.append(log)
            else:
                letters.append(log)
        #정렬하는데 위에서 1번째 원소가 글자인 letters에서 1번째원소에 따라 정렬한다
        #만약 1번쨰이후 원소가 같다면(ex. 예시의 let3 art zero, let0 art zero) 0번째 원소로 구별
        #x.split()[0]가 없다면 input순서로 구별해서 let3이 let0보다 앞으로 온다
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
    
    
if __name__ == "__main__":
    a = Solution()
    b = a.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero", "let0 art zero"])
    print(b)