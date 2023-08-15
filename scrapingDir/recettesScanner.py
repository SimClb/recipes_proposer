import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import time
#import some files; 
import colors #our file colors ;)
import listOfRecettes



url = 'https://www.amourdecuisine.fr/article-idee-de-repas-femme-debordee-recettes-facile-rapides.html'
recettesTotal = []

# here we effectue a request to get the website by his url
r = requests.get(url) 
# if 200 status is returned than the website is already


if r.ok:
    print(colors.bcolors.OKGREEN, "Statuss ok:", r, colors.bcolors.ENDC)
    soup = BeautifulSoup(r.text, 'html.parser')
    #links = soup.select('tbody > tr > td > p > a', href=True)
    
    project_href = [i['href'] for i in soup.find_all('a', href=True)]
    project_href = list(project_href)

    #fouding of start and end index 
    number1 = project_href.index('https://www.amourdecuisine.fr/article-gratin-de-pommes-de-terre-fromage.html')
    number2 = project_href.index('https://www.amourdecuisine.fr/article-pates-a-la-creme-poulet-champignons.html')

    #creation of a new list without undesirable links
    mainList = project_href[number1:(number2 + 1)]
    txtInPY = "recettes ="
    #let's write the new list into the file 

    #try: 
    #    file = open('listOfRecettes.py', 'w')
    #    file.write(txtInPY + str(mainList))
    #    file.close()
    #    print(colors.bcolors.OKGREEN, 'Writing file succeeded', colors.bcolors.ENDC)
    #except: 
    #    print(colors.bcolors.WARNING, "Writing file failed...", colors.bcolors.ENDC)

    
    #time.sleep(2) # the script will sleep for 5 seconds to be sure that the script is running correctly

    # go scan every links one by one to keep the title, the links and the ingredients

    ingredients = []


    for link in listOfRecettes.recettes:
        
        try:
            requestAccess = requests.get(link).text
            print(colors.bcolors.OKGREEN, "Access to the website was autorized", colors.bcolors.ENDC)

        except:
            print(colors.bcolors.WARNING, "Access to the website was denied", colors.bcolors.ENDC)
            break

        if requestAccess:
            print(colors.bcolors.OKGREEN, "Connect Statuss ok !", colors.bcolors.ENDC)

            soup2 = BeautifulSoup(requestAccess, 'html.parser')
            names = soup2.h1.text

            #initialize the list of ingredients
            ingredients = []

            print(colors.bcolors.UNDERLINE, names, colors.bcolors.ENDC)
            print(colors.bcolors.OKBLUE, link, colors.bcolors.ENDC)
            for li in soup2.find_all("li", {"wprm-recipe-ingredient"}):
                ingredient = li.text
                ingredients.append(ingredient)

            
            #hash table 
                
            hashTable ={
                        'name': f"{names}",
                        'ingrédients': ingredients,
                        'link': f"{link}",
                    }


            #send the hash table to the list of recettes
            
            recettesTotal.append(hashTable)

        else:
            print(colors.bcolors.WARNING, "Echec connection failed...", colors.bcolors.ENDC)



    print(colors.bcolors.OKGREEN, "Extraction succeeded !")

    


else:
    print(colors.bcolors.WARNING + 'Error status: ' + r)



print(colors.bcolors.BOLD,colors.bcolors.OKGREEN, recettesTotal, colors.bcolors.ENDC)
prefix = "container ="
try: 
    file = open('recettes.py', 'w')
    file.write(prefix + str(recettesTotal))
    file.close()
    print(colors.bcolors.OKGREEN, 'Writing file succeeded', colors.bcolors.ENDC)
except: 
    print(colors.bcolors.WARNING, "Writing file failed...", colors.bcolors.ENDC)