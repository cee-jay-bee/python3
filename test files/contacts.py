contacts = {
    'number': 4,
    'students': 
        [
            {'name': "CJ Barnes", 'email':'cj@example.com'},
            {'name': "Theresa Ha", 'email':'theresa@example.com'},
            {'name': "Mia Barnes", 'email':'mia@example.com'},
            {'name': "Emma Barnes", 'email':'emma@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])