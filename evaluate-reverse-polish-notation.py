class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c.lstrip('-+').isdigit():
                stack.append(int(c))
            elif c=="+":
               temp = stack.pop() 
               temp += stack.pop()
               stack.append(temp)
                           
            elif c=="-":
               second = stack.pop() 
               first = stack.pop()
               stack.append(first-second)              
            elif c == "/":
               deno = stack.pop() 
               numerator = stack.pop()
               temp = numerator / deno
               if temp < 0:
                  temp = ceil(temp)
               else:
                    temp = floor(temp)
               stack.append(temp)
               
            elif c=="*":
               temp = stack.pop() 
               temp *= stack.pop()
               stack.append(temp)
               
        return stack[0]

