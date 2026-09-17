import numpy as np
import matplotlib.pyplot as plt

"""Ritar en graf av funktionen och dess derivata uppgift A"""
L = 1

f = lambda x: (8*x)/(3*L) - 3*(x/L)**2 + (1/3)*(x/L)**3 - (2/3)*np.sin(np.pi*x/L)
#funktion f
def df(x, L):
    return 8/(3*L) - (6*x)/(L**2) + (x**2)/(L**3) - (2*np.pi)/(3*L)*np.cos(np.pi*x/L)
#funktion för derivatan av f

x = np.linspace(0, L, 100) #skapar en vektor 0->L med 100siffror
"plottar funktioonerna med x och y axel"
plt.plot(x, f(x), label="f(x)") #funktionen
plt.plot(x, df(x, L), label="f'(x)") #derivatan
plt.xlim(0, 1) # x axeln
plt.ylim(-0.4, 0.25) #y axeln
plt.grid(True) # skapa rutnät
plt.legend() # öppna rutan
plt.show() # visa grafen

"B beloppet av g derivatan måste vara mindre än 1 för att det ska gå att använda fixpunktsmetoden lokalt"
"""Uppgift C python program för Fixpunktsmetoden"""
#fixmetoden lista för differanser
print("det här är uppgift C för fixpunktsmetoden\n")
diff_fixpunkt = [] 
L = 1
g = lambda x: (3 * L / 8) * (
    3 * (x / L) ** 2
    - (1 / 3) * (x / L) ** 3
    + (2 / 3) * np.sin(np.pi * x / L) 
) #här löser vi ut x ur ekvationen f(x) flytta allt till ena sidan läman en term och lös ut x
tol = 1e-10 # toleransen max 1e-16
i, max_iter = 0, 500 #itterationer
x = 0.8  # 1. Definiera ett startvärde x0
diff = 1.0  # Sätt ett startvärde för diff så loopen startar

while diff > tol and i < max_iter:
  xn = g(x)  # Beräkna nästa värde
  diff = np.abs(xn - x)  # Beräkna skillnaden mellan nya x 
  diff_fixpunkt.append(diff) #lägger till felet i listan
  x = xn  # Uppdatera x till det nya värdet
  i += 1  # Öka rätt räknare
  print(f"försök nummer {i}: x = {x:.10f}, diff  = {diff:.2e}") 
  #skriver ut på snyggt sätt med antal decimaler


"""uppgift D Newton metoden"""
#newtons metod lista för differanser
print("uppgift D med hjälp av newtons metod\n")
diff_newton = [] 
L = 1
g = lambda x: (
    (8 * x) / (3 * L)
    - 3 * (x / L) ** 2
    + (1 / 3) * (x / L) ** 3
    - (2 / 3) * np.sin(np.pi * x / L))

gd = lambda x: (
    8 / (3 * L)
    - (6 * x) / (L**2)
    + (x**2) / (L**3)
    - (2 * np.pi) / (3 * L) * np.cos(np.pi * x / L)
) #derivata av g

tol = 1e-10
i, max_iter = 0, 500
x = 0.8  # 1. Definiera ett startvärde x0
diff = 1.0  # Sätt ett startvärde för diff så loopen startar

while diff > tol and i < max_iter:
  xn = x - g(x) / gd(x)  # Beräkna nästa värde med punkt och derivata
  diff = np.abs(xn - x)  # skillnaden mellan nya och gamla värdet
  diff_newton.append(diff) #lägger till felet i lista
  x = xn  # Uppdatera x till det nya värdet
  i += 1  # Öka räknare
  print(f"försök {i}: x = {x:.10f}, diff = {diff:.2e}")



"""Uppgift e jämför hur de olika metoderna konvergerar"""
plt.semilogy(diff_fixpunkt, label="Fixpunktsmetoden") #plottar fixpmetod och döper den
plt.semilogy(diff_newton, label="Newton-Raphson")# plottar newton och namn
plt.grid(True, which="both") #skapar ett rutnät
plt.legend() #skapar en lilten ruta i hörnet med namn
plt.show() #visar plottarna
