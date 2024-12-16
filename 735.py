class Solution:
    def asteroidCollision(self, asteroids):
        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            curr_element = asteroids[i]
            abs_val = abs(curr_element)

            if (curr_element < 0 and stack[-1] < 0) or (curr_element > 0 and stack[-1] > 0):
                stack.append(curr_element)

            else:
                while len(stack) >= 1 and abs(stack[-1]) <= abs_val and stack[-1] > 0:
                    last_popped_element = stack.pop()
                else:
                    stack.append(curr_element)
                if len(stack) == 0 and abs_val != last_popped_element:
                    stack.append(curr_element)

        return stack


soln = Solution()
print(soln.asteroidCollision([-2,-2,1,-2]))
