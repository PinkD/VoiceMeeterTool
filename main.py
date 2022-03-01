import _md5
import sys

built_in = "D27EB245948A4B728B1F23572D78ADA9"

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage:\n\t{sys.argv[0]} email serial")
        exit(1)
    email = sys.argv[1]
    serial = sys.argv[2]
    src = f"{email}{serial}"
    result = []
    s = ""
    for i in range(len(src)):
        c = ord(src[i]) + ord(built_in[i % len(built_in)])
        s += f"{c:X}"
        result.append(c)
    b = bytes.fromhex(s)
    print(f"raw: {s}")
    md5 = _md5.md5()
    md5.update(b)
    sum = md5.hexdigest()
    print(f"sum: {sum}")
    code = sum[12:14] + sum[16:20] + sum[22:24]
    code = code.upper()
    print(f"code: {code}")
