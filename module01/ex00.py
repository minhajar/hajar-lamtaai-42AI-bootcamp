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
        t=[]
        def __init__(self,book_name, last_update, creation_time, recipes_list):
            
            self.x=book_name
            self.y=last_update
            self.z=creation_time
            self.t=recipes_list
        def __str__ (self):
           return 'Book=(' + self.x + ',' + str(self.y) + ',' + str(self.z) +',' + str(self.t) +')'
        