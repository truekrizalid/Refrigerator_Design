import CoolProp.CoolProp as CP
from RefCycle import refCycle
import numpy as np
import scipy.linalg as alg
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def suctionTemp(Tk,Te,Tsub,eihx):
    return eihx*(Tk-Tsub-Te)+Te

#定义系统循环：

ref = "R600a"
subcoolDegree = 1.5
condTemp = np.linspace(35,45,3)
evapTemp = np.linspace(-30,-10,21)
Eihx = 0.85
qv = np.zeros(3*21).reshape(3,21)
wv = np.zeros(3*21).reshape(3,21)
COP = np.zeros(3*21).reshape(3,21)
for i in range(len(condTemp)):
    for j in range(len(evapTemp)):
        Tsuct = suctionTemp(condTemp[i],evapTemp[j],subcoolDegree,Eihx)
        rf = refCycle(ref,Tsuct,evapTemp[j],condTemp[i],condTemp[i]-subcoolDegree)
        qv[i,j] =rf.denSuction()*rf.qe()/1000.0
        wv[i,j] = rf.denSuction()*rf.wc()/1000.0
        COP[i,j] = rf.cycleCOP()



plt.figure(figsize=(10, 5))
plt.plot(evapTemp, qv[0,:],label = "Condensing Temp. =35℃",linestyle='dashdot',marker = "v",color ="red")
plt.plot(evapTemp, qv[1,:],label = "Condensing Temp. = 40℃",linestyle=':',marker = "x",color ="blue")
plt.plot(evapTemp, qv[-1,:],label = "Condensing Temp. = 45℃",linestyle='--',marker = "d",color ="green")
plt.xlabel("Evaporating Temperature(centigrade)")
plt.ylabel('capacity per volume(KJ/m^3)')
plt.legend()
plt.savefig('fig2.png',dpi=75)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(evapTemp, wv[0,:],label = "Condensing Temp. =35℃",linestyle='dashdot',marker = "v",color ="red")
plt.plot(evapTemp, wv[1,:],label = "Condensing Temp. = 40℃",linestyle=':',marker = "x",color ="blue")
plt.plot(evapTemp, wv[-1,:],label = "Condensing Temp. = 45℃",linestyle='--',marker = "d",color ="green")
plt.xlabel("Evaporating Temperature(centigrade)")
plt.ylabel('Effective compress work per volume(KJ/m^3)')

plt.legend()
plt.savefig('fig3.png',dpi=75)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(evapTemp, COP[0,:],label = "Condensing Temp. =35℃",linestyle='dashdot',marker = "v",color ="red")
plt.plot(evapTemp, COP[1,:],label = "Condensing Temp. = 40℃",linestyle=':',marker = "x",color ="blue")
plt.plot(evapTemp, COP[-1,:],label = "Condensing Temp. = 45℃",linestyle='--',marker = "d",color ="green")
plt.xlabel("Evaporating Temperature(centigrade)")
plt.ylabel('CYCLE COP (w/w)')

plt.legend()
plt.savefig('CYCLE_COP.png',dpi=75)
plt.show()