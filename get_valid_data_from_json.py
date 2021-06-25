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


if __name__ == '__main__':
    # data = json.loads(z)
    # r_data = dealwith_json_data(data)
    # print(r_data)
    print(fib(5))
