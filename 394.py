class Solution:
    def get_integer(self, s: str, position: int):
        multiplier = ""
        while position >= 0 and s[position].isdigit():
            multiplier = s[position] + multiplier
            position -= 1

        return int(multiplier), position

    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s) - 1, -1, -1):
            curr_char = s[i]

            if curr_char == '[':
                multiplier_factor, i = self.get_integer(s, i - 1)
                temp_str_list = []
                while True and stack:
                    popped_char = stack.pop()
                    if popped_char == ']':
                        break
                    temp_str_list.append(popped_char)
                temp_str = "".join(temp_str_list)
                temp_str = temp_str * multiplier_factor
                for j in range(len(temp_str) - 1, -1, -1):
                    stack.append(temp_str[j])
            else:
                stack.append(curr_char)

        ans = reversed("".join(stack))

        stack = []

        for i in ans:
            if not i.isdigit():
                stack.append(i)

        return "".join(stack)


s = Solution()
print(s.decodeString("100[leetcode]"))
