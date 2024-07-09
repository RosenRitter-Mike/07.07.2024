user: list =[];
for x in range(3):
    uid: str = input("id: ");
    fname: str = input("first name: ");
    lname: str = input("last name: ");
    height: float = float(input("height: "));
    ybirth: int = int(input("year of birth: "));

    user.append(f"#id: {uid:9} name:{lname:<10}, {fname:<10} height{height:.2f} year-of-birth:{ybirth:<4}");

print(f"{user[0]}\n{user[1]}\n{user[2]}");
