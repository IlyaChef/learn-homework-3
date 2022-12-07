with open('referat.txt', 'r', encoding='utf-8') as referat:
    content = referat.read()
    print(content)
    print(len(content)) # длина строки 
    print(len(content.split())) # кол-во слов в тексте
    for exclamation in content: # замена точек на восклицательные знаки
        exclamation = content.replace('.', '!')
    print(exclamation)

    with open('referat2.txt', 'w', encoding='utf-8') as result:
        result.write(exclamation)  # запись результата в новый файл 
        