# module/class/run_class.py

import classPerson

name = "pipusana petgumpoom"
age = 26
address = "London"

person = classPerson.Person(name, age, address)

print(person.get_name())
print(person.get_age())
print(person.get_address())
print(person.get_info())