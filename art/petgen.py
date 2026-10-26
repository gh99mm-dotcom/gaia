# 20 pet sprites for the planned pet system: 10 SF creatures and 10 robots, 32x32 in the item-icon style. Prints {id:[name,kind,desc,uri]}.
import json,math,random
P='/tmp/claude-0/-home-user-gaia/a08ffecd-82b3-5e77-a1cc-226d4c9424cb/scratchpad/'
exec(open(P+'foodgen.py').read().split('\ndef plate(')[0])
def R(c,x,y,col):c.raw(int(round(x*K)),int(round(y*K)),col)
def eye(c,x,y,col='#141018',glint='#ffffff',big=True):
    X,Y=int(round(x*K)),int(round(y*K))
    for dx in range(2 if big else 1):
        for dy in range(2 if big else 1):c.raw(X+dx,Y+dy,col)
    if big:c.raw(X,Y,glint)
def blush(c,x,y):c.raw(int(round(x*K)),int(round(y*K)),'#ff8fb8');c.raw(int(round(x*K))+1,int(round(y*K)),'#ff8fb8')
def screen_eye(c,x,y,col):
    X,Y=int(round(x*K)),int(round(y*K))
    for dx in range(2):
        for dy in range(3):c.raw(X+dx,Y+dy,col)
D={}
def pet(i,n,kind,d):
    def deco(f):D[i]=(n,kind,d,f);return f
    return deco
# ---------------- SF creatures ----------------
@pet('nebslime','성운 슬라임','sf','속에 작은 별이 떠다니는 말랑한 젤리')
def _(c):
    c.galaxy(c.poly([(4,20),(5,13),(8,9),(12,7.5),(16,9),(19,13),(20,20)]),'#7a4fc0',seed=3)
    c.shape(c.rect(4,19,20,20.5),'#5a3a90',shade=False)
    for x,y in [(9,10),(14,11),(11,15),(16,16),(7,16)]:R(c,x,y,'#fff6c8')
    for x in (9,14):c.shape(c.ell(x+.6,13,1.7,1.9),'#f2eefa',shade=False)
    eye(c,9,12.5);eye(c,14,12.5);blush(c,7,15.5);blush(c,16,15.5);c.line(11,15.5,12.5,15.5,'#2a1a3a')
@pet('starfox','별꼬리 여우','sf','꼬리 끝에 별빛을 매달고 다니는 여우')
def _(c):
    c.shape(c.poly([(13,17),(17,12),(21,9),(22,12),(19,17),(15,20)]),'#3fa9c8')
    c.shape(c.ell(21,9.5,2,2),'#e8fbff',shade=False)
    c.shape(c.ell(10,16,5.5,4),'#5fc8e0')
    c.shape(c.ell(8,10.5,4.5,4),'#6fd8f0')
    c.shape(c.poly([(4.5,8),(5,3.5),(8,6.5)]),'#4fb0d0');c.shape(c.poly([(8.5,6.5),(11,3),(11.5,8)]),'#4fb0d0')
    c.shape(c.ell(6.5,12.5,2,1.3),'#e8fbff',shade=False)
    for x in (7,12):c.shape(c.rect(x,19,x+1.5,21),'#3f98b8',shade=False)
    eye(c,6.5,9.5);eye(c,9.5,9.5);R(c,6,12.2,'#141018')
@pet('meteortl','운석 거북','sf','등에 작은 운석을 지고 다니는 느긋한 거북')
def _(c):
    c.shape(c.ell(5,15.5,3,2.6),'#8fc0a0')
    for x in (8,16):c.shape(c.rect(x,18,x+2,20.5),'#7aa88a')
    c.shape(c.ell(13,14,7.5,5.5),'#6e6470')
    for x,y,r in [(10,12,1.4),(15,11,1.1),(13,15.5,1.2),(17,15,.9)]:c.shape(c.ell(x,y,r,r),'#4a4252',shade=False)
    R(c,11,10,'#ffb35f');R(c,16.5,12.5,'#ffb35f')
    c.shape(c.rect(6,18.5,20,19),'#5a5260',shade=False)
    eye(c,3.5,14.5)
