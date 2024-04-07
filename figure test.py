from random import *
def checkturn(dots1,dots2,dots3):
    return (dots2[0]-dots1[0])*(dots3[1]-dots2[1])-(dots2[1]-dots1[1])*(dots3[0]-dots2[0])
def jarvismarch(alldots):
    n = len(alldots)
    for i in range(1,n):
        if alldots[i][0]<alldots[0][0]: 
            alldots[i], alldots[0] = alldots[0], alldots[i]  
    obolochkadots = [alldots[0]]
    del alldots[0]
    alldots.append(obolochkadots[0])
    while True:
        right = 0
        for i in range(1,len(alldots)):
            if checkturn(obolochkadots[-1],alldots[right],alldots[i])<0:
                right = i
        if alldots[right]==obolochkadots[0]: 
            break
        else:
            obolochkadots.append(alldots[right])
            del alldots[right]
    return obolochkadots
xwindowsize=500
ywindowsize=500
f=open('picture.svg','w')
f.write("<?xml version='1.0' encoding='utf-8'?>\n")
f.write("<svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='{xwindowsize}px' height='{ywindowsize}px'>\n")
alldots=[]
dotspassed=[]
randomdots=[]
for i in range(5000): #колво точек (можно менять)
    alldots.append([random()*300+50,random()*300+50])
for i in range(10000): #колво точек вне оболочки(можно менять)
    randomdots.append([random()*500,random()*500])
# alldots=[[100,100],[150,200],[200,100]]
# alldots=[[0,100],[0,200],[125,300],[250,200],[250,100],[125,0]]
obolochka=jarvismarch(alldots)
# for i in randomdots:
#     if i not in dotspassed:
#         f.write(f"<circle cx='{i[0]}' cy='{i[1]}' r='2' stroke='green' fill='green'/>\n")
#     else:
#         f.write(f"<circle cx='{i[0]}' cy='{i[1]}' r='2' stroke='red' fill='red'/>\n")
for i in range(len(obolochka)-1):
    f.write(f'<line x1="{obolochka[i][0]}" y1="{obolochka[i][1]}" x2="{obolochka[i+1][0]}" y2="{obolochka[i+1][1]}" stroke="black" stroke-width="1" />')
for i in range(len(obolochka)-1):
    f.write(f'<line x1="{obolochka[i][0]}" y1="{obolochka[i][1]}" x2="{obolochka[i+1][0]}" y2="{obolochka[i+1][1]}" stroke="black" stroke-width="1" />')
for i in obolochka:
    f.write(f"<circle cx='{i[0]}' cy='{i[1]}' r='3' stroke='orange' fill='orange'/>\n")
for i in range(len(obolochka)-1):
    f.write(f'<line x1="{obolochka[i][0]}" y1="{obolochka[i][1]}" x2="{obolochka[i+1][0]}" y2="{obolochka[i+1][1]}" stroke="black" stroke-width="1" />')
f.write(f'<line x1="{obolochka[0][0]}" y1="{obolochka[0][1]}" x2="{obolochka[-1][0]}" y2="{obolochka[-1][1]}" stroke="black" stroke-width="1" />')
for i in alldots:
    if i not in obolochka:
        f.write(f"<circle cx='{i[0]}' cy='{i[1]}' r='3' stroke='green' fill='green'/>\n")
xmin=999999
ymin=999999
xmax=-999999
ymax=-999999
for i in obolochka:
    if i[0]>xmax:
        xmax=i[0]
    if i[0]<xmin:
        xmin=i[0]
    if i[1]>ymax:
        ymax=i[1]
    if i[1]<ymin:
        ymin=i[1]
f.write(f'<line x1="{xmin}" y1="{ymin}" x2="{xmin}" y2="{ymax}" stroke="black" stroke-width="3" />')
f.write(f'<line x1="{xmin}" y1="{ymax}" x2="{xmax}" y2="{ymax}" stroke="black" stroke-width="3" />')
f.write(f'<line x1="{xmax}" y1="{ymax}" x2="{xmax}" y2="{ymin}" stroke="black" stroke-width="3" />')
f.write(f'<line x1="{xmax}" y1="{ymin}" x2="{xmin}" y2="{ymin}" stroke="black" stroke-width="3" />')
squareplosh=(xmax-xmin)*(ymax-ymin)
xsred=0
ysred=0
for i in obolochka:
    xsred+=i[0]
    ysred+=i[1]
xsred=xsred/len(obolochka)
ysred=ysred/len(obolochka)
randomdot=[xsred,ysred] #x3,y3
obolochkaplosh=0
for i in range(len(obolochka)-1):
    obolochkaplosh+=0.5*abs((obolochka[i+1][0]-obolochka[i][0])*(randomdot[1]-obolochka[i][1])-(randomdot[0]-obolochka[i][0])*(obolochka[i+1][1]-obolochka[i][1]))
print(squareplosh)
print(obolochkaplosh)
f.write(f"<circle cx='{randomdot[0]}' cy='{randomdot[1]}' r='2' stroke='purple' fill='purple'/>\n")
if obolochkaplosh/squareplosh*100>68: #66<x
    print('Квадрат')
    figurename='Square'
    print(obolochkaplosh/squareplosh*100,'%')
elif obolochkaplosh/squareplosh*100<40: #33<x
    print('Треугольник')
    figurename='Triangle'
    print(obolochkaplosh/squareplosh*100,'%')
else: #33>x
    print('Круг')
    figurename='Circle'
    print(obolochkaplosh/squareplosh*100,'%')
fillpercent=str(round(obolochkaplosh/squareplosh*100,3))+'%'
f.write(f'<text x="{xsred}" y="{ymax+20}" font-size="20" fill="black">{figurename}</text> \n')
f.write(f'<text x="{xsred}" y="{ymax+40}" font-size="20" fill="black">{fillpercent}</text> \n')
f.write("</svg>")
f.close()
# print(obolochka)