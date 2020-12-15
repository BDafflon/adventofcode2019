from math import floor

def day1_2(data):
    if floor(int(data)/3)-2 <=0 :
        return 0
    else:
        return floor(int(data)/3)-2 + day1_2(floor(int(data)/3)-2)

if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    linesDeMonFichier = fichier.read().splitlines()
    data = [ floor(int(d)/3)-2 for d in linesDeMonFichier]
    print(sum(data))

    data = [ d+day1_2(d)  for d in data]
    print(sum(data))
