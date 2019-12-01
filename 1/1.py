def getFuel(mass):
    return (mass//3)-2

def sumFuel(filename):
    total=0
    with open(filename) as f:
        for line in f:
            currentFuel = getFuel(int(line))
            total += fuelForFuel(currentFuel)
    return total

def fuelForFuel(currentFuel):
    toReturn = currentFuel
    while currentFuel > 0:
        currentFuel = getFuel(currentFuel)
        if currentFuel > 0:
            toReturn += currentFuel
    return toReturn

if __name__ == "__main__":
    currentFuel = sumFuel("input.txt")
    print(currentFuel)
