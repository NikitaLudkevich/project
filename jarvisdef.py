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
obolochka=[]
xwindowsize=300
ywindowsize=300
alldots=[]
dotsin=[]
dotsout=[]
f=open('picture.svg','w')
f.write("<?xml version='1.0' encoding='utf-8'?>\n")
f.write("<svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='{xwindowsize}px' height='{ywindowsize}px'>\n")
for i in range(100):
    coordsnew=[]
    coordsnew.append(random()*xwindowsize)
    coordsnew.append(random()*ywindowsize)
    alldots.append(coordsnew)
    if coordsnew[0]>=xwindowsize/3 and coordsnew[0]<=xwindowsize/1.2 and coordsnew[1]>=xwindowsize/3 and coordsnew[1]<=xwindowsize/1.2:
        dotsin.append(coordsnew)
        f.write(f"<circle cx='{coordsnew[0]}' cy='{coordsnew[1]}' r='2' stroke='green' fill='green'/>\n")
    else:
        dotsout.append(coordsnew)
        f.write(f"<circle cx='{coordsnew[0]}' cy='{coordsnew[1]}' r='2' stroke='red' fill='red'/>\n")
obolochka=jarvismarch(dotsin)
    # for i in obolochka:
    #     f.write(f"<circle cx='{i[0]}' cy='{i[1]}' r='4' stroke='green' fill='green'/>\n")
for i in range(len(obolochka)-1):
    f.write(f'<line x1="{obolochka[i][0]}" y1="{obolochka[i][1]}" x2="{obolochka[i+1][0]}" y2="{obolochka[i+1][1]}" stroke="black" stroke-width="2" /> \n')
f.write(f'<line x1="{obolochka[0][0]}" y1="{obolochka[0][1]}" x2="{obolochka[-1][0]}" y2="{obolochka[-1][1]}" stroke="black" stroke-width="2"  /> \n')
f.write("</svg>")
print(alldots)
f.close()