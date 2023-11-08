# Put this at the top of your kata01.py file
kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}
kata01_output = '{} was created by {}'

for kata_key in kata.keys():
    print(kata01_output.format(kata_key, kata[kata_key]))