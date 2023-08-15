from django.shortcuts import render
from proposer.models import Recipes
import random

def home(request):

    x = 6
    count = Recipes.objects.count()
    random_index = random.randint(0, count - x)
    elements = [i for i in Recipes.objects.all().order_by('?')[random_index:random_index + x]]
    listIngre = []

    for i in Recipes.objects.all().values('ingredients').order_by('?')[random_index:random_index + x]:
        listIngre.append(i)



    recipe = Recipes.objects.get(id=65)

    hashTable = [
        {'test', 'pff', 'ddd'},
        {'fefe', 'mlk', 'ddd'},
        {'dss', 'slss', 'slks'},
    ]

    return render(
        request,
        'proposer/proposer.html',
        {'ele': elements, 'test':listIngre, 'hash':hashTable, 'recipe':recipe, 'type':type}
    )
