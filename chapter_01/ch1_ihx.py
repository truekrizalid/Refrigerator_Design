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
condTemp = 40
evapTemp = np.linspace(-30,-20,21)
Eihx = np.linspace(0.75,0.95,3)
qv = np.zeros(3*21).reshape(3,21)
wv = np.zeros(3*21).reshape(3,21)
COP = np.zeros(3*21).reshape(3,21)
for i in range(len(Eihx)):
    for j in range(len(evapTemp)):
        Tsuct = suctionTemp(condTemp,evapTemp[j],subcoolDegree,Eihx[i])
        rf = refCycle(ref,Tsuct,evapTemp[j],condTemp,condTemp-subcoolDegree)
        qv[i,j] =rf.denSuction()*rf.qe()/1000.0
        wv[i,j] = rf.denSuction()*rf.wc()/1000.0
        COP[i,j] = rf.cycleCOP()



plt.figure(figsize=(10, 5))
plt.plot(evapTemp, qv[0,:],label = "Eihx = %f"%Eihx[0],linestyle='dashdot',marker = "v",color ="red")
plt.plot(evapTemp, qv[1,:],label = "Eihx = %f"%Eihx[1],linestyle=':',marker = "x",color ="blue")
plt.plot(evapTemp, qv[-1,:],label = "Eihx = %f"%Eihx[2],linestyle='--',marker = "d",color ="green")
plt.xlabel("Evaporating Temperature(centigrade)")
plt.ylabel('capacity per volume(KJ/m^3)')
plt.legend()
plt.savefig('Eihx1.png',dpi=75)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(evapTemp, wv[0,:],label = "Eihx = %f"%Eihx[0],linestyle='dashdot',marker = "v",color ="red")
plt.plot(evapTemp, wv[1,:],label = "Eihx = %f"%Eihx[1],linestyle=':',marker = "x",color ="blue")
plt.plot(evapTemp, wv[-1,:],label = "Eihx = %f"%Eihx[2],linestyle='--',marker = "d",color ="green")
plt.xlabel("Evaporating Temperature(centigrade)")
plt.ylabel('Effective compress work per volume(KJ/m^3)')

plt.legend()
plt.savefig('Eihx2.png',dpi=75)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(evapTemp, COP[0,:],label = "Eihx = %f"%Eihx[0],linestyle='dashdot',marker = "v",color ="red")
plt.plot(evapTemp, COP[1,:],label = "Eihx = %f"%Eihx[1],linestyle=':',marker = "x",color ="blue")
plt.plot(evapTemp, COP[-1,:],label = "Eihx = %f"%Eihx[2],linestyle='--',marker = "d",color ="green")
plt.xlabel("Evaporating Temperature(centigrade)")
plt.ylabel('CYCLE COP (w/w)')

plt.legend()
plt.savefig('CYCLE_COP_ihx.png',dpi=75)
plt.show()