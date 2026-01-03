class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            while stack and stack[-1] > 0 and num < 0:
                net_value = stack[-1] + num
                if net_value < 0:
                    stack.pop()
                elif net_value > 0:
                    num = 0
                else:
                    num = 0
                    stack.pop()
            
            if num != 0:
                stack.append(num)
        return stack