@pet('jelly','은하 해파리','sf','공중을 둥실둥실 떠다니는 빛나는 해파리')
def _(c):
    c.shape(c.ell(12,9,7,5.5),'#ff8fd0');c.shape(c.rect(5,9,19,11),'#ff8fd0')
    c.shape(c.ell(12,7,4,2.2),'#ffd0ee',shade=False)
    for i,x in enumerate([6.5,9.5,12.5,15.5,18]):
        for k in range(8):R(c,x+math.sin(k*.9+i)*.7,12+k*1.1,'#e070c0' if k%2 else '#ffb0e0')
    eye(c,9.5,9);eye(c,13.5,9);blush(c,8,11);blush(c,15,11)
@pet('cyclocat','외눈 고양이','sf','커다란 눈 하나로 무엇이든 꿰뚫어 보는 고양이')
def _(c):
    c.shape(c.poly([(9,20.5),(16,20.5),(19,23),(20,17),(19,13)]),'#7ac870')
    c.shape(c.ell(12,16,6,4.8),'#8ad880')
    c.shape(c.ell(12,10,6,5),'#9ae890')
    c.shape(c.poly([(6.5,7),(7,2.5),(10,5.5)]),'#7ac870');c.shape(c.poly([(14,5.5),(17,2.5),(17.5,7)]),'#7ac870')
    c.shape(c.ell(12,10,3,3),'#f2fbe8',shade=False);c.shape(c.ell(12,10.3,1.6,1.8),'#2a1a3a',shade=False);R(c,11.4,9.4,'#ffffff')
    c.line(10,13.6,14,13.6,'#3a5a30')
    for x in (8,15):c.shape(c.rect(x,19.5,x+1.5,21.5),'#6ab860',shade=False)
@pet('crylizard','결정 도마뱀','sf','등에 은하결정이 자라는 작은 도마뱀')
def _(c):
    c.shape(c.poly([(2,18),(6,16),(9,17),(6,19)]),'#e0a050')
    c.shape(c.ell(12,16.5,6.5,3),'#f0b860')
    c.shape(c.ell(19,14.5,3.5,2.8),'#f8c870')
    for x,h,col in [(8,4,'#9ae8ff'),(11,6,'#c8a0ff'),(14,5,'#9ae8ff'),(17,3,'#c8a0ff')]:c.shape(c.poly([(x-1.3,14.5),(x,14.5-h),(x+1.3,14.5)]),col)
    for x in (8,11,14,16):c.shape(c.rect(x,18.5,x+1.2,20.5),'#d09040',shade=False)
    eye(c,19.5,13.5);R(c,22,15.5,'#ff8fb8')
@pet('sporeling','포자 꼬마','sf','머리에서 반짝이는 포자를 퐁퐁 뿜는 버섯 친구')
def _(c):
    c.shape(c.ell(12,9,8.5,5.5),'#d0505a');c.shape(c.rect(3.5,9,20.5,11),'#d0505a')
    for x,y,r in [(8,7,1.3),(14,6,1.6),(17.5,9,1),(10.5,10,.9)]:c.shape(c.ell(x,y,r,r),'#f8e8d0',shade=False)
    c.shape(c.ell(12,15.5,5,5),'#f2e2c8')
    eye(c,9.5,14.5);eye(c,13.5,14.5);blush(c,8,17);blush(c,15,17)
    for x,y in [(5,3),(19,2.5),(12,1.5)]:R(c,x,y,'#c8ff9a')
    for x in (9,14):c.shape(c.rect(x,20,x+1.5,21.5),'#d8c8a8',shade=False)
