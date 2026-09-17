import numpy as np
import matplotlib.pyplot as plt

"uppgift A"
#importerar data
print("\n det här är uppgift A")
y = np.loadtxt("Sf1514-labb-1/KPI.csv", delimiter=",", skiprows=3, usecols=1)
t = np.arange(y.size) / 12
#plottar en graf med grid, labels och data från KPI

I = (t+1980 >= 1991) & (t+1980 < 2021)
t = t[I]
y = y[I]

vektor_1 = np.ones(len(t)) # bygger vektor med 0 or
A = (np.column_stack((vektor_1, t))) # bygger matris
C = np.linalg.solve(A.T @ A, A.T @ y) #löser ut C för minsta kvadrat
c_1 = C[0] #utskrift av C värden
c_2 = C[1]
p = A @ C # får ut vektor med aprox y värden
#minsta kvadrat till funktionen den gör A^T*Ac = A^T*y f är sedan A*c
plt.plot(t+1980, y)
plt.plot(t+1980, p, label= "polynomial")
plt.ylabel("KPI")
plt.xlabel("År")
plt.legend()
plt.grid()
plt.show()

# Erms fel funktion 
def E_rms(f, y, z):
    E = 0
    N = 360 # eller len(x)
    for i in range(N):
        E += ((f[i]) - (y[i]))**2 #tar avtsåndet i kvardat
    print(z)
    print(np.sqrt(E/360)) # tar felet 

E_rms(p, y, "\nerms felet för kvadratmetoden") #skickar in i erms funktionen A@C y och text

#plot för modellfelet med differanser av varje punkt
def M_fel(f, y, ettiket):
    E = []
    N = len(t)
    for i in range(N):
        E.append((f[i]) - (y[i])) # värden minus varandra fake y och y
    plt.plot(t+1980, E, label= ettiket) # gör en graf med år och fel
    plt.grid()
    plt.legend()
    plt.show()

M_fel(p, y, "kvadratmetoden")

print(f"koficienterna är C1={c_1}, C2={c_2}")

"""uppgift B"""
print("\n\n Uppgift B")
L = 8
e = np.ones(t.shape)
A = np.column_stack((e, t, np.sin((2*np.pi*t)/L), np.cos((2*np.pi*t)/L)))
#bygger en matris
#löser 
d = np.linalg.lstsq(A, y)[0]
print("det här är d", d)
#löser ut en vektor d som gånger A blir lika med våra y värden.

ny_funktion = A @ d #matris multiplikation för att få ut grafens värden i vektor
plt.plot(t+1980, y) #plott vanlig funk
plt.plot(t+1980, ny_funktion, label= "newtons metod") #plot ny funktion
plt.ylabel("KPI")
plt.xlabel("År")
plt.grid()
plt.legend()
plt.show()

E_rms(ny_funktion, y, "Erms felet för sin/cos funktionen") 
#beräknar ems felet

#modellfel och plot för sin/kos modellen
M_fel(ny_funktion, y, "sin/kos funktionens fel")


#uppgift c
#gaus newton #95.3 är x0 alltså det första värdet

# metoden funkar som
print('\nd) Gauss-Newton')
F = lambda d0, d1, d2, d3, L: d0 + d1*t + d2*(np.sin((2*np.pi*t)/L)) + d3*(np.cos((2*np.pi*t)/L)) -y
# funktionen minus y därmed reservaren                                                    
def J(d0, d1, d2, d3, L):
    col0 = np.ones(t.shape)
    col1 = t
    col2 = np.sin(2 * np.pi * t / L)
    col3 = np.cos(2 * np.pi * t / L)
    col4 = -d2 * np.cos(2 * np.pi * t / L) * (2*np.pi*t / L**2) + d3 * np.sin(2 * np.pi * t / L) * (2*np.pi*t / L**2)
    return np.column_stack((col0, col1, col2, col3, col4))
#jakobianen av funktionen

cGN = np.array([d[0], d[1], d[2], d[3], 8]) # gissning från tidigare modell
tol = 1e-12
diff = np.ones(cGN.shape)
it = 0
maxiter = 100
while np.linalg.norm(diff) > tol and it < maxiter:
    diff = -np.linalg.lstsq(J(*cGN), F(*cGN))[0]
    cGN += diff
    it += 1
    print(it, cGN, np.linalg.norm(diff))
print("\nFärdiga resultat:")
print("d0 =", cGN[0])
print("d1 =", cGN[1])
print("d2 =", cGN[2])
print("d3 =", cGN[3])
print("L  =", cGN[4])

y1 = (cGN[0] + cGN[1]*t + cGN[2]*(np.sin((2*np.pi*t)/cGN[4])) + cGN[3]*(np.cos((2*np.pi*t)/cGN[4]))) 
#skapa funktion med de besämda parametrarna och plotta denna
plt.plot(t+1980, y)
plt.plot(t+1980, y1, label= "gausnewton")
plt.ylabel("KPI")
plt.xlabel("År")
plt.legend()
plt.grid()
plt.show()

M_fel(y1, y, "gausnewtons fel")
#plotta felet
E_rms(y1, y, "gaus metoden") 

#uppgift d
E_rms(p, y, "Modell a (Linjär)")
E_rms(ny_funktion, y, "Modell b (Sin/Cos, L=8)")
E_rms(y1, y, "Modell c (Gauss-Newton, optimerat L)")


def okning(y, t, etikett):
    tid = t[-1] - t[0]
    ökning = y[-1] - y[0]
    lutning = ökning / tid
    print(f"{etikett} {lutning} enheter/år")
    return lutning

# Anrop för respektive modell
print("\nGenomsnittlig ökning av KPI per år")
okning(p, t, "Modell a (Linjär)")
okning(ny_funktion, t, "Modell b (Sin/Cos)")
okning(y1, t, "Modell c (Gauss-Newton)") 


