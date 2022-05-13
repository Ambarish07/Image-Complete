def convert( s: str, n: int) -> str:
    ans = ""
    x = 2*n - 2
    y = 0
    for i in range(n):
        ans += s[i]
        tmp = i
        while tmp + x < len(s):
            if x > 0 and (tmp + x) < len(s): 
                ans += s[x+tmp]
                tmp += x
                x -= 2
            if y > 0 and tmp + y < len(s):
                ans += s[y+tmp]
                tmp += y
                y += 2
        print(tmp,x,y,ans)
    return ans

print(convert("PAYPALISHIRING",3))