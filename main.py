import hashlib
import json
# je load le contenu du json
with open('password.json', 'r') as f:
    password_list = json.load(f)


def check(mdp):  # la fonction qui check la conformité du mdp
    special_char = ["!", "@", "#", "$", "%", "^", "&", "*"]
    lower = 0
    alpha = 0
    chiffre = 0
    special = 0
    len_mdp = len(mdp)

    for letter in mdp:
        if letter.isalpha():
            alpha += 1
        if letter.islower():
            lower += 1
        if letter in special_char:
            special += 1
        if letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            chiffre += 1
    if lower != 0 and alpha != 0 and chiffre != 0 and special != 0 and len_mdp > 7:
        correct = 1
        return correct
    else:
        correct = 0
        return correct


def main():  # architecture globale
    user_name = input("Entrez votre nom d'utilisateur: ")
    if user_name in password_list:
        print("Nom d'utilisateur existant")
        main()
    print('Votre mot de passe doit contenir:\n8 caractères \nAu moins une lettre majuscule et une minuscule'
          '\nun chiffre\nun caratère spécial parmis: (!, @, #, $, %, ^, &, *)')
    mdp = input('Entrez votre mot de passe: ')

    correct = check(mdp)
    if correct == 1:
        hash_mdp = hashlib.sha256()
        hash_mdp.update(mdp.encode())
        hash_mdp_final = hash_mdp.hexdigest()
        if hash_mdp_final in password_list:
            print('Mot de passe existant')
            main()
        password_list[user_name] = str(hash_mdp_final)
        with open('password.json', 'w') as f:  # je sauvegarde le dictionnaire dans le json
            json.dump(password_list, f)
        show_password = input('Voulez vous voir la liste de mot de passe? Y/N: ')

        if show_password.lower() == "y":
            for i in password_list:
                print(i, ':', password_list[i])
        else:
            pass
    else:
        main()


main()
