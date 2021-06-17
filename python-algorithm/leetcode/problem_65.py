import re


class Solution:
    def is_number(self, s: str) -> bool:
        def check_int(num: str) -> bool:
            return True if re.match("^\\d+$", num) else False

        def check_float(num: str) -> bool:
            splits = num.split(".")
            if len(splits) > 2:
                return False
            if splits[0] == "" and splits[1] == "":
                return False
            return check_int(splits[0] + "0") and check_int(splits[1] + "0")

        splits = re.split("[Ee]", s)
        if len(splits) > 2:
            return False
        if len(splits) == 1:
            arr = s.split('.')
            if len(arr) == 1:
                if s.startswith('+') or s.startswith('-'):
                    s = s[1:]
                return check_int(s)
            if len(arr) == 2:
                if s.startswith('+') or s.startswith('-'):
                    s = s[1:]
                return check_float(s)
            return False
        if splits[0] == '' or splits[1] == '':
            return False
        if splits[1].startswith('+') or splits[1].startswith('-'):
            splits[1] = splits[1][1:]
        if not check_int(splits[1]):
            return False
        if len(splits[0].split('.')) == 1:
            if splits[0].startswith('+') or splits[0].startswith('-'):
                splits[0] = splits[0][1:]
            return check_int(splits[0])
        elif len(splits[0].split('.')) == 2:
            if splits[0].startswith('+') or splits[0].startswith('-'):
                splits[0] = splits[0][1:]
            return check_float(splits[0])
        else:
            return False
