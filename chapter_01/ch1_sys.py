import CoolProp.CoolProp as CP
from RefCycle import refCycle
from Compressor import compressor
import numpy as np
import scipy.linalg as alg
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def suctionTemp(Tk,Te,Tsub,eihx):
    return eihx*(Tk-Tsub-Te)+Te

# Data input
model = "VTH1113YA"
N = 1800 # rpm
cmp1 = compressor(model)
ref = "R600a"
subcoolDegree = 1.5
condTemp = np.linspace(35,45,3)
evapTemp = np.linspace(-30,-10,21)
Eihx = 0.85
q = np.zeros(3*21).reshape(3,21)
Pel = np.zeros(3*21).reshape(3,21)
COP_sys = np.zeros(3*21).reshape(3,21)
MassFlow = np.zeros(3*21).reshape(3,21)
for i in range(len(condTemp)):
    for j in range(len(evapTemp)):
        Tsuct = suctionTemp(condTemp[i],evapTemp[j],subcoolDegree,Eihx)
        rf = refCycle(ref,Tsuct,evapTemp[j],condTemp[i],condTemp[i]-subcoolDegree)
        q[i,j] =cmp1.mf(N,evapTemp[j],condTemp[i],Tsuct)*rf.qe()
        Pel[i,j] = cmp1.mf(N,evapTemp[j],condTemp[i],Tsuct)*rf.wc()/cmp1.isoEff(evapTemp[j],condTemp[i],N)
        COP_sys[i,j] = rf.cycleCOP()*cmp1.isoEff(evapTemp[j],condTemp[i],N)
        MassFlow[i,j]= cmp1.mf(N,evapTemp[j],condTemp[i],Tsuct)

plt.figure(figsize=(10, 5))
plt.plot(evapTemp, q[0,:],label = "Condensing Temp. =35℃",linestyle='dashdot',marker = "v",color ="red")
plt.plot(evapTemp, q[1,:],label = "Condensing Temp. = 40℃",linestyle=':',marker = "x",color ="blue")
plt.plot(evapTemp, q[-1,:],label = "Condensing Temp. = 45℃",linestyle='--',marker = "d",color ="green")
plt.xlabel("Evaporating Temperature(centigrade)")
plt.ylabel('capacity (W)')
plt.legend()
plt.savefig('capacity.png',dpi=75)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(evapTemp, Pel[0,:],label = "Condensing Temp. =35℃",linestyle='dashdot',marker = "v",color ="red")
plt.plot(evapTemp, Pel[1,:],label = "Condensing Temp. = 40℃",linestyle=':',marker = "x",color ="blue")
plt.plot(evapTemp, Pel[-1,:],label = "Condensing Temp. = 45℃",linestyle='--',marker = "d",color ="green")
plt.xlabel("Evaporating Temperature(centigrade)")
plt.ylabel('Input Power(W)')

plt.legend()
plt.savefig('Pel.png',dpi=75)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(evapTemp, COP_sys[0,:],label = "Condensing Temp. =35℃",linestyle='dashdot',marker = "v",color ="red")
plt.plot(evapTemp, COP_sys[1,:],label = "Condensing Temp. = 40℃",linestyle=':',marker = "x",color ="blue")
plt.plot(evapTemp, COP_sys[-1,:],label = "Condensing Temp. = 45℃",linestyle='--',marker = "d",color ="green")
plt.xlabel("Evaporating Temperature(centigrade)")
plt.ylabel('System COP (w/w)')

plt.legend()
plt.savefig('system_COP.png',dpi=75)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(evapTemp, MassFlow[0,:],label = "Condensing Temp. =35℃",linestyle='dashdot',marker = "v",color ="red")
plt.plot(evapTemp, MassFlow[1,:],label = "Condensing Temp. = 40℃",linestyle=':',marker = "x",color ="blue")
plt.plot(evapTemp, MassFlow[-1,:],label = "Condensing Temp. = 45℃",linestyle='--',marker = "d",color ="green")
plt.xlabel("Evaporating Temperature(centigrade)")
plt.ylabel('Refrigerant mass flow rate (kg/s)')
plt.legend()
plt.savefig('MassFlow',dpi=75)
plt.show()
