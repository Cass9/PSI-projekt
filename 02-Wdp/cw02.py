# Zadanie 1

a_list = [1, 2, 3, 4, 5]
b_list = [7, 8, 9, 10, 11]

def polaczListy(a_list, b_list):
    y = []
    for i, w in enumerate(a_list):
        if i%2 == 0:
            y.append(w)
    for i, w in enumerate(b_list):
        if i%2 != 0:
            y.append(w)        
    print(y)

polaczListy(a_list, b_list)

# Zadanie2

def zadanie2(data_text):
    slownik = {
        "lenght" : len(data_text),
        "letters" : list(data_text),
        "big_letters" : data_text.upper(),
        "small_letters" : data_text.lower()
    }
    print(slownik)

zadanie2("Cos tam")

# Zadanie3

def zadanie3(text, letter):
    text = text.replace(letter, "")
    print(text)

zadanie3("Mamma mia", 'a')

# Zadanie4

def przeliczanie(temp, temp_type):
    if temp_type == "fahrenheit" :
        temp = (temp * 9/5) + 32
    
