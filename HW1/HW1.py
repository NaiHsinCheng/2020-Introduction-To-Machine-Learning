"""
   Author：B062040027 鄭乃心 / B0620400 張詠晴
   Date：2020.09.16
   Purpose：機器學習導論Homework#1
"""
import numpy as np
import matplotlib.pyplot as plt

#輸入方程式係數
while True:
    a = list()
    myInput =input("Input the coefficient of a third-order equation: (format a, b, c, d)\n")
    try:
        for myInput in myInput.split(','):
            b = float(myInput)
            a.append(b)
        if len(a) != 4:
            print("Input Error. Please input again.\n")
        else:
            break;
    except:
        print("Input Error. Please input again.\n")

#輸入任意點數
while True:
    pointX = list()
    pointY = list()
    myInput =input("Input the coefficient of points:\n")
    try:
        for i in range(len(myInput.split(','))):
            if i%2==0 :
                temp = float(myInput.split(',')[i])
                pointX.append(temp)
            else:
                temp = float(myInput.split(',')[i])
                pointY.append(temp)
        if len(pointX) != len(pointY):
            print("Input Error. Please input again.\n")
        else:
            break;
    except:
        print("Input Error. Please input again.\n")

#分類點數位置 綠紅藍
redX=list();redY=list()
blueX=list();blueY=list()
greenX=list();greenY=list()

def F(x):
    y=a[0]*(x**3) + a[1]*(x**2) + a[2]*x + a[3]
    return y

for i in range(len(pointX)):
    if F(pointX[i]) < pointY[i]:
        greenX.append(pointX[i])
        greenY.append(pointY[i])
    elif F(pointX[i]) > pointY[i]:
        blueX.append(pointX[i])
        blueY.append(pointY[i])
    else:
        redX.append(pointX[i])
        redY.append(pointY[i])



plt.figure(1)           #創建圖形
p1=plt.subplot(2,2,1)   #第一列第一行圖形
p2=plt.subplot(2,2,2)   #第一列第二行圖形
p3=plt.subplot(2,2,3)
p4=plt.subplot(2,2,4)

#方程式紫色曲線
plt.sca(p1)
x = np.linspace(-10,10,100)
y = F(x)
plt.plot(x,y,color='purple')
plt.title("line")

#三色點
plt.sca(p2)
plt.plot(x,y,color='purple')
plt.plot(greenX,greenY,'g.')
plt.plot(blueX,blueY,'b.')
plt.plot(redX,redY,'r.')
plt.title("point")

#找最小值
def slope(x):
    return 3*a[0]*(x**2)+2*a[1]*x+a[2]

startX=5
alpha=0.1
epsilon=1e-8
minX=[startX]
while True:
    update=slope(startX)
    lastX=startX
    startX=startX-alpha*update
    if startX>10 or startX<-10:
        break
    minX.append(startX)
    if abs(float(F(lastX)-F(startX)))<epsilon:
        break

print("Min:[",minX[len(minX)-1],',',F(minX[len(minX)-1]),']')

plt.sca(p3)
plt.plot(x,y,color='purple')
plt.plot(np.array(minX),F(np.array(minX)),'r.')
plt.title("min")

#找最大值
startXX=5
maxX=[startXX]
while True:
    update=slope(startXX)
    lastXX=startXX
    startXX=startXX+alpha*update
    if startXX>10 or startXX<-10:
        break
    maxX.append(startXX)
    if abs(float(F(lastXX)-F(startXX)))<epsilon:
        break

print("Max:[",maxX[len(maxX)-1],',',F(maxX[len(maxX)-1]),']')

plt.sca(p4)
plt.plot(x,y,color='purple')
plt.plot(np.array(maxX),F(np.array(maxX)),'r.')
plt.title("max")

plt.show()
