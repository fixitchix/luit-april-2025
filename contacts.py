contacts = {
    'number': 4,
    'students':
    [
        {'name': 'Tracy Downs', 'email':'tracy@example.com'},
        {'name': 'Harry Potter', 'email':'harry@example.com'},
        {'name': 'Frasier Crane', 'email':'frasier@example.com'},
        {'name': 'Jessica Fletcher', 'email':'jessica@example.com'}
    ]
}

# Will give us the email list only
print('Student emails:')
for student in contacts ['students']:
    print(student['email'])