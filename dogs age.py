'''15 human years equals the first year of a medium-sized dog’s life.
Year two for a dog equals about nine years for a human.
And after that, each human year would be approximately five years for a dog.'''


dog_age = float(input('what is your dog age in human months? '))

if dog_age <= 12:
    dog_age = dog_age * 12 / 15
    print('Your dog is', dog_age,'years old in dog years')
elif  12 < dog_age > 24:
    dog_age = dog_age * 12 / 9
    print('Your dog is', dog_age, 'years old in dog years')
else:
    dog_age = dog_age * 12 / 5
    print('Your dog is', dog_age, 'years old in dog years')

