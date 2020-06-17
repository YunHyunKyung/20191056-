name = input("이름을 입력하시오 : ")
user={
    "name" : name,
    "level" : 1,
    "hp" : 100,
    "item" : ["에리디봉","뉴리디봉","또리디봉"],
    "skill" : ["이수만 펀치", "김영민 핵펀치", "유영진 피하기"] 
    }
f = open("save.txt", "w")
#f.write("name:{}\n".format(name))
for key in user:
    if type(user[key]) is list:
        for i in user[key]:
            print("%s:%s" % (key, i))
            f.write("%s:%s\n" % (key, i))
    else:
        print("%s:%s" % (key, user[key]))
        f.write("%s:%s\n" % (key, user[key]))
f.close()

print(user["name"],"님 반갑습니다.", user["name"],"(HP",user["hp"],")으로 게임을 시작합니다.")
b=user["hp"]
print(user["name"],"님의 정보입니다.")
for key in user:
    print(key," : ", user[key])
def nhp():
    print("현재 HP : ",b)
    
print("길을 가다가 이수만을 만났습니다.")
print("1. 돈을 지급한다. 2. 일 좀 제대로 하라고 욕을 한다. 3. 그냥 지나간다. 4. 스킬/아이템 사용")

try:
    c = int(input("당신이 취할 행동은? : "))
    if c==1:
        with open("basic.txt", "w") as file:
            file.write("당신은 이수만의 ATM이 되었습니다. HP -5")
        with open("basic.txt", "r") as file:
            contents = file.read()
        print(contents)
        b=b-5
        nhp()
    if c==2:
        print("당신은 경찰서로 소환되었습니다. HP -50")
        b=b-50
        nhp()
    if c==3:
        print("당신은 아무런 타격도 입지 않았습니다. HP -0")
        nhp()
    if c==4:
        print(user["skill"])
        f = int(input("당신이 취할 행동은? : "))
        if f==1:
              print("이수만에게 피해를 입혔습니다. 이수만 처치")
              nhp()
        if f==2:
              print("이수만에게 피해를 역습 당했습니다. HP -10")
              b=b-10
              nhp()
        if f==3:
              print("이수만을 치료합니다.")
              nhp()
except:
    print("입력이 올바르지 않습니다")
    
    

print("집 앞에서 엑소를 만났습니다.")
print("1. 돈을 지급한다. 2. 일 좀 제대로 하라고 욕을 한다. 3. 그냥 지나간다. 4.스킬/아이템 사용")
d = int(input("당신이 취할 행동은? : "))
if d==1:
    print("당신은 엑소의 팬이 되었습니다. HP +120408")
    b=b+120408
    nhp()
if d==2:
    print("사형. HP -120408")
    b=b-120408
    nhp()
if d==3:
    print("바보같은 선택을 하였습니다. HP -100")
    b=b-100
    nhp()
if d==4:
    print(user["item"])
    g = int(input("당신이 취할 행동은? : "))
    if g==1:
          print("엑소를 응원합니다. HP +100")
          b=b+100
          nhp()
    if g==2:
          print("엑소에게 몬스터 춤을 보여줍니다. HP +1000")
          b=b+1000
          nhp()
    if g==3:
          print("엑소에게 파워를 불러줍니다. HP +10000")
          b=b+10000
          nhp()


print("길을 가다가 아무 것도 모르는 머글을 만났습니다.")
print("1. 시비를 건다. 2. 엑소를 열심히 영업한다. 3. 그냥 지나간다.")
e = int(input("당신이 취할 행동은? : "))
if e==1:
    print("적이 생겼습니다. HP -500")
    b=b-500
    nhp()
if e==2:
    print("동료가 생겼습니다. HP +120408")
    b=b+120408
    nhp()
if e==3:
    print("바보같은 선택을 하였습니다. HP -100")
    b=b-100
    nhp()


if b>100000:
    print("당신은 엑소와 함께 행복한 덕질 라이프를 보내게 됩니다.")

if 100000>b>0:
    print("머글이군요. 그냥 지나가세요.")

if b<0:
    print("사형")
