birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

print("We have these birthdays :")

for birth in birthdays:
    print("{}".format(birth))

name = raw_input("Whose info you want :")
if name in birthdays:
    print("{} has birthday on {}".format(name,birthdays[name]))