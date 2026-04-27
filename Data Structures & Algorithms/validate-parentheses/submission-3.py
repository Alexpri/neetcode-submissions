class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        brackets_map = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        opened_set = {"[", "(", "{"}

        opened_stack = list()

        is_valid = True

        for el in s:
            if el in opened_set:
                opened_stack.append(el)
            else:
                if not len(opened_stack):
                    return False

                opened_el = opened_stack.pop()
                if opened_el != brackets_map[el]:
                    return False

        return not bool(len(opened_stack))