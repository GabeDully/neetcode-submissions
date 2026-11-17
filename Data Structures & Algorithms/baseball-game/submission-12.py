class Solution:
    def calPoints(self, operations: List[str]) -> int:
        c = []
        for i in range(len(operations)):
            if operations[i] == "+":
                c.append(c[-2] + c[-1])
            elif operations[i] == "D":
                c.append(c[-1] * 2)
            elif operations[i] == "C":
                c.pop()
            else:
                c.append(int(operations[i]))
            print(c)
        
        return sum(c)