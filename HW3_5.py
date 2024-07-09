num: int = int(input("input your integer: "));
prnt: str = ""
if not num%5:
    prnt+=" Fizz";
if not num%3:
    prnt+=" Buzz";

print(prnt);
