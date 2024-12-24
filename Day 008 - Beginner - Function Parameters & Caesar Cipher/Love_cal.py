def calculate_love_score(name1, name2):
    couple = name1+name2
    true_check = "true"
    love_check = "love"
    true_score = 0
    love_score = 0

    for letter_input in couple.lower():
        for letter_check in true_check:
            if letter_check == letter_input:
                true_score += 1

    for letter_input in couple.lower():
        for letter_check in love_check:
            if letter_check == letter_input:
                love_score += 1      
    
    print(str(true_score)+str(love_score))

calculate_love_score("Tanaratta Umpon", "Roongnapa Mongkolnit")