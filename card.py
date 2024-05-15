class Card:
    def __init__(self, value: int, suit: str):
        self.value = value
        # 1 is Ace, 11 is Jack, 12 is Queen, 13 is King
        self.suit = suit
    
    def get_value_string(self):
        valueString = ""
        match self.value:
            case 1:
                valueString = "A"
            case 11:
                valueString = "J"
            case 12:
                valueString = "Q"
            case 13:
                valueString = "K"
            case _:
                valueString = str(self.value)
        return valueString
    
    def __str__(self):
        return f"{self.get_value_string()}{self.suit[0].lower()}"