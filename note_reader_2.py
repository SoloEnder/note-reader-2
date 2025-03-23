import os, json
from colorama import Style

print('#'*20, 'Note Reader 2', '#'*20)
with open('data/data.json', 'r') as f:
    data = json.load(f)
    
gras = Style.BRIGHT 
nos = Style.RESET_ALL
ext = data['file_format'] 
save_folder = data['save_folder']
running = True

while running == True:
    command = input(f"{gras}Que voulez vous faire ? Tapez 'cl' pour accédez à la liste des commandes\nUser: {nos}")
    
    if command == 'w':
        name = input(f'{gras}Quel est le nom du fichier ?\nUser: {nos}')
        print('='*20, name, '='*20)
        content = input('')
        print('='*40)
        save_loop = True
        
        while save_loop == True:
            save = input(f'{gras}Voulez vous sauvegarder le fichier {name} ? (Y/n)\nUser: {nos}')
            
            if save == 'Y':
                file = save_folder + name + ext
                
                if ext == '.txt':
                    
                    with open(file, 'w') as f:
                        f.write(content)
                        print(f'{gras}Sauvegardé')
                        
                if ext == '.json':
                    
                    with open(file, 'w') as f:
                        json.dump(content, f)
                        print(f'{gras}Sauvegardé')
                        
                save_loop = False
                    
            elif save == 'n':
                save_loop = False
                
            else:
                print('Réponse invalide')
                        
    elif command == 'r':
        name = input(f'{gras}Quel fichier voulez vous lire ?\nUser: {nos}')
        
        if '.txt' in name:
            
            with open(name, 'r') as f:
                content = f.read()
            print('='*20,name,'='*20)
            print(content)
            print('='*40)
            
        elif '.json' in name:
            
            with open(name, 'r') as f:
                content = json.load(f)
            print(content)
            
        else:
                print(f'{gras}Format non reconnu')
                
    elif command == 's':
        print(f'{gras}1) Dossier de sauvegarde          2) Format des fichiers')
        settings_modif = input(f'{gras}Que voulez vous modifier ?\nUser: {nos}')
                
        if settings_modif == '1':
                    
            if save_folder == 'saves':
                print(f"{gras}Le dossier de sauvegarde actuel est 'saves', situé dans le dossier du programme")
                
            else:
                print(f'{gras}Le dossier de sauvegarde actuel est {save_folder}')
                
            modif_save_folder_conf_loop = True
                
            while modif_save_folder_conf_loop == True:
                modif_save_folder_conf = input(f'{gras}Voulez vous le modifier ? (Y/n)\nUser: {nos}')
                    
                if modif_save_folder_conf == 'Y':
                    new_save_folder = input(f"{gras}Entrez le chemin du nouveau dossier de sauvegardé\nUser: {nos}")
                        
                    with open('data/data.json', 'w') as f:
                        data['save_folder'] = new_save_folder
                        json.dump(data, f)
                        
                elif modif_save_folder_conf == 'n':
                    modif_save_folder_conf_loop = False
                    
                else:
                    print(f'{gras}Réponse invalide')
                    
        elif settings_modif == '2':
            print(f'{gras}Format disponibles :         1) txt               2) json')
            modif_file_format = True
            while modif_file_format == True:
                
                file_format_select = input(f'{gras}Quel format préférez vous ?\nUser: {nos}')
                
                if file_format_select == '1':
                    data['file_format'] = '.txt'
                    
                    with open('data/data.json', 'w') as f:
                        json.dump(data, f)
                        print(f'{gras}format modifié')
                        modif_file_format = False
                        
                elif file_format_select == '2':
                    data['file_format'] = '.json'
                    
                    with open('data/data.json', 'w') as f:
                        json.dump(data,f)
                        print(f'{gras}format modifié')
                        modif_file_format = False
                        
                else:
                                 print(f'{gras}Réponse invalide')
                                 
                                 
    elif command == 'rn':
        print(f"{gras}Note Reader 2.0, finie le 23/03/2024                                       - prise en charge des formats 'json' et 'txt'")
        
    elif command == 'cl':
                    print(f'''{gras}
- 'w': créer un fichier
- 's': modifier les paramètres
- 'rn': afficher les notes de versions
- 'e': arrêter le programme''')

    elif command == 'e':
                    running = False
                    
    else:
        print(f"{gras}Commande non reconnue")                                                                                     