def script(txt):
    txt1 = txt.split('.')
    k = 0
    for i in txt1:
        print(txt1[k].split())
        k += 1


text1 = open('sample copy.txt')
script(text1.read())
