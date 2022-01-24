"""520. Detect Capital
https://leetcode.com/problems/detect-capital/
"""


def detect_capital_use(word: str) -> bool:
    n = len(word)
    if n == 1:
        return True
    is_first_capital = True if ('A' <= word[0] <= 'Z') else False
    is_second_capital = True if ('A' <= word[1] <= 'Z') else False
    if not is_first_capital and is_second_capital:
        return False
    case = 0  # Abc
    if is_first_capital and is_second_capital:
        case = 1  # ABC
    if not is_first_capital and not is_second_capital:
        case = 2  # abc
    for i in range(2, len(word)):
        is_cur_capital = True if ('A' <= word[i] <= 'Z') else False
        if is_cur_capital:
            if case != 1:
                return False
        else:
            if case == 1:
                return False
    return True
