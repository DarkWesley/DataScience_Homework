def dec_to_bin(dec):
    dec_int = int(dec)
    dec_frac = dec - dec_int
    b = 0
    w = 1
    while dec_int > 0:
        b += (dec_int % 2) * w
        dec_int //= 2
        w *= 10

    bin_frac = ""
    while dec_frac != 0:
        dec_frac *= 2
        digit = int(dec_frac)
        bin_frac += str(digit)
        dec_frac -= digit

    res = str(b)
    if bin_frac:
        res += "." + bin_frac
    return res
n = float(input("请输入一个十进制数："))
print(f"十进制数 {n} 的二进制表示为 {dec_to_bin(n)}")