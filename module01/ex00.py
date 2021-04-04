class Recipe:
    a=' '
    b=0
    c=0
    d=[]
    e=' '
    f=' '
    def __init__(self, recipe_name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.a=recipe_name
        self.b=cooking_lvl 
        self.c=cooking_time
        self.d=ingredients 
        self.e=description 
        self.f=recipe_type
        def __str__ (self):
           return 'Recipe=(' + str(self.a) + ',' + self.b + ',' + self.c +',' + str(self.d) +',' + str(self.e)+',' + str(self.f)+')'
           
        
                
class Book:
        x=' '
        y=0
        z=0
        t={'starter':[],'lunch':[],'dessert':[]}
        def __init__(self,book_name, last_update, creation_time, recipes_list):
            
            self.x=book_name
            self.y=last_update
            self.z=creation_time
            self.t=recipes_list
        def __str__ (self):
           return 'Book=(' + self.x + ',' + str(self.y) + ',' + str(self.z) +',' + str(self.t) +')'
        def get_recipe_by_name(self,recipe_name):
            return("the recipe's name is " + str(self.a))
            pass
        def get_recipes_by_type(self,recipe_type):
            return self.t[self.f]
            pass
        def add_recipe(self, recipe):
            
            for key in self.t:
                 if self.t[key]==recipe.recipe_type:
                     self.t[key].append(recipe.recipe_name)
            pass
                     
                     
#test  
book1 = Book("pastery", 2020, 2002,["cake","cupcakes","popcakes"])
print(book1)
    
        
