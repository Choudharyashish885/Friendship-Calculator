alphabet = 'bcghjklmpqrtvwxyz'  #remaining alphabets other than vowels and friends
score = 0
name = input("Enter first name and give space and than enter second name:- ")
for character in name:
    if character in 'aeiou':  #vowels with + score 5
        score+=5                                         #assignment operator -  score = score + 5
    if character in 'friends': #friends with + score 10
        score+=10
    if character in alphabet:
        score+=alphabet.find(character)               #it find the remaining alphabets position
    else:                                             #and multiply it with amount of times alphabet is used
        score+=0


if score>100:
    print('your friendship score is: ', score)
    print('Congratulation you both are best friends')
else:
    print('your friendship score is: ', score)

    '''
    this is for calculation score of alphabets other than vowels and friends 32
    position of alphabet l is at 6 and we used at 2 times so 6*2 = 12.
    '''