class Solution:
    def calPoints(self, operations: List[str]) -> int:
        answer = []
        sol = 0
        for i in range(len(operations)):
            if operations[i] == 'C':
                answer.pop()
            elif operations[i] == 'D':
                answer.append(answer[-1]*2)
            elif operations[i] == "+":
                answer.append(answer[-1] + answer[-2])
            else:
                answer.append(int(operations[i]))
        
        for num in answer:
            sol += num
        return sol
        