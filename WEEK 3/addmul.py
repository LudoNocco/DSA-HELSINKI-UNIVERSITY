import re

def evaluate(data):
    pattern=re.compile(r'(add|mul)\((\d+),(\d+)\)')
    def repl(m):
        if m.group(1)=='add':
            return str(int(m.group(2))+int(m.group(3)))
        return str(int(m.group(2))*int(m.group(3)))
    return pattern.sub(repl,data)

if __name__ == "__main__":
    print(evaluate("add(1,2)")) # 3
    print(evaluate("aybabtu")) # aybabtu
    print(evaluate("mul(6,7),mul(7,191)")) # 42,1337
    print(evaluate("abadd(123,456)mulxmul(3,13)")) # ab579mulx39
    print(evaluate("mul()mul(13)mul(0,1)")) # mul()mul(13)mul(0,1)

    data = "mul(6,7)"*10**5
    result = evaluate(data)
    print(len(result)) # 200000
    print(result[:20]) # 42424242424242424242
