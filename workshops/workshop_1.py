# assigned x the value of 5
x = 5 # number
# printing the value
# print(x)
 
# This is our Mudkip
mudkip_lvl = 15.5 # float (decimal)
mudkip_name = 'Mudkip' # string (str)
mudkip_current_exp = 15 # integer (int)
mudkip_total_exp_needed = 30 # integer (int)
 
# assigning 
# x = 15
# print(x)
# mudkip = float(x) # converting the value 15 from an integer to a float
# print(mudkip)
# print(x)
 
# Combines the mudkip name with colon and the
# stringified version of mudkip_lvl
# mudkip_lvl = mudkip_lvl + 1
# operators: 
# + (addition)
# - (subtraction)
# / (division)
# * (multiplication)
# ** (power of)
# mudkip_lvl += 1 --> mudkip_lvl = mudkip_lvl + 1
 
# mudkip health damage
#         30      10
# have two variables, one for health and one for damage, then display the health before taking damage and after taking damage
 
# mudkip_health = 30
# damage = 10
# print(mudkip_health)
# mudkip_health = mudkip_health - damage
# print(mudkip_health)
 
# mudkip_health = 30
# damage = 10
# print("Mudkip health before taking damage: " + str(mudkip_health))
# mudkip_health -= damage # same thing as what we did on line 37
# print("Mudkip health after taking damage: " + str(mudkip_health))
 
# mudkip_lvl = 15
 
# print("mudkip lvl: " + str(mudkip_lvl))
# print("mudkip leveled up!!")
# mudkip_lvl += 1
 
# print("mudkip lvl: " + str(mudkip_lvl))
 
# is_mudkip_evolving = mudkip_lvl == 16
# print('Is mudkip evolving: ' + str(is_mudkip_evolving))
 
# mudkip health damage
#         30      30
# have two variables, one for health and one for damage, then display the health before taking damage and after taking damage 
# have a comparison for the health at the end of the program and print "Is mudkip KO: " followed by the boolean value
 
 
mudkip_health = 30
damage = 200
print("Mudkip health before taking damage: " + str(mudkip_health))
mudkip_health -= damage # same thing as what we did on line 37
print("Mudkip health after taking damage: " + str(mudkip_health))
is_mudkip_ko = mudkip_health == 0
is_mudkip_overkilled = mudkip_health < 0
print("Is Mudkip KO: ", str(is_mudkip_ko))
 
# comparators 
# == (equality)
# > (superior)
# < (inferior)
# >= (superior or equal)
# <= (inferior or equal)
# != (different)
 
if is_mudkip_ko:
  print("Mudkip is KO")
elif is_mudkip_overkilled:
  print("Mudkip has been terminated.")
else:
  print("Mudkip is alive and kicking.")
