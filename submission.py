#Liam Duffy 
#CSCI 128



Gate = input("Gate> ")
INP1 = int(input("INP1> "))
INP2 = int(input("INP2> "))

Gates_List = ["AND", "OR", "NAND", "NOR", "XOR", "XNOR"]

if Gate not in Gates_List:
    print(f"OUTPUT Invalid Gate {Gate}")

elif INP1 != 0 and INP1 != 1:
    print(f"OUTPUT Invalid Input {INP1}")

elif INP2 != 0 and INP2 != 1: 
    print(f"OUTPUT Invalid Input {INP2}")
else:
    if INP1 == 0: 
        INP1 = False
    else: 
        INP1 = True
    
    if INP2 == 0: 
        INP2 = False
    else: INP2 = True
    
    if Gate == "AND":
        print(f"OUTPUT {INP1 and INP2}")
    
    elif Gate == "OR":
        print(f"OUTPUT {INP1 or INP2}")
    
    elif Gate == "NAND":
        print(not{INP1 and INP2})
    
    elif Gate == "NOR":
        print(f"OUTPUT (not{INP1 or INP2})")
    
    elif Gate == "XOR":
        print(f"OUTPUT {(INP1 ^ INP2)}")
    
    elif Gate == "XNOR":
         print(f"OUTPUT{not(INP1 ^ INP2)}")
   
   
    
    
  
   
    
    
   









    
