import json

def set_user(name, hp=100):
    user = {
        "name" : name,
        "level" : 1,
        "hp" : hp,
        "items" : ["에리디봉","뉴리디봉","또리디봉"],
        "skill" : ["이수만 펀치", "김영민 핵펀치", "유영진 피하기"]
    }
    #print("{0}님 반갑습니다. HP {1}으로 게임을 시작합니다." .format(user["name"], user["hp"]))
    with open("static/save.txt", "w", encoding='utf-8') as f: 
       json.dump(user, f, ensure_ascii = False, indent=4)
    return user

def save_game(filename, user) :
    f = open(filename, "w", encoding="utf-8")
    for key in user:
        print("%s:%s" % (key, user[key]))
        f.write("%s:%s\n" % (key, user[key]))
    f.close()