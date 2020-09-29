# IS 403 - IS Junior Core 1-12
# Bryce Cindrich
# Hailey Hullinger
# Nathaniel Milligan
# Melissa Squires

import datetime

class Customer:
    company_name = 'Critter Watch'

    def __init__(self, first_name, last_name, address1, address2, city, state, zip):
        self.cust_id = self.gen_id(first_name, last_name, address1)
        self.first_name = first_name
        self.last_name = last_name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip = zip
        self.balance = 0.0
        self.cust_pets = []

    # generates customer id from first 3 characters from first name, 3 from last name, and 5 from address1
    def gen_id(self, first_name, last_name, address1):
        return first_name.replace(' ', '')[0:3] + \
            last_name.replace(' ', '')[0:3] + \
            address1.replace(' ', '')[0:5]

    def return_bill(self):
        try:
            # TODO: add appointment dates
            return (f'Customer {self.cust_id} with name {self.first_name} {self.last_name} '
                f'owes {self.balance} for {self.cust_pets[0].pet_name}\'s stay from '
                f'{self.cust_pets[0].appointments[0].begin_date} to {self.cust_pets[0].appointments[0].end_date}')
        except:
            print('ERROR: Make sure the pet has a name and the appointments have dates')
            return 'failed to return bill'

    def make_payment(self, payment):
        self.balance -= payment


class Pet:

    def __init__(self, pet_name, breed, age, owner):
        self.pet_name = pet_name
        self.breed = breed
        self.age = age
        self.owner = owner
        self.appointments = [Appointment(owner)]


class Appointment:

    def __init__(self, owner):
        self.begin_date = datetime.datetime.now()
        self.end_date = datetime.datetime.now()
        self.day_rate = 0.0
        self.total_days = 0
        self.total_cost = 0.0
        self.owner = owner
    
    def set_appointment(self, begin_date, end_date, day_rate):
        self.begin_date = begin_date
        self.end_date = end_date
        self.day_rate = day_rate
        self.total_days, self.total_cost = self.calc_days()
        self.owner.balance += self.total_cost

    # returns tuple of (total_days, total_cost)
    def calc_days(self):
        days = (self.end_date - self.begin_date).days
        if days <= 0:
            return (1, self.day_rate)
        else:
            cost = days * self.day_rate
            return (days, cost)


# collect num customers, but don't use it anywhere
num_customers = int(input('How many customers? '))

# collect customer information
first_name = input('Enter Customer\'s First Name: ')
last_name = input('Enter Customer\'s Last Name: ')
address1 = input('Enter Customer\'s Address1: ')
address2 = input('Enter Customer\'s Address2: ')
city = input('Enter Customer\'s City: ')
state = input('Enter Customer\'s State: ')
zip = input('Enter Customer\'s Zip: ')
# initialize customer object
oCust1 = Customer(first_name, last_name, address1, address2, city, state, zip)

# collect pet info
pet_name = input('Enter Customer\'s pet\'s name: ')
breed = input('Enter pet\'s breed: ')
age = input('Enter pet\'s age: ')
# initialize pet object
oCust1.cust_pets.append(Pet(pet_name, breed, age, oCust1))

# collect appointment info
begin_date = datetime.datetime.strptime(input('Enter start date in the format mm/dd/yyyy: '), '%m/%d/%Y')
end_date = datetime.datetime.strptime(input('Enter end date in the format mm/dd/yyyy: '), '%m/%d/%Y')
day_rate = float(input('Enter the day rate in the format 13.73: '))
# initialize appointment object
oCust1.cust_pets[0].appointments[0].set_appointment(begin_date, end_date, day_rate)

# print current bill
print(oCust1.return_bill())

# collect payment amount
payment = float(input('Enter the payment amount in the format 13.73: '))
# make payment
oCust1.make_payment(payment)

# print bill after payment
print(oCust1.return_bill())
