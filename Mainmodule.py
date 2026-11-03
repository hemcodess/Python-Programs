import Module
print(Module.full_name('Hema','Sai'))
print("")
print("Impost functions from a module")

from Module import full_name, sum_two_nums, person,  gravity
print(full_name('hema', 'lata'))
print(sum_two_nums(1, 9))
mas = 100
weight = mass * gravity
print(weight)
print(person['firstname'])