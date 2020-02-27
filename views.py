from django.shortcuts import render
from .models import HouseDetails


def home(request):
    return render(request, 'main/home.html')


def predict(request):

    if request.method == "POST":
        bedroom = request.POST.get('number1')
        bathroom = request.POST.get('number2')
        sqft_living = request.POST.get('number3')
        sqft_lot = request.POST.get('number4')
        floors = request.POST.get('number5')
        sqft_above = request.POST.get('number6')
        sqft_basement = request.POST.get('number8')
        zipcode = request.POST.get('number9')
        sqft_living15 = request.POST.get('number10')
        sqft_lot15 = request.POST.get('number11')
        year_renovated = request.POST.get('yesno')
        year_built = request.POST.get('date')
        viewss = request.POST.get('viewss')
        waterfront = request.POST.get('waterfront')
        condition = request.POST.get('condition')
        grade = request.POST.get('grade')

        val = HouseDetails(bedroom=bedroom, bathroom=bathroom, sqft_living=sqft_living, sqft_lot=sqft_lot, floors=floors, sqft_above=sqft_above, sqft_basement=sqft_basement,
                           zipcode=zipcode, sqft_living15=sqft_living15, year_renovated=year_renovated,
                           sqft_lot15=sqft_lot15, year_built=year_built, viewss=viewss, waterfront=waterfront,
                           condition=condition, grade=grade)

        val.save()


    return render(request, 'main/predict.html')

def about(request):
    return render(request, 'main/about.html')