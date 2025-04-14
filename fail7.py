
def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()
list_=Loe_failist('tund7.txt')
for x in list_:
    print(x)
list_ = ['Ann','Kati','mari']
Kirjuta_failisse('tund7.txt', list_)
list_2=Loe_failist('tund7.txt')
print(list_2)
with open('tund7.txt', 'r', encoding='utf-8-sig') as f:
    print(f.read())


from random import * 
def failist_to_dict(f:str):
    riik_pealinn={}
    pealinn_riik={}
    riigid=[]
    file=open(f, 'r', encoding="utf-8-sig")
    for line in file:
        k, v = line.strip().split('-')
        riik_pealinn[k]=v
        pealinn_riik[v]=k
        riigid.append(k)
    file.close()
    return riik_pealinn, pealinn_riik, riigid
riigidriik_pealinn, pealinn_rikk, riigid=failist_to_dict('riigid_pealinnad.txt')
print(riigidriik_pealinn)

def failist_to_dict(f:str):
    riik_pealinn = {}
    pealinn_riik = {}
    riigid = []
   
    with open(f, 'r', encoding="utf-8-sig") as file:
        for line in file:
            k, v = line.strip().split('-')
            riik_pealinn[k] = v
            pealinn_riik[v] = k
            riigid.append(k)
    
    return riik_pealinn, pealinn_riik, riigid



def getcapital(country, riik_pealinn):
    return riik_pealinn.get(country, "Ei ole pealinn")


def getcountry(capital, pealinn_riik):
    return pealinn_riik.get(capital, "Ei ole pealinn")

def add_country_capital(country, capital, riik_pealinn, pealinn_riik):
    riik_pealinn[country] = capital
    pealinn_riik[capital] = country
    print(f" {country} ja pealinn {capital} new!")

def main_menu(riik_pealinn, pealinn_riik):
    while True:
        print("\nValige tegevus:")
        print("1. Kuvada pealinn riigi järgi")
        print("2. Kuvada riik pealinna järgi")
        print("3. Lisada riik ja pealinn")
        print("4. Uuendada riigi pealinna")
        print("5. Teadlikkuse kontroll")
        print("6. Välju")
        
        choice = input("Sisesta tegevuse number: ")
        
        if choice == "1":
            country = input("Sisesta riigi nimi: ")
            print(f"Riigi {country} pealinn on: {getcapita(country, riik_pealinn)}")
        
        elif choice == "2":
            capital = input("Sisesta pealinna nimi: ")
            print(f"Riik, mille pealinn on {capital}: {getcountry(capital, pealinn_riik)}")
        
        elif choice == "3":
            country = input("Sisesta riigi nimi: ")
            capital = input("Sisesta pealinna nimi: ")
            add_country_capital(country, capital, riik_pealinn, pealinn_riik)
        
        elif choice == "4":
            country = input("Sisesta riigi nimi: ")
            new_capital = input("Sisesta uus pealinn: ")
            update_country_capital(country, new_capital, riik_pealinn, pealinn_riik)
        
        elif choice == "5":
            quiz(riik_pealinn, pealinn_riik)
        
        elif choice == "6":
            print("Väljumine programmist.")
            break
        
        else:
            print("Vale valik. Palun vali uuesti.")

# Andmete laadimine failist
riik_pealinn, pealinn_riik, riigid = failist_to_dict('riigid_pealinnad.txt')

# Käivitame peamenüü
main_menu(riik_pealinn, pealinn_riik)