"""
par: Arfaoui mehdi

proportes optique des solides

Modele de Drude-Lorentz

Delectrique( w0!=0, gamma !=0)

"""
import matplotlib.pyplot as plt
import numpy as np


#donnee

epsistat=12.1#epsilon(r)(w tend vers 0)
epsinf=10#epsilon(r)(w tend vers oo)
gamma=5.0e12#s-1
w0=1.0e14#s-1 frequence de resonnance
epsi0=8.85418782e-12 #F m−1
wp2=w0**2*(epsistat-epsinf)#frequence de plasma au carree

dw= np.linspace(0.,2*w0,10)
w= np.linspace(0.,2*w0,20)
def eps1(ddw):
    return epsinf-(epsistat-epsinf)*(2*w0*dw)/(4*(dw**2)+gamma**2)
def eps2(ddw):
    return (epsistat-epsinf)*(gamma*w0)/(4*(dw**2)+gamma**2)
def epsi1(ww):
    return epsinf+(wp2*(w0**2-w**2))/((w0**2-w**2)**2-(gamma*w)**2)
def epsi2(ww):
    return wp2*gamma*w/((w0**2-w**2)**2-(gamma*w)**2)
#representation graphique
fig=plt.figure()


#fig1
sub1=plt.subplot(121)
sub1.set_title(r'$\epsilon_1= \Re(\epsilon_r)=\epsilon_\infty+\frac{\omega_p^2(\omega_0^2-\omega^2)}{((\omega_0^2-\omega^2)^2+(\gamma\omega)^2)}$')
plt.xlabel(r'$\omega$',rotation=0)
plt.ylabel(r'$\epsilon_1= \Re(\epsilon_r)$',rotation=90)
plt.plot(w,epsi1(w))
plt.axvline(x=w0,color='k', linestyle='--')
plt.grid('True')
#fig2
sub2=plt.subplot(122)
sub2.set_title(r'$\epsilon_2= \Im(\epsilon_r)=\frac{\omega_p^2\gamma\omega}{((\omega_0^2-\omega^2)^2+(\gamma\omega)^2)}$')
plt.xlabel(r'$\omega$',rotation=0)
plt.ylabel(r'$\epsilon_2= \Im(\epsilon_r)$',rotation=90)
plt.axvline(x=w0,color='k', linestyle='--')

plt.plot(w,epsi2(w))


plt.grid('True')
plt.show()

