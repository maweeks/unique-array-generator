def say_hello():
    print( 'Hello, world!' )

def shorten(item, maxLength):
    return item[:maxLength]

def complex_process(result, toSort, maxLength, cutLength):
    toSortFurther = []
    for item in toSort:
        replacements=[]
        for x in range(10**cutLength):
            replacement = shorten(item[0], maxLength-cutLength) + str(x).rjust(cutLength, '0')
            if replacement not in result:
                replacements.append(replacement)

        if len(replacements) >= item[1]:
            result = result + replacements[:item[1]]
            toSort.remove(item)
        else:
            added = False
            newString = shorten(item[0], maxLength-(cutLength+1))
            for thing in toSortFurther:
                if newString == thing[0]:
                    thing[1] += item[1]
                    added = True
            if not added:
                toSortFurther.append([newString, item[1]])

    if len(toSortFurther) == 0:
        return result
    elif cutLength == maxLength:
        raise Exception("NOOOOOOOOOOOOOOOOO...WHYYYYYYYYYYYYYYYY")

    return complex_process(result, toSortFurther, maxLength, cutLength+1)

def process(items, maxLength):
    shortStrings = []
    for item in items:
        shortStrings.append(shorten(item, maxLength))

    result = []
    toSort = []

    for pointer in range(0, len(shortStrings)):
        count = shortStrings.count(shortStrings[pointer])
        if count == 1:
            result.append(shortStrings[pointer])
        else:
            item = [shortStrings[pointer], count]
            if toSort.count(item) == 0:
                toSort.append(item)

    if len(toSort) > 0:
        result = complex_process(result, toSort, maxLength, 1)

    return result

if __name__ == "__main__":
    say_hello()
