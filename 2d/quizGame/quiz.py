questions = ("Apa ibukota Indonesia?: ",
             "Apa mata uang saudi arabia?: ",
             "Apa bahasa resmi china?: ",
             "Siapakah presiden ke-3 di Indonesia?: ",
             "1 ringgit berapa rupiah?: ")

options = (("A. Medan", "B. Jakarta", "C. Bandung", "D. Cimahi"), 
           ("A. Dollar", "B. Won", "C. Riyal", "D. Rupiah"), 
           ("A. Mandarin", "B. Tagalog", "C. Hokkien", "D. Arab"), 
           ("A. Soekarno", "B. Jokowi", "C. Prabowo", "D. Habibie"),
           ("A. Rp3.500", "B. Rp10.000", "C. Rp4.000", "D. Rp1.450"))
answers = ("B", "C", "A", "D", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print('----------------------')
    print(question)
    for option in options[question_num]:
        print(option)
        
        
    guess = input('pilih jawaban ini (A, B, C, D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print('CORRECT!')
        score += 1
    else:
        print('INCORRECT!')
        print(f'{answers[question_num]} is the correct answer' )
    question_num += 1

print('----------------------')
print('       RESULTS        ')
print('----------------------')

print("answers: ", end='')
for answer in answers:
    print(answer, end=' ')
print()

print("guesses: ", end='')
for guess in guesses:
    print(guess, end=' ')
print()

score = int(score / len(questions) * 100)
print(f'Your score is {score}%')