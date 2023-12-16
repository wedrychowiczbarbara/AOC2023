
cards_strength_dict = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}

def get_points(cards_all):
    cards = []
    for card in cards_all:
        cards.append(card)
    cards = list(set(cards))
    occurrences = []
    for card in cards:
        counter=0
        for x in cards_all:
            if card==x:
                counter+=1
        occurrences.append([card, counter])
    return occurrences

print(get_points('AABAA'))