#To Do List

#Read from txt doc
def readFromExternalFile(filename):
    external_items = []

    with open(filename) as f:
        external_items = f.read() .splitlines()
    return external_items

def listTrimming(external_items):
    external_items_trimmed = []
    for item in external_items:
        if item.strip() != '':
            external_items_trimmed.append(item)

    return external_items_trimmed

#Add Item

#Remove Item

def main():
    print(listTrimming(readFromExternalFile("TO DO LIST.txt")))

main()