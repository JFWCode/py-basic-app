import json

z = """{
   "first_ name": "Jane",
   "last_ name": "Smith",
   "email": "jane .smith@wyng.com",
   "gender": null,

"invitations": [
{
   "from": "",
   "code": null,
   "test": false,
   "home": true
}
],
"company": {
    "name": "",
    "industries": {"dd":""},
    "industries1": {"dd":"1"}
},
"address": {
   "city": "New York",
    "state": "NY",
    "zip": "10011",
    "street": " "
  }
}"""

def isTrue(v):
    if v not in [' ']:
        return v
    else:
        return None


def dealwith_json_data(z):
    if isinstance(z, list):
        ll = []
        for i in z:
            l_data = dealwith_json_data(i)
            l_data = isTrue(l_data)
            if l_data:
                ll.append(l_data)

        if z:
            return ll
    elif isinstance(z, dict):
        dd = {}
        for key, val in z.items():
            d_data = dealwith_json_data(val)
            d_data = isTrue(d_data)
            if d_data:
                dd[key] = d_data

        return dd
    else:
        new_z = isTrue(z)
        if new_z:
            return z

def dp(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    return a


def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return fib(n-1) + fib(n-2)


def solution(d):
    # 在这⾥写代码
    sorted_d = sorted(d.items(), key=lambda item:(item[1], item[0]), reverse=True)
    return sorted_d


def lengthOfLongestSubstring(s):
    dic = {}
    res = tmp = 0
    for j in range(len(s)):
        i = dic.get(s[j], -1)
        dic[s[j]] = j
        tmp = tmp + 1 if tmp < j - i else j - i
        res = max(res, tmp)
    return res



if __name__ == '__main__':
    # data = json.loads(z)
    # r_data = dealwith_json_data(data)
    # print(r_data)
    #print(fib(5))
    # d = {7: 2, 10: 33, 4: 11, 9: 11, 5: 14, 3: 8, 12: 11}
    # print(solution(d))
    # d = {1: 2, 0: 3, 4: 1, 9: 2, 5: 14, 3: 8, 2: 2}
    # print(solution(d))

    s = '12301239'
    r = lengthOfLongestSubstring(s)
    print(r)
