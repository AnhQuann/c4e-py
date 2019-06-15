salary_table = [
    {
        "name": "Hai",
        "money": 50000,
        "days": 25,
        "hour_per_day": 8,
    },
    {
        "name": "Duc",
        "money": 25000,
        "days": 20,
        "hour_per_day": 8,
    },
    {
        "name": "Minh",
        "money": 20000,
        "days": 27,
        "hour_per_day": 5,
    },
    {
        "name": "Long",
        "money": 15000,
        "days": 30,
        "hour_per_day": 3,
    },
]

# minh = salary_table[2]
# print(minh["money"])

# name_input = input("Name? ")
# for person in salary_table:
#     if person["name"] == name_input:
#         month_salary = person["money"] * person["days"] * person["hour_per_day"]
#         print(month_salary)
#         break

total_salary = 0

for person in salary_table:
    each_person = person["money"] * person["days"] * person["hour_per_day"]
    total_salary += each_person

print(total_salary)
