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

rf1 = refCycle(ref,32,evapTemp,condTemp,condTemp-subcoolDegree)
rf2 = refCycle(ref,27,evapTemp,condTemp,condTemp-subcoolDegree)
rf3 = refCycle(ref,22,evapTemp,condTemp,condTemp-subcoolDegree)
density1 = rf1.denSuction()
density2 = rf2.denSuction()
density3 = rf3.denSuction()
plt.figure(figsize=(10, 5))
plt.plot(evapTemp, density1,label = "Suction Temp. =32℃",linestyle='dashdot',marker = "v",color ="red")
plt.plot(evapTemp, density2,label = "Suction Temp. = 27℃",linestyle=':',marker = "x",color ="blue")
plt.plot(evapTemp, density3,label = "Suction Temp. = 22℃",linestyle='--',marker = "d",color ="green")
plt.xlabel("Evaporating Temperature(centigrade)")
plt.ylabel('Gas suction density(kg/m^3)')
plt.savefig('fig1.png',dpi=75)
plt.legend()
plt.show()
