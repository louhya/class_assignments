'''15 human years equals the first year of a samll-sized dog’s life.
Year two for a dog equals about nine years for a human.
And after that, each human year would be approximately five years for a dog.'''


dog_age = float(input('How old is your dog? (in years)'))

if dog_age <= 1:
    dog_age = dog_age * 15
    print('Your dog is', dog_age,'years old in dog years')
elif  1 < dog_age <= 2:
    dog_age = 15 + (dog_age-1) * 9
    print('Your dog is', round(dog_age), 'years old in dog years')
else:
    dog_age = 24 + (dog_age-2) * 5 - (dog_age-2)
    print('Your dog is', round(dog_age), 'years old in dog years')