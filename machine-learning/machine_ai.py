import json
import os

def add_phone_info(datas : list):
    data = {}
    while True:
        try:
            data['nom'] = input("Nom du contact : ")
            data["Numero"] = input("Numero du contact : ")
            datas.append(data)
            datas.sort(key=lambda dicts : dicts['nom'].lower())
            save_phone(datas)
            continues = input("Yes/no : ")
            if continues == "no":
                return
        except ValueError:
            print("Numero invalide !")
            
def save_phone(data):
    with open("phone.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)
        print("Information sauvegarder !")
        
def binary_search(data,items):
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high) // 2
        value_middle = data[middle]
        if value_middle['nom'] == items:
            return middle
        if items < value_middle['nom']:
            high = middle - 1
        else:
            low = middle + 1
    return None
                
        
def find_phone(data):
    names = input("Entrer le nom a rechercher : ")
    binary_result = binary_search(data,names)
    if binary_result is not None:
        resultat = data[binary_result]
        print("-----Contact trouvé-----")
        print(f"Nom : {resultat['nom']}")
        print(f"Numero : {resultat['Numero']}")
    else:
        print("Contact introuvable")
def delete_contact(data):
    names = input("Entrer le nom a  supprimer : ")
    binary_searchs = binary_search(data,names)
    if binary_searchs is not None:
        resultat = data[binary_searchs]
        del data[binary_searchs]
        print(f"Le contact {resultat['nom']} est supprimé !")
        save_phone(data)

def load_phone_data():
    if os.path.exists("phone.json"):
        with open("phone.json","r",encoding="utf-8") as file:
            data = json.load(file)
            return data
    return []
    
def menu(datas):
    while True:
        print("CONTACT".center(20,"="))
        print("1.Enregister un contact !")
        print("2.Chercher un contact")
        print("3.Supprimer un contact")
        print("4.Quitter")
        
        choix = input("Entrer votre choix : ")
        
        if choix == "1":
            add_phone_info(datas)
        elif choix == "2":
            find_phone(datas)
        elif choix == "3":
            delete_contact(datas)
        elif choix == "4":
            break
        else:
            print("Choix invalide !")