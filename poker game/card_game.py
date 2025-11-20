import random

from enum import IntEnum
card_types = (
    (1, "Ace"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
    (10, "10"),
    (11, "Jack"),
    (12, "Queen"),
    (13, "King"),
)
card_colors = ("clubs","diamonds","hearts","spades")

class Card:
    card_type = ""
    card_color = ""

    def __init__(self, card_type, card_color):
        self.card_type = card_type
        self.card_color = card_color

class CombinationType(IntEnum):
    Rolal_Flush = 10
    Straight_Flush = 9
    Four_Of_A_Kind = 8
    Full_House = 7
    Flush = 6
    Straight = 5
    Three_Of_A_Kind = 4
    Two_Pair = 3
    Pair = 2
    High_Card = 1

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f'{cls_name}.{self.name}'

class Combinations:
    cards = list()

    def __init__(self, cards):
        self.cards = cards

    def count_multible(self):
        local_score = 0

        containing_card_types = [card.card_type for card in self.cards]
        
        unique_card_types = set(containing_card_types)
        
        for type in unique_card_types:
            num_type = containing_card_types.count(type)
            
            if num_type >= 4:
                local_score += 8
            elif num_type >= 3:
                local_score += 3
            elif num_type >= 2:
                local_score += 2
            
        match(local_score):
            case 8:
                return CombinationType.Four_Of_A_Kind
            case 5:
                return CombinationType.Full_House
            case 4:
                return CombinationType.Two_Pair
            case 3:
                return CombinationType.Three_Of_A_Kind
            case 2:
                return CombinationType.Pair
            
        return CombinationType.High_Card
        
    def cards_in_order(self,num_draws = 5):
        royal_flush = sorted((card_types[0],) + card_types[-(num_draws-1):])
        containing_card_types = [card.card_type for card in self.cards]
        containing_card_colors = [card.card_color for card in self.cards]
        #print(containing_card_colors)

        same_color = (set(containing_card_colors).__len__() == 1)
        
        sorted_base = sorted(card_types)
        sorted_inner = sorted(containing_card_types)

        start_index = sorted_base.index(sorted_inner[0])

        comparing_array = sorted_base[start_index:start_index+num_draws]

        if royal_flush == sorted_inner and same_color:
            return CombinationType.Rolal_Flush

        if comparing_array == sorted_inner: 
            if same_color:
                return CombinationType.Straight_Flush
            else:
                return CombinationType.Straight
        elif same_color:
            return CombinationType.Flush
        
        return CombinationType.High_Card

def generate_cards():
    cards = [] 
    
    for card_color in card_colors:
        for card_type in card_types:
            cards.append(Card(card_color=card_color,card_type=card_type))
    return cards


def draw_cards(cards, num_draws, print = False):
    random.shuffle(cards)

    drawn_cards = cards[-num_draws:]
    
    if print:
        for card in drawn_cards:
            print(card)
    return drawn_cards


if __name__ == "__main__":
    default_val_plays = 100_000
    default_val_draws = 5

    input_str = input("Number plays:")
    num_plays = int(input_str) if type(input_str) is int else default_val_plays

    input_str = input("Number draws:")
    num_draws = int(input_str) if type(input_str) is int else default_val_draws
    
    cards = generate_cards()

    resulting_combinations = []

    for i in range(num_plays):
        result = CombinationType.High_Card
        drawn_cards = draw_cards(cards=cards,num_draws=num_draws)
        combinations = Combinations(drawn_cards)
        result = max(result, combinations.count_multible())
        result = max(result, combinations.cards_in_order())
        #print(result.name)
        resulting_combinations.append(result)
        del combinations

    for object in CombinationType:
        print(f"{object.name} Probability: {((resulting_combinations.count(object))/num_plays)*100}%")
        #print("ROYAL FLUSH!!!!!") if resulting_combinations.count(CombinationType.Rolal_Flush) > 0 else None