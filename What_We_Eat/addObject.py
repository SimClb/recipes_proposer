import os
import django
import colors

# Définir la variable d'environnement DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'What_We_Eat.settings')

# Configurer l'environnement Django
django.setup()

# Importer votre modèle
from proposer.models import Recipes
# import our recipes 
import recettes


for recipe in recettes.container[1:]:
    list_ingredients = ""

    for i in recipe['ingrédients']:
        list_ingredients += f"{i}, "

    try: 
        object = Recipes(name=f"{recipe['name']}", ingredients=f"{list_ingredients}", link=f"{recipe['link']}")
        object.save()
        print(colors.bcolors.OKGREEN, f"{recipe['name']} was successfully saved in the db !", colors.bcolors.ENDC)
    except: 
        print(colors.bcolors.FAIL,'error', colors.bcolors.ENDC)
