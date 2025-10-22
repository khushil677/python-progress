letter = ''' Dear <|Name|>,
            You are selected!
             <|Date|> '''

print(letter.replace("<|Name|>", "Khushil").replace("<|Date|>", "17/09/10"))