@pet('plasmoth','플라즈마 나방','sf','날개에 전기가 흐르는 푸른 나방')
def _(c):
    for s in (-1,1):
        c.shape(c.poly([(12,11),(12+9*s,4),(12+10.5*s,10),(12+7*s,14)]),'#3f7ad8')
        c.shape(c.poly([(12,14),(12+7.5*s,15),(12+6*s,20),(12+2*s,18)]),'#5f9af0')
        c.shape(c.ell(12+6.5*s,9,1.6,1.6),'#e8fbff',shade=False)
        c.line(12+2*s,11,12+8*s,6,'#bfefff')
    c.shape(c.ell(12,14,1.8,6),'#2a2050')
    c.line(11,8,9,4,'#bfefff');c.line(13,8,15,4,'#bfefff')
    eye(c,11,10,big=False);eye(c,12.6,10,big=False)
@pet('moonbun','달토끼','sf','더듬이 같은 귀로 우주 전파를 듣는 토끼')
def _(c):
    c.shape(c.ell(12,16,6,5),'#e8e4f4')
    c.shape(c.ell(12,10.5,5.5,4.5),'#f2eefa')
    for x in (9,15):
        c.shape(c.rect(x-.8,2.5,x+.8,7),'#e0dcf0');c.shape(c.rect(x-.3,3.5,x+.3,6.5),'#ffb0d0',shade=False)
        c.shape(c.ell(x,2,1.2,1.2),'#ffd65f',shade=False)
    eye(c,9.5,10);eye(c,13.5,10);blush(c,8,12.5);blush(c,15,12.5);R(c,11.8,12,'#ff8fb8')
    c.shape(c.ell(18,17,1.6,1.6),'#ffffff',shade=False)
@pet('voiddrake','공허 아기용','sf','블랙홀 근처에서 태어났다는 아기 용')
def _(c):
    for s in (-1,1):c.shape(c.poly([(12+2*s,11),(12+9*s,5),(12+8.5*s,12),(12+4*s,15)]),'#5a3a8a')
    c.shape(c.poly([(15,19),(20,21),(22,18),(18,17)]),'#3a2860')
    c.shape(c.ell(12,15.5,5,5),'#4a3478')
    c.shape(c.ell(12,16.5,2.8,3.5),'#c8a0ff',shade=False)
    c.shape(c.ell(12,9,4.8,4),'#5a4290')
    c.shape(c.poly([(8.5,6.5),(8,3),(10,5.5)]),'#ffd65f');c.shape(c.poly([(14,5.5),(16,3),(15.5,6.5)]),'#ffd65f')
    eye(c,9.8,8.5,'#ffd65f','#fff6c8');eye(c,13,8.5,'#ffd65f','#fff6c8')
# ---------------- robots ----------------
@pet('propdrone','프로펠러 드론','robot','작은 프로펠러로 머리 위를 맴도는 정찰 드론')
def _(c):
    c.line(4,5,10,5,'#c4c7d4');c.line(14,5,20,5,'#c4c7d4');c.shape(c.rect(11,4,13,7),'#5d6274')
    c.shape(c.ell(12,12,6.5,5),'#e0a040')
    c.shape(c.rect(7.5,10,16.5,14),'#1a1c28',shade=False)
    screen_eye(c,9.5,10.8,'#7fe8ff');screen_eye(c,13.5,10.8,'#7fe8ff')
    c.line(9,17,8,20,'#7a8098');c.line(15,17,16,20,'#7a8098')
@pet('vacbot','동글 청소봇','robot','바닥 먼지를 찾아 동글동글 굴러다니는 청소 로봇')
def _(c):
    c.shape(c.ell(12,15,9,5),'#c4c7d4');c.shape(c.ell(12,13.5,7,3),'#e8eaf0',shade=False)
    c.shape(c.rect(8,13,16,14.5),'#2a2d3a',shade=False)
    screen_eye(c,9.5,12.6,'#7dff9b');screen_eye(c,13.5,12.6,'#7dff9b')
    c.shape(c.rect(3,17,21,18.5),'#5d6274',shade=False)
    R(c,12,10,'#ff5f6a');c.line(12,10,12,8,'#9aa0b4')
    for x in (5,9,13,17):R(c,x,19,'#8a8ea6')
