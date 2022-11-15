#Basic structure of anny class in Python:

class Customer:
    def __init__(self, name, membership_type):      #'name' et 'membership_type' sont des 'parametres' car ils sont dans la partie de définition
        self.name = name
        self.membership_type = membership_type
    def update_membership(self, new_membership):
        self.membership_type = new_membership


customers = [Customer("Caleb", "Gold"), Customer("Brad", "Bronze")]  # 'Caleb' et 'Gold' sont des 'arguments' car nous avons donné des variables spécifiques 
print(customers[0].name)