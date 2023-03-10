from copy import copy
from decimal import Decimal


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
            term1 = Decimal(s[index_start:index])
            term2 = Decimal(s[index + 1:index_stop])
            if i == '+':
                result = format(term1 + term2, '.13f')
            elif i == '|':
                result = format(term1 * term2 / (term1 + term2), '.13f')
            elif i == '*':
                result = format(term1 * term2, '.13f')
            s = s[:index_start] + result + s[index_stop:]
    return s


def math_string_rc(s: str) -> str:
    while True:
        if '*' not in s:
            break
        index = s.find('*')
        index_start = s.rfind('+', 0, index) + 1
        index_stop = s.find('+', index)
        term1 = Decimal(s[index_start:index])
        term2 = Decimal(s[index + 1:index_stop])
        result = format(term1 * term2, '.13f')
        s = s[:index_start] + result + s[index_stop:]
    return s


def level_string_rc(s: str) -> str:
    index = s.rfind('+') + 1
    if '%' in s:
        result = format(Decimal(s[index:-1])/Decimal('100.0'), '.13f')
    elif 'v' in s:
        index_start = s.find('v')
        term1 = Decimal(s[index:index_start])
        term2 = Decimal(s[index_start+2:-1])
        result = format(term1 / term2, '.13f')
    s = s[:index] + result
    return s


def time_string_rc(s: str) -> str:
    index1 = s.find('+')
    index2 = s.rfind('+')
    term1 = Decimal(s[:index1])
    term2 = Decimal(s[index1+1:index2])
    term3 = Decimal(s[index2+1:])
    result = format(-(Decimal('1.0')-term3).ln()*term1*term2, '.13f')
    if '.00000000000000' in result:
        result = result[:-15]
    return result


def clear_string_resistor(s: str) -> str:
    s1 = ''
    for i in s.lower():
        if i == '-':
            s1 += '|'
        elif i == ',':
            s1 += '.'
        elif i in '0123456789+|)(.*':
            s1 += i
        if i == 'k' or i == '??':
            s1 += '*1000'
        elif i == 'm' or i == '??':
            s1 += '*1000000'
        elif i == 'g' or i == '??':
            s1 += '*1000000000'
    s1 = s1.lstrip('*').replace('**', '*')
    s = copy(s1)
    s1 = s[0]
    for i in range(1, len(s)):
        if s[i - 1] == ('+' or '|') and s[i] == '*':
            continue
        s1 += s[i]
    return s1


def clear_string_capacity(s: str) -> str:
    s1 = ''
    s = s.lower()
    for i in range(len(s)):
        if s[i] == '-':
            s1 += '|'
        elif s[i] == ',':
            s1 += '.'
        elif s[i] in '0123456789+|)(.*':
            s1 += s[i]
        if (s[i] == 'm' or s[i] == '??') and i != (len(s) - 1) and (s[i + 1] == 'k' or s[i + 1] == '??'):
            s1 += '*0.000001'
        elif s[i] == 'm' or s[i] == '??':
            s1 += '*0.001'
        elif s[i] == 'n' or s[i] == '??':
            s1 += '*0.000000001'
        elif s[i] == 'p' or s[i] == '??':
            s1 += '*0.000000000001'
    s1 = s1.lstrip('*').replace('**', '*')
    s = copy(s1)
    s1 = s[0]
    for i in range(1, len(s)):
        if s[i - 1] == ('+' or '|') and s[i] == '*':
            continue
        s1 += s[i]
    return s1


def clear_string_rc(s: str) -> str:
    s1 = ''
    s = s.lower()
    for i in range(len(s)):
        if s[i] == ',':
            s1 += '.'
        elif s[i] in '0123456789+./v%*':
            s1 += s[i]
        elif s[i] == 'k' and s.find('+', 0, i) == -1:
            s1 += '*1000'
        elif s[i] == 'm' and s.find('+', 0, i) == -1:
            s1 += '*1000000'
        elif s[i] == 'g':
            s1 += '*1000000000'
        elif s[i] == 'm' and s[i + 1] == 'k':
            s1 += '*0.000001'
        elif s[i] == 'm':
            s1 += '*0.001'
        elif s[i] == 'n':
            s1 += '*0.000000001'
        elif s[i] == 'p':
            s1 += '*0.000000000001'
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


def parse_string(s: str, status: str):
    if status == 'rc':
        s = clear_string_rc(s)
        s = math_string_rc(s)
        s = level_string_rc(s)
        s = time_string_rc(s)
        return s
    elif status == 'resistor':
        s = clear_string_resistor(s)
    elif status == 'capacity':
        s = clear_string_capacity(s)
    s = brackets_string(s)
    s = math_string(s)
    return s
