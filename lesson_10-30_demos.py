class tea: 
    '''varieties of team for my tea shop'''

    def __init__(self, name, allergens = None):
        self.name = name
        self.allergen = allergens
       
    def brew(self): 
        print(f'How about a nice cup of {self.name}?')
        print(f'Please collect your tea from the counter!')
    
    def restock(self):
        print(f'Tea emergency! We are out of {self.name}, which is a {self.type} varierty.')
        self.instock = 'n'
        print("Sorry, we only have teabags")

# gr_jas = tea('jasmine green tea', 'green')
# oo_peo = tea('white peony oolong', 'oolong')
# bl_alm = tea('almond darjeeling', 'black', 'tree nut')


class blacktea(tea):
    '''varieties of black tea'''
    def __innit__(self, name, strength, allergen, caffeinated = 'y'):
        super().__init__(name, allergen)
        self.strength = strength
        self.caffeinated = caffeinated

bl_asm = blacktea('Assam', 'none', 'full-bodied')

print(f'''
{bl_asm.name}
{bl_asm.allergen}
{bl_asm.caffeinated}
      ''')





# gr_jas.restock()


# print(gr_jas.name, gr_jas.looseleaf)
# print(oo_peo.name, oo_peo.looseleaf)
# print(bl_alm.name, bl_alm.looseleaf)








# print(f'Can I have a cup of {gr_jas.name}')
# oo_peo.brew()

# print(f'''
#    known allergens: ''')
 
# print(gr_jas.name, '- allergen:', gr_jas.allergen, '- in stock? : ', gr_jas.instock)
# # {oo_peo.name}: {oo_peo.allergen}
# # {bl_alm.name}: {bl_alm.allergen}      

# gr_jas.restock()