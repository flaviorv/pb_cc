
def hanoi(discs, origin, destination, auxiliary):
    if discs == 1:
        print(f"Move disc 1 from {key(origin)} to {key(destination)}")
        decrease(origin)
        sum(destination)
        show_spindles(origin, destination, auxiliary)
    else:

        hanoi(discs -1, origin, auxiliary, destination)

        print(f"Move disc {discs} from {key(origin)} to {key(destination)}")
        decrease(origin)
        sum(destination)
        show_spindles(origin, auxiliary, destination)

        hanoi(discs -1, auxiliary, destination, origin)
     
          

def key(dictionary):
    keys = list(dictionary.keys())
    return keys[0]
    

def sum(dictionary):
    dictionary[key(dictionary)] += 1

def decrease(dictionary):
    dictionary[key(dictionary)] -= 1

def show_spindles(spindle1, spindle2, spindle3):
    spindles = [spindle1, spindle2, spindle3]
    left = 0
    aux = 0
    right = 0
    for spindle in spindles:
        if key(spindle) == "Left":
            left = spindle[key(spindle)]
        if key(spindle) == "Right":
            right = spindle[key(spindle)]
        if key(spindle) == "Aux":
            aux = spindle[key(spindle)]
    print(f"Spindles's state: {left} {aux} {right}")




def init(discs):
    if discs <= 0:
        return "Discs must be greater than 0"
    elif isinstance(discs, int) == False:
        return "Discs must be an integer"
    print("The Tower of Hanoi")
    print(f"Movements: {2**discs-1}")
    hanoi(discs, {"Left": discs}, {"Right": 0}, {"Aux": 0})
    


    
