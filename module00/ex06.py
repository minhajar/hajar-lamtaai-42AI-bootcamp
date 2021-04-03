cookbook={
    "cake":{"Ingredients":["flour","eggs","sugar"],
            "mealType":"dessert",
            "cookingTime":60},
    "sandwich":{"Ingredients":["bread","greens","chicken"],
                "mealType":"lunch",
                "cookingTime":10},
    "salad":{"Ingredients":["greens","veggies","sauce"],
             "mealType":"appetizer",
             "cookingTime":20},
}   

def print_recipe(recipeName):
    print("Recipe for a",recipeName)
    print("Ingredients are",cookbook[recipeName]["Ingredients"])
    print("To have it as",cookbook[recipeName]["mealType"])
    print("Takes",cookbook[recipeName]["cookingTime"],"for prep")

def delete_recipe(recipeName):
    if recipeName in cookbook:
        del cookbook[recipeName]
    
def add_new_recipe(recipeName,Ing,meal,Time):
    recipe={"Ingredients":[],
                "mealType":[],
                "cookingTime":[]}
    recipe["Ingredients"].append(Ing)
    recipe["mealType"].append(meal)
    recipe["cookingTime"].append(Time)
    cookbook[recipeName]=recipe
   
def display():
    print(cookbook.items())
    

while option!=5:
print("Please select an option by typing the corresponding number:")
print("1: Add a recipe ")
print("2: Delete a recipe")
print("3: Print a recipe")
print("4: Print the cookbook")
print("5: Quit")
option=int(input())

    if option==1:
      recipeName=input("print ur recipe name")
      Ing=input("print the list of ingredients")
      meal=input("print the meal type")
      time=input("print the prep time")
      add_new_recipe(recipeName,Ing,meal,Time)
    elif option==2:
      recipeName=input("print the recipe name")
      delete_recipe(recipeName)
    elif option==3:
      recipeName=input("print the recipe name")
      print_recipe(recipeName)
    elif option==4:
      display()
if option==5:
   print("you quit the cookbook")
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
