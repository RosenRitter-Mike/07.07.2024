grade: int = int(input("what is your grade? "));
if grade > 0 and grade <=40:
    print("try harder next time…");
elif grade >= 41 and grade <=60:
    print("you're getting there, need some more work");
elif grade >= 61 and grade <=80:
    print("pretty good");
elif grade >= 81 and grade <=95:
    print("awesome!");
elif grade >= 96 and grade <=100:
    print("excellent!!! You're a Star!");
else:
    print("illegal grade");

'''
______________Task______________________________________________________
a.עבור ציון בין0-40: הדפס"try harder next time…"
b.עבור ציון בין41-60: הדפס"you're getting there, need some more work"
c.עבור ציון בין61-80: הדפס"pretty good"
d.עבור ציון בין81-95: הדפס"awesome!"
e.עבור ציון בין96-100: הדפס"excellent!!! You're a Star!"
f.עבור ציון קטן מ-0או גדול מ-100:הדפס"illegal grade"
________________________________________________________________________
'''