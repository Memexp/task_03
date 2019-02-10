from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	'my_list' : [
    		{
    		"restaurant_name" : "Nino",
    		"food_type" : "Italian",
    		},
    		{
    		"restaurant_name" : "Shrimp Anatomy",
    		"food_type" : "Sea Food",
    		},
    		{
    		"restaurant_name" : "Pizzahut",
    		"food_type" : "Pizza!",
    		},
    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	'my_object' : {
    		"restaurant_name" : "Sports Cafe",
    		"food_type" : "Deserts, All Kind of Food",
    	},
    	'my_object2' : {
    		"restaurant_name" : "Juice Time",
    		"food_type" : "Juices",
    	},
    	'my_object3' : {
    		"restaurant_name" : "Anoosh",
    		"food_type" : "Cookies",
    	},
    }
    return render(request, 'detail.html', context)
