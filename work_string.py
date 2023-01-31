from copy import copy


def math_string(s: str) -> str:
    arr = ['*', '|', '+']
    for i in arr:
        while True:
            if i not in s:
                break
            index = s.find(i)
            index_start = max(s.rfind(arr[0], 0, index), s.rfind(arr[1], 0, index), s.rfind(arr[2], 0, index)) + 1
            index_stop = len(s)
            if arr[0] in s[index + 1:] and s.find(arr[0], index + 1, len(s)) < index_stop:
                index_stop = s.find(arr[0], index + 1, len(s))
            if arr[1] in s[index + 1:] and s.find(arr[1], index + 1, len(s)) < index_stop:
                index_stop = s.find(arr[1], index + 1, len(s))
            if arr[2] in s[index + 1:] and s.find(arr[2], index + 1, len(s)) < index_stop:
                index_stop = s.find(arr[2], index + 1, len(s))
            term1 = float(s[index_start:index])
            term2 = float(s[index + 1:index_stop])
            if i == '+':
                result = format(term1 + term2, '.9f')
            elif i == '|':
                result = format(term1 * term2 / (term1 + term2), '.9f')
            elif i == '*':
                result = format(term1 * term2, '.9f')
            if '.000000000' in result:
                result = result[:-10]
            s = s[:index_start] + result + s[index_stop:]
    return s

def clear_string(s: str) -> str:
    s1 = ''
    for i in s.lower():
        if i == '-':
            s1 += '|'
        elif i == ',':
            s1 += '.'
        elif i in '0123456789+|)(.*':
            s1 += i
        if i == 'k' or i == 'к':
            s1 += '*1000'
        elif i == 'm' or i == 'м':
            s1 += '*1000000'
        elif i == 'g' or i == 'г':
            s1 += '*1000000000'
    s1 = s1.lstrip('*').replace('**', '*')
    s = copy(s1)
    s1 = s[0]
    for i in range(1, len(s)):
        if s[i - 1] == ('+' or '|') and s[i] == '*':
            continue
        s1 += s[i]
    return s1


def brackets_string(s: str) -> str:
    index = 0
    while True:
        index = s.find('(', index)
        if index == -1:
            break
        index_bracket_open = s.find('(', index + 1)
        index_bracket_close = s.find(')', index + 1)
        if (index_bracket_open < index_bracket_close and index_bracket_open != -1) or (index_bracket_close == -1):
            index += 1
            continue
        index_start = index
        index_stop = s.find(')', index)
        s = s[:index_start] + math_string(s[index_start + 1:index_stop]) + s[index_stop + 1:]
        index = 0
    return s


def parse_string(s: str):
    s = clear_string(s)
    s = brackets_string(s)
    s = math_string(s)
    return s
