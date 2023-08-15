import random
#put some colors in our life ;)
import colors

#our data source
import recettes

n=0

name = recettes.container[n]['name']
ingredients = recettes.container[n]['ingrédients']
link = recettes.container[n]['link']

recettesOfTheWeek = []


#there are seven days in a week ;)
for i in range(7):

    #we import a random recette 
    recetteNow = random.choice(recettes.container)
    #we put this recette into a list 
    recettesOfTheWeek.append(recetteNow)

    #print(colors.bcolors.UNDERLINE, colors.bcolors.OKGREEN ,recetteNow["name"], colors.bcolors.ENDC)
    #for i in recetteNow['ingrédients']:
    #    print(colors. bcolors.OKBLUE, "-", i, colors.bcolors.ENDC)
    #print(recetteNow['link'])


#our week meal 
Monday = recettesOfTheWeek[0]
Tuesday = recettesOfTheWeek[1]
Wednesday = recettesOfTheWeek[2]
Thursday = recettesOfTheWeek[3]
Friday = recettesOfTheWeek[4]
Saturday = recettesOfTheWeek[5]
Sunday = recettesOfTheWeek[6]

##### let's proposate the recettes of the week ######

MondayName = recettesOfTheWeek[0]['name']
TuesdayName = recettesOfTheWeek[1]['name']
WednesdayName = recettesOfTheWeek[2]['name']
ThursdayName = recettesOfTheWeek[3]['name']
FridayName = recettesOfTheWeek[4]['name']
SaturdayName = recettesOfTheWeek[5]['name']
SundayName = recettesOfTheWeek[6]['name']

print("Vos recettes de la semaine sont; \n"
    "-Monday: ", MondayName, 
    "\n-Tuesday: ", TuesdayName, 
    "\n-Wednesday: ", WednesdayName,
    "\n-Thursday", ThursdayName,
    "\n-Friday: ", FridayName,
    "\n-Saturday: ", SaturdayName,
    "\n-Sunday: ", SundayName)

recipeTable = {

    Monday : [

    ]

}


ChoiceConfirmation = str(input("Validez-vous ces recettes ? Y/N:  "))

confirmation = False

while not confirmation: 

    asking = input("Do you agreed those recipe ?")

    if asking.upper() == "Y":
        confirmation = True

    elif asking.upper() == "N":

        print("waiting")
 



        
        
        








