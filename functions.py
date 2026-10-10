# def greet_user(username):
#     """ Display simple greeting """
#     print(f"hello, {username.title()}!")
    
# greet_user('azamat')    

# POSITIONAL_ARGUMENTS
# def describe_animal(animal_type, pet_name):
#     """ positional arguments that is describes and gives and receives"""
#     print(f"\n My animal {animal_type}")
#     print(f"My animal {animal_type} is name {pet_name.title()}")

# describe_animal(animal_type='hamster', pet_name='harry')    

# RETURN VALUES

# def get_formatted_name(first_name, last_name):
#     """ Return full formatted name """
#     full_name = f"{first_name}, {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jinne', 'hendrix')
# print(musician)


# Optional value

# def built_person(first_name, last_name, age=None):
#     """ Return persons name """
#     person = {'first': 'first_name', 'last': 'last_name'}
    
#     if age:
#         person['age'] = age
#     return person

# musician = built_person('jimmi', 'hendrix', age=27)
# print(musician)    

unprinted_designs = ['robot', 'toy car', 'plastic hand', 'game simulator']
completed_designs = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_designs.append(current_design)
#     print("\n The following models are printed")
#     for completed_design in completed_designs:
#         print(completed_design)
        
def print_models(unprinted_designs, completed_design):
    """
        Simulate printing each design, until none are left.
        Move each design to completed_models after printing.
    """        
    
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Pinting model: {current_design}")
        completed_designs.append(current_design)