def age_greater_than_25(person):
    return person['age'] > 25
print(list(filter(age_greater_than_25, people)))
