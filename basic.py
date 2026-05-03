
# loopdata = [1,3,4,4]
# loopdata= "purushothaman"
loopdata = (1,5,6,8,)
loopdata = 1
loopdata = True
loopdata = {"name":"abi",
            "age":23}

name = 1
if name ==1:
    print("condition")
else:
    print("else condition ")

# Python has one for loop, but we use it with list, string, range, dictionary, tuple, set, etc.
for data in loopdata:
     print(data)
# switch 
match name :
    case 200:
        print()
    case 1:
        print()

# while True :
#     print("asas")

def function(here):
    try:
        return f"this is return:{here} "
    except Exception as e:
        print(e)
    finally:
        print("final")
    

print(function("abi"))