@pet('robopup','로봇 강아지','robot','꼬리 대신 안테나를 흔드는 충직한 강아지')
def _(c):
    c.line(19,12,22,8,'#9aa0b4');R(c,22,7.5,'#ff5f6a')
    c.shape(c.rect(8,12,19,17),'#b0b8c8')
    for x in (8.5,12,15.5,18):c.shape(c.rect(x,17,x+1.5,21),'#6a7088')
    c.shape(c.rect(2,7,10,13),'#c8d0dc')
    c.shape(c.poly([(2,7),(1,11),(3.5,10)]),'#6a7088');c.shape(c.poly([(9,7),(11,11),(8.5,10)]),'#6a7088')
    c.shape(c.rect(1,10.5,4,12.5),'#9aa0b4')
    screen_eye(c,4.5,8.5,'#5fd8ff');screen_eye(c,7.5,8.5,'#5fd8ff')
    c.shape(c.rect(10,13.5,17,14.5),'#5fd8ff',shade=False)
@pet('spiderbot','거미 정비봇','robot','여덟 다리로 우주선 틈새를 기어 다니는 정비봇')
def _(c):
    for s in (-1,1):
        for k,(a,b) in enumerate([(6,8),(8,12),(8,16),(6,20)]):c.line(12+3*s,12+k*1.2,12+a*s+1.5*s,b,'#5d6274');c.line(12+a*s+1.5*s,b,12+(a+2)*s,b+2.5,'#3a3e4c')
    c.shape(c.ell(12,13,5,4.5),'#d04050')
    c.shape(c.ell(12,11,3.5,2),'#ff7a7a',shade=False)
    c.shape(c.rect(8.5,12.5,15.5,15),'#1a1c28',shade=False)
    for x in (9.5,11.5,13.5):eye(c,x,13.2,'#ffd65f','#fff6c8')
@pet('orbsat','고리 위성구','robot','작은 고리를 두르고 둥실 떠 있는 위성 구체')
def _(c):
    c.shape(c.ell(12,11,6,6),'#7a6fd0')
    c.shape(c.ell(10,9,2.5,2),'#b0a8ff',shade=False)
    for a in range(0,360,4):
        t=math.radians(a);x=12+10*math.cos(t);y=12.5+2.2*math.sin(t)
        if math.sin(t)>0 or abs(x-12)>5.6:R(c,x,y,'#ffd65f' if math.sin(t)>0 else '#c89a30')
    c.shape(c.rect(9.5,10.5,14.5,12.5),'#1a1c28',shade=False)
    screen_eye(c,10.4,10.8,'#7fe8ff');screen_eye(c,12.8,10.8,'#7fe8ff')
    R(c,12,20,'#5fd8ff');R(c,12,21.5,'#3f8ab8')
@pet('tankbot','캐터필러 탱크봇','robot','무한궤도로 어디든 밀고 가는 꼬마 탱크')
def _(c):
    c.shape(c.rect(3,16,21,20.5),'#3a3e4c')
    for x in range(4,21,3):c.shape(c.ell(x,18.3,1.1,1.1),'#8a8ea6',shade=False)
    c.shape(c.rect(6,9.5,18,16),'#6a8a50')
    c.shape(c.rect(8,11,16,14),'#1a1c28',shade=False)
    screen_eye(c,9.5,11.6,'#ffb35f');screen_eye(c,13.5,11.6,'#ffb35f')
    c.shape(c.rect(17,10.5,22,11.8),'#4a6a3a');c.line(9,9.5,8,6,'#9aa0b4');R(c,8,5.5,'#7dff9b')
