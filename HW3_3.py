volume: int = int(input("what is the volume? "));
match volume:
    case 0:
        print("mute");
    case 1 | 2:
        print("very quiet");
    case 3:
        print("quiet");
    case 4:
        print("moderately quiet");
    case 5:
        print("medium");
    case 6:
        print("moderately loud");
    case 7:
        print("loud");
    case 8:
        print("very loud");
    case 9 | 10:
        print('extremely loud');
    case _:
        print("invalid input");











'''
______________Task______________________________________________________
a.עבור0הדפס "mute"
b.עבור1הדפס "very quiet"
c.עבור2הדפס "very quiet"
d.עבור3הדפס "quiet"
e.עבור4הדפס "moderately quiet"
f.עבור5הדפס "medium"
g.עבור6הדפס "moderately loud"
h.עבור7הדפס "loud"
i.עבור8הדפס "very loud"
j.עבור9הדפס "extremely loud"
k.עבור10הדפס "extremely loud
________________________________________________________________________
'''