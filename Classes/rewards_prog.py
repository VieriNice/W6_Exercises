cust_list = []

class RewardsPrograms:
    '''This class shows a rewards prgram'''
    
    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
    def prof(self):
        print(f'Name: {self.cust_name}')
        print(f'Phone: {self.phone}')
        print(f'Email: {self.email}')

    def thank_you(self):
        print(f'Thank you, {self.cust_name}, for visiting our restaurant!')
    
    def add_to_cust_list(self):
        cust_list.append(self.cust_name, self.phone, self.email)

customer1 = RewardsPrograms('Vieri Escamilla', '7734445698', 'escamillavieri@yearup.org')
customer2 = RewardsPrograms('Gisselle Mora', '7734304567', 'gmora12@yahoo.com')
customer3 = RewardsPrograms('Bruce Wayne', '7734304589', 'bwayne@yahoo.com')

