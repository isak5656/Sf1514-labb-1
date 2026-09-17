import numpy as np
import matplotlib.pyplot as plt


#importerar data
y = np.loadtxt("KPI.csv", delimiter=",", skiprows=3, usecols=1)
t = np.arange(y.size) / 12
#plottar en graf med grid, labels och data från KPI

I = (t+1980 >= 1991) & (t+1980 < 2021)
t = t[I]
y = y[I]

p = np.polynomial.Polynomial.fit(t, y, 1) #minsta kvadrat till funktionen
plt.plot(t+1980, y)
plt.plot(t+1980, p(t))
plt.ylabel("KPI")
plt.xlabel("År")
plt.grid()
plt.show()

# Erms fel funktion 
def E_rms(f, y, z):
    E = 0
    N = 360 # eller len(x)
    for i in range(N):
        E += ((f[i]) - (y[i]))**2
    print(z)
    print(np.sqrt(E/360))

E_rms(p(t), y, "erms felet för kvadratmetoden")

#plot för modellfelet med differanser av varje punkt
def M_fel(f, y, ettiket):
    E = []
    N = len(t)
    for i in range(N):
        E.append((f[i]) - (y[i]))
    plt.plot(t+1980, E, label= ettiket)
    plt.grid()
    plt.legend()
    plt.show()
M_fel(p(t), y, "kvadratmetoden")

"""uppgift B"""
L = 8
e = np.ones(t.shape)
A = np.column_stack((e, t, np.sin((2*np.pi*t)/L), np.cos((2*np.pi*t)/L)))
#bygger en matris
#löser 
d = np.linalg.lstsq(A, y)[0]
print(d)
#löser ut en vektor d som gånger A blir lika med våra y värden.

ny_funktion = A @ d #matris multiplikation för att få ut grafens värden i vektor
plt.plot(t+1980, y)
plt.plot(t+1980, ny_funktion)
plt.ylabel("KPI")
plt.xlabel("År")
plt.grid()
plt.show()

E_rms(ny_funktion, y, "Erms felet för sin/cos funktionen") 
#beräknar ems felet

#modellfel och plot för sin/kos modellen
M_fel(ny_funktion, y, "sin/kos funktionens fel")


#uppgift c
"""gaus newton""" #95.3 är x0 alltså det första värdet
print('\nd) Gauss-Newton')
F = lambda x0, k: x0*np.exp(-k*t) - x
J = lambda x0, k: np.column_stack((
np.exp(-k*t),
(-t)*x0*np.exp(-k*t),
))
k = ny_funktion[0]
cGN = np.array([k]) # startgissning fr˚an tidigare modell
tol = 1e-12
diff = np.array([1])
it = 0
maxiter = 100
while np.linalg.norm(diff) > tol and it < maxiter:
    Jmat = J(cGN[0]).reshape(-1, 1) # omforma som kolumnvektor
    Fval = F(cGN[0])
    diff = -np.linalg.lstsq(Jmat, Fval)[0]
    cGN += diff
    it += 1
    print(it, cGN, np.linalg.norm(diff))
kGN = cGN[0]
print('k =', kGN)
