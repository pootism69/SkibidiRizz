i = 1
n = 100

while i < n:
    output = ""
    dictionaryNum = {1:"Skibidi", 3:"Biden", 5:"Toilet", 7:"Brainrot", 11:"Sigma", 13:"Aura", 2:"Rizz"}

    for x in dictionaryNum.keys():
        if i % x == 0:
            output = output + dictionaryNum.get(x)
    
    if output == "":
        output = i
    
    print(output)

    i = i + 1