@pet('robocat','기계 고양이','robot','태엽을 감아 주면 골골송을 부르는 고양이')
def _(c):
    c.line(18,18,21,13,'#9aa0b4');c.line(21,13,20,11,'#9aa0b4')
    c.shape(c.ell(12,16.5,6,4),'#2a2d3a')
    c.shape(c.rect(6.5,6.5,17.5,13.5),'#3a3e4c')
    c.shape(c.poly([(6.5,6.5),(7,2.5),(10,6.5)]),'#3a3e4c');c.shape(c.poly([(14,6.5),(17,2.5),(17.5,6.5)]),'#3a3e4c')
    c.shape(c.rect(8,8,16,12),'#101218',shade=False)
    screen_eye(c,9.5,8.8,'#ff8fd0');screen_eye(c,13.5,8.8,'#ff8fd0')
    c.shape(c.ell(5,15,1.5,1.5),'#ffd65f');c.line(3.5,15,6.5,15,'#a8862a')
    for x in (8,14.5):c.shape(c.rect(x,19.5,x+1.5,21.5),'#1a1c28',shade=False)
@pet('wrenchbot','렌치 팔 수리봇','robot','한쪽 팔이 렌치인 부지런한 수리 로봇')
def _(c):
    c.shape(c.rect(8,7,16,13),'#e0d0a0')
    c.shape(c.rect(9,8.5,15,11.5),'#1a1c28',shade=False)
    screen_eye(c,10,9,'#7dff9b');screen_eye(c,13,9,'#7dff9b')
    c.shape(c.rect(7,13.5,17,19),'#c07a3a')
    c.line(17,15,21,12,'#9aa0b4');c.shape(c.poly([(20,9.5),(22.5,10),(22,12.5),(20.5,11.5)]),'#c4c7d4')
    c.line(7,15,4,18,'#9aa0b4');c.shape(c.ell(3.5,18.5,1.2,1.2),'#c4c7d4')
    c.shape(c.rect(8,19,10,21.5),'#5d6274');c.shape(c.rect(14,19,16,21.5),'#5d6274')
    c.line(12,7,12,4.5,'#9aa0b4');R(c,12,4,'#ffd65f')
@pet('holopeng','홀로 펭귄','robot','투명한 홀로그램으로 만들어진 펭귄 안내봇')
def _(c):
    c.shape(c.ell(12,13,6,7.5),'#3fa9d8')
    c.shape(c.ell(12,14.5,3.8,5.5),'#c8f4ff',shade=False)
    for s in (-1,1):c.shape(c.poly([(12+5.5*s,11),(12+8*s,15),(12+5*s,16)]),'#2f8ab8')
    eye(c,10,9.5,'#0a2a40');eye(c,13,9.5,'#0a2a40');c.shape(c.poly([(11,11.5),(13,11.5),(12,13)]),'#ffd65f')
    c.shape(c.rect(4,21,20,22),'#5fd8ff',shade=False)
    for y in (6,10,14,18):
        for x in range(6,19,2):
            if c.get(int(x*K),int(y*K)):R(c,x,y,'#9ae8ff')
@pet('minimech','미니 메카','robot','작지만 우주 해적도 도망가는 꼬마 전투 메카')
def _(c):
    c.shape(c.rect(7,9,17,16),'#e8e4dc')
    c.shape(c.rect(9,10.5,15,13),'#d04050',shade=False)
    screen_eye(c,10,11,'#fff6c8');screen_eye(c,13,11,'#fff6c8')
    c.shape(c.rect(3,10,7,14),'#4a6aa8');c.shape(c.rect(17,10,21,14),'#4a6aa8')
    c.shape(c.rect(2,14,6,17),'#c4c7d4');c.shape(c.rect(18,14,22,17),'#c4c7d4')
    c.shape(c.rect(8,16,11,21),'#4a6aa8');c.shape(c.rect(13,16,16,21),'#4a6aa8')
    c.shape(c.rect(7,20.5,11.5,22),'#3a3e4c');c.shape(c.rect(12.5,20.5,17,22),'#3a3e4c')
    c.shape(c.poly([(10,9),(12,4),(14,9)]),'#ffd65f')
out={}
for i,(n,kind,d,f) in D.items():
    c=C();f(c);c.outline();out[i]=[n,kind,d,c.png()]
json.dump(out,open(P+'pets.json','w'),ensure_ascii=False);print(len(out))
