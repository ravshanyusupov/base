from django.shortcuts import render
from myapp.models import Independent
# Create your views here.
import random
from datetime import date

vaqt = date.today()


def home(request):
    a = Independent.objects.filter(age__range=(18,  30))
    b = Independent.objects.all().count()
    context = {
        'a': a,
        'b': b
    }
    return render(request, 'base.html', context)

def delete(request):
    a = Independent.objects.all().delete()
    context = {
        'a': a
    }
    return render(request, 'base.html', context)




def Data(request):
    ism = ['Ravshan', 'Suleyman', 'Roma', 'Odil', 'Obid', 'Abdullo', 'Obid', 'Olim', 'Otabek']
    familiya = ['Yusupov', 'Nazarov', 'Abdulayev', 'Odilov', 'Atoyev', 'Odilov', 'Qosimov', 'Avazov']
    for i in range(1, 100):
        ism_1 = random.choice(ism)
        familiya_1 = random.choice(familiya)
        yil = random.randint(1929, 2021)
        yosh = vaqt.year - yil
        oy = random.randint(1, 12)
        kun = random.randint(1, 31)
        if (oy == '2' or kun <= 28) or (oy == '4' or oy == '6' or oy == '9' or oy == '11' or kun <= 30):
             date = f"{yil}-{oy:02d}-{kun:02d}"
             a = Independent.objects.create(name=ism_1, last=familiya_1, birth=date, age=yosh)
        else:
            print('wrong')
    return render(request, 'data.html')
