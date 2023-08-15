import random
import recettes
import colors 


print(colors.bcolors.OKGREEN,'''

#############################################################
################### RECIPE PROPOSER V2 ######################
#############################################################

''', colors.bcolors.ENDC)

# functions 

def recipeChoicer(list):

    oneRecipe = random.choice(list)
    return oneRecipe

# choice random our recipes 

ourRecipes = []

for i in range(7):

    recipe = random.choice(recettes.container)
    ourRecipes.append(recipe)

# propose to user

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
n = 0

for d in days:
    print(f" - {d} : {ourRecipes[n]['name']}")
    n += 1


for i in ourRecipes:
    print(colors.bcolors.OKBLUE, i, colors.bcolors.ENDC)

# ask if everything is good for the user

confirmation = False
counter = 0

while not confirmation or counter != 7:

    asking = input("\nDo you agreed those recipes ? (Y/N):")

    if asking.upper() == 'Y':
        confirmation = True
        counter = 7

    elif asking.upper() == 'N': 

        for (i, j) in zip(days, ourRecipes):
            print(f"Do you agreed '{j['name']}' for {i} ? (Y/N):")
            askingQ = input()
            
            if askingQ.upper() == 'Y':
                counter += 1
            
            elif askingQ.upper() == 'N':
                confirmUnit = False

                while not confirmUnit:
                
                    #print(j)
                    index = ourRecipes.index(j)
                    ourRecipes[index] = recipeChoicer(recettes.container)
                    print(f"Do you agreed {ourRecipes[index]['name']} for {i} ? (Y/N):")
                    askingLast = input()

                    if askingLast.upper() == 'Y':
                        counter += 1
                        confirmUnit = True


                
                
