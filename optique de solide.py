"""
par: Arfaoui mehdi

proportes optique des solides

Modele de Drude-Lorentz

Delectrique( w0!=0, gamma !=0)

"""
import matplotlib.pyplot as plt
import numpy as np


#variable

epsistat=12.1#epsilon(r)(w tend vers 0)
epsinf=10#epsilon(r)(w tend vers oo)
gamma=5.0e12#s-1
w0=1.0e14#s-1 frequence de resonnance
epsi0=8.85418782e-12 #F.m−1
wp2=w0**2*(epsistat-epsinf)#frequence de plasma au carree
#
dw= np.linspace(-6*w0,6*w0,20)
w= np.linspace(0.,2*w0,10)
def eps1(ddw):
    return epsinf-(epsistat-epsinf)*(2*w0*dw)/(4*(dw**2)+gamma**2)
def eps2(ddw):
    return (epsistat-epsinf)*(gamma*w0)/(4*(dw**2)+gamma**2)
#def epsi1(ww):
#   return epsinf+(wp2*(w0**2-w**2))/((w0**2-w**2)**2-(gamma*w)**2)
#def epsi2(ww):
#    return wp2*gamma*w/((w0**2-w**2)**2-(gamma*w)**2)
#representation graphique
fig=plt.figure()


#fig1
sub1=plt.subplot(121)
sub1.set_title(r'$\epsilon_1= \Re(\epsilon_r)=\epsilon_\infty-(\epsilon_{stat}-\epsilon_\infty)\frac{(2\times\omega_0\vartriangle\omega)}{(4\times(\vartriangle\omega^2)+\gamma^2)}$')
plt.xlabel(r'$\vartriangle\omega= ( \omega-\omega_0)$',rotation=0)
plt.ylabel(r'$\epsilon_1= \Re(\epsilon_r)$',rotation=90)
plt.plot(dw,eps1(dw))
#dw=0

plt.xticks([0.], [r'$\vartriangle\omega= 0$'])
plt.axvline(x=0,color='r', linestyle='--')

plt.grid('True')
#fig2
sub2=plt.subplot(122)
sub2.set_title(r'$\epsilon_2= \Im(\epsilon_r)=(\epsilon_{stat}-\epsilon_\infty)\frac{(\gamma\omega_0)}{(4\times(\vartriangle\omega^2)+\gamma^2)}$')
plt.xlabel(r'$\vartriangle\omega= ( \omega-\omega_0)$',rotation=0)
plt.ylabel(r'$\epsilon_2= \Im(\epsilon_r)$',rotation=90)
plt.axvline(x=0,color='k', linestyle='--')


plt.plot(dw,eps2(dw))
#fig3 re (epsi )=f(w)
#sub3=plt.subplot(223)
#plt.plot(w,epsi1(w))
#♦fig4 Im(epsi )=f(w)
#sub4=plt.subplot(224)
#plt.plot(w,epsi2(w))
#plt.plot(dw,np.sqrt((0.5*(np.sqrt(eps1(dw)**2+eps2(dw)**2)+eps1(dw)))))

#fig5
#sub5=plt.subplot(133)
#plt.plot(dw,np.sqrt((0.5*(np.sqrt(eps1(dw)**2+eps2(dw)**2)+eps1(dw)))))

plt.grid('True')
plt.show()





