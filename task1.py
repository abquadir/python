# Write a program to create an Enum object and display a member name and value

# Sample data : Afghanistan = 93 Albania = 355 Algeria = 213 Andorra = 376 Angola = 244 Antarctica = 672

# Expected Output : Member name: Albania Member value: 355


from enum import Enum

class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print('Member name : {}'.format(Country.Albania.name))
print('Member value : {}'.format(Country.Albania.value))



# OUTPUT
# waris@vostro:/Desktop/python_task$ python3 task1.py 
# Member name : Albania
# Member value : 355