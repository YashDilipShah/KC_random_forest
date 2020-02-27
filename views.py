from django.shortcuts import render
from .models import HouseDetails

import pickle

regressor = pickle.load(open("C:/Users/RUSHABH/Desktop/SGH_files/KC_SAVED_RANDOM_FOREST_ORIGINAL.sav", "rb"))
print("This model is having accuracy of 88.313%")
import numpy as np


def waterfront_convert(bool_water):
    if bool_water == 'Yes':
        return 1
    else:
        return 0

def year_renovated_convert(year_built, year_reno):
    if year_reno < year_built:
        return 0
    else:
        return year_reno


def predict_user_values(inp):

    arr = np.array(inp)
    arr = np.reshape(arr, (1, len(inp)))
    pred = regressor.predict(arr)
    return (pred[0])




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
        year_built = request.POST.get('date')
        year_renovated = year_renovated_convert(year_built, request.POST.get('yesno'))
        viewss = request.POST.get('viewss')
        waterfront = waterfront_convert(request.POST.get('waterfront'))
        condition = request.POST.get('condition')
        grade = request.POST.get('grade')


        l = [bedroom, bathroom, sqft_living, sqft_lot, floors, waterfront,
             viewss, condition, grade, sqft_above, sqft_basement,
             year_built, year_renovated, zipcode, 47.560053, -122.213896,
             sqft_living15, sqft_lot15]

        final_price = str(predict_user_values(l))
        print(final_price)


        val = HouseDetails(bedroom=bedroom, bathroom=bathroom, sqft_living=sqft_living, sqft_lot=sqft_lot, floors=floors, sqft_above=sqft_above, sqft_basement=sqft_basement,
                           zipcode=zipcode, sqft_living15=sqft_living15, year_renovated=year_renovated,
                           sqft_lot15=sqft_lot15, year_built=year_built, viewss=viewss, waterfront=waterfront,
                           condition=condition, grade=grade)

        val.save()


    return render(request, 'main/predict.html')

def about(request):
    return render(request, 'main/about.html')