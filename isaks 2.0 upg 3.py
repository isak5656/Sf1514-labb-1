#Labb uppgift 3 A
#definerar funktionen
import numpy as np

"uppgift A"
#funktionen f
def intergral (x):
    f = x**3 * np.exp(x)
    return f


def trapets(gränser, N, f):
    #skapa lista för förvaring av värden
    #intergral gränser
    a, b = gränser
    #steglängden
    h = (b - a) / N
    #N+ 1 för att kompensera för 0an?
    x_värden = np.linspace(a, b, N+1) 
    #skickar in vektorn i funktionen och få f(x) värden
    funktions_värden = f(x_värden)
    #trapetsreglen h gånger höjden plus en halv första och sista punkt för att få hela arena
    Th = h* (np.sum(funktions_värden) - 0.5*(funktions_värden[0] + funktions_värden[-1]))
    return Th
    
def uppgift_A():
    print("\n uppgift A")
    gränser = [0, 2]
    N = 100
    Th = trapets(gränser, N, intergral)
    dTh = (Th - 20.7781)
    print(f"intergralens värde är {Th:.4f} och skillnaden är {dTh:.4f}") #:.4f avrunda 4 decimaler
    



"uppgift B"

def uppgift_B():
    print("\n uppgigft B")
    #olika intervall för gränser
    intervall = [10, 20, 30, 40, 100, 1000]
    for i in range(len(intervall)):
        gränser = [0, 2]
        N = intervall[i]
        Th = trapets(gränser, N, intergral)
        print(f"integralens värde är{Th} med intervall: {intervall[i]}")

"uppgift C"
def uppgift_C ():
    print("\nuppgift C")
    t_data = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
    f_data =[12.00, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56]

    #interpolera för att skapa en graf med en input x
    N = 8 #antal år
    a, b = [t_data[0], (t_data[-1])] #intervall
    #steglängden
    h = (b - a) / N # alltså 1 
    #trapetsreglen h gånger höjden plus en halv första och sista punkt för att få hela arena
    Th = h* (np.sum(f_data) - 0.5*(f_data[0] + f_data[-1])) 
    print("värdet från uppgift c integral är", Th)





"uppgift D"
def uppgift_D ():
    print("\ndet här är uppgift D")
    t_data = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
    f_data =[12.00, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56]

    #interpolera för att skapa en graf med en input x
    N = [1, 2, 4, 8] #steglängd 1, 0.5, 0.25 osv
    lagring = np.ones(len(N))
    for i in range(len(N)):
        a, b = [t_data[0], (t_data[-1])] #intervall
        #steglängden
        h = (b - a) / (8*N[i]) # alltså 1 
        #trapetsreglen h gånger höjden plus en halv första och sista punkt för att få hela arena
        Th = h* (np.sum(f_data) - 0.5*(f_data[0] + f_data[-1])) 
        lagring[i] = Th
        print(f"värdet från uppgift D integral är,{Th}, då steglängden är {N[i]}")
        

    
    "räkna u t flet e"
    eh1 = lagring[0] - lagring[2]
    eh2 = lagring[2] - lagring[3]
    print(f" felen i D\n här är felet för h = 5, 10 {eh1} \n här är felet för h = 10, 20 {eh2}\n")
    return lagring, N

"uppgift E"
def uppgift_E():
    Thvec, intervall = uppgift_D()
    Rhvec = []
    for i in range(1, np.size(intervall)): # i startar p˚a 1
        # Anv¨and i-1 och i f¨or att ber¨akna Richardson
        Th = Thvec[i-1]
        Th_half = Thvec[i]
        Rh_half = (4*Th_half - Th) / 3
        Rhvec.append(Rh_half)
    Rhvec = np.array(Rhvec)
    print("rvec är", Rhvec)


"uppgift F"

#funktion som beräknar simpons
def simpsons(gränser, N, f):
    #skapa lista för förvaring av värden
    #intergral gränser
    a, b = gränser
    #steglängden
    h = (b - a) / N
    #N+ 1 för att kompensera för 0an?
    x_värden = np.linspace(a, b, N+1) 
    #skickar in vektorn i funktionen och få f(x) värden
    funktions_värden = f(x_värden)
    #Simpsons formel: h/3 * (ändpunkter + 4*udda punkter + 2*jämna punkter)
    udda_summa = np.sum(funktions_värden[1:-1:2])   #index 1,3,5,... (udda index) [start:stop:steg]
    jämn_summa = np.sum(funktions_värden[2:-1:2])   #index 2,4,6,... (jämna index, ej ändpunkter)

    simpsons_metod = (h/3) * (funktions_värden[0] + funktions_värden[-1] + 4*udda_summa + 2*jämn_summa)
    return simpsons_metod


def uppgift_F(): # simpsons metod
    t_data = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
    f_data =[12.00, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56]
    def f(x):
            funktion = np.interp(x, t_data, f_data)
            return funktion
    print("\nuppgift F - Simpsons metod")
    gränser = [t_data[0], (t_data[-1])]
    N = (len(t_data)) -1
    Simopsons_värde = simpsons(gränser, N, f)
    print("integralens värde med Simpsons metod är", Simopsons_värde)
"uppgift F - exponentiell modell (linjär ersättningsmodell)"

def uppgift_F_exp(): # linjärisering av exponential funktion
    print("\nuppgift f - exponentiell modell")
    t_data = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
    f_data = np.array([12.00, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56])

    #linjärisering: ln(f) = ln(a) + b*(t-2014)
    x = t_data - 2014
    y = np.log(f_data)

    #ställ upp normalekvationerna för y = c0 + c1*x ettor för c0 
    A = np.vstack([np.ones(len(x)), x]).T
    c = np.linalg.lstsq(A, y)[0]
    c0 = c[0]
    c1 = c[1]

    #räkna tillbaka till ursprungliga koefficienter
    a = np.exp(c0)
    b = c1
    print(f"a = {a}, b = {b}")
    return a, b

"uppgift E" #nya integralvärden
def uppgift_E():
    a, b = uppgift_F_exp()
    f_2023 = a * np.exp(b * (2023 - 2014)) # funktionsvärde 2023
    print(f"effekten är ungefär,{f_2023} kW")
    t_data = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
    f_data = np.array([12.00, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56, f_2023])
    #interpolera för att skapa en graf med en input x
    def f(x):
        funktion = np.interp(x, t_data, f_data)
        return funktion
    # antalet datapunkter -1 
    N = (len(t_data)) -1
    #gränsen första sita t
    gränser = [t_data[0], (t_data[-1])]
    #skicka in i funktionen
    Th = trapets(gränser, N, f)
    print(f"värdet från uppgift c integral är {Th}kW")

    if f_2023 > 100:
        print("2023 var det över 100 kW")
    if Th > 350:
        print("totala integralen är större än 350 Kw")
    else:
        print("inget av vilkoren uppfylls")



uppgift_A()
uppgift_B()
uppgift_C()
uppgift_D()
uppgift_E()
uppgift_F()
uppgift_F_exp()
uppgift_E()

