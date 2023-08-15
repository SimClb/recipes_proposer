import os
import django
import colors

# Définir la variable d'environnement DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'What_We_Eat.settings')

# Configurer l'environnement Django
django.setup()

# Importer votre modèle
from proposer.models import Recipes

for ite in range(39):
    try:

        my_object = Recipes.objects.get(id=ite)
        print(colors.bcolors.OKGREEN, f"object '{my_object.name}' has been deleted ", colors.bcolors.ENDC)
        my_object.delete()
    except:
        print(colors.bcolors.FAIL, 'error', colors.bcolors.ENDC)