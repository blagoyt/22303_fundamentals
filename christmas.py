toys_size = input()
toys_color = input()
batches = int(input())

if toys_color == "Red":
    if toys_size == "Large":
        price = batches * 16
        
    elif toys_size == "Medium":
        price = batches * 13
        
    elif toys_size == "Small":
        price = batches * 9
        
elif toys_color == "Green":
    if toys_size == "Large":
        price = batches * 12
        
    elif toys_size == "Medium":
        price = batches * 9
        
    elif toys_size == "Small":
        price = batches * 8
        
elif toys_color == "Yellow":
    if toys_size == "Large":
        price = batches * 9
        
    elif toys_size == "Medium":
        price = batches * 7
        
    elif toys_size == "Small":
        price = batches * 5
        

final_price = price * 35 /100
print(f"You have earned {final_price} leva.")