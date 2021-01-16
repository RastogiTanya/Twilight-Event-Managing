d = {"Ranchoddas Chanchad" : [9876543210, 9638527410], "Raju Rastogi" : [9873216540], "Farhan Kureshi" : [9516238470]}

def store(n):

    l = []

    if (d.get(n, "none") == "none"):
        l.append(int(input("Enter the person's number: ")))

    else:
        l = list(d[n])
        l.append(int(input("Enter the person's number: ")))

    d[n] = l


def ret(n):
    b = []

    s1 = n.split(" ")
    s2 = []

    for i in s1:
        s2.append(i.capitalize())

    n = " ".join((s2))

    if (d.get(n, "none") == "none"):
        k = list(d.keys())

        for i in k:
            a = i.split(" ")

            for j in a:

                j = j.lower()

                if ((len(j) >= len(n)) and (len(n) > 2) and (j.count(n.lower()) > 0)):
                    b.append(i)
                    break

                elif ((len(j) >= len(n)) and (len(n) <= 2) and (j.count(n.lower(), 0, len(n)) > 0)):
                    b.append(i)
                    break

        if (len(b) > 0):
            b = sorted(b)

            print("\nSearch results:")
            for i in b:
                print(i)

            ret(str(input("\nEnter the person's name: ")))

        else:
            if (choice((str(input("\nWrong entry. Would you like to continue?(Y/N): "))).lower()) == "y"):
                ret(str(input("\nEnter the person's name: ")))

    else:
        print("Name: \n   " + n + "\nContact: ")

        for i in range(len(d[n])):
            print("   " + str(i+1) + ") " + str(d[n][i]))

def choice(c):

     if ((c == "n") or (c == "no")):
         return "n"
     elif ((c == "y") or (c == "yes")):
         return "y"
     else:
         return choice((str(input("\nInvalid input. Please enter your choice again.(Y/N): "))).lower())


while (True):

    print(d)

    want = input("\nWhat do you wish to do?\n1) Store\n2) Retrieve\n3) Exit \n\nYour Choice: ")
    want = want.lower()

    if (want == "store"):

        store(str(input("\nEnter the person's name: ")))

        if (choice((str(input("\nDo you want to access the data?(Y/N): "))).lower()) == "n"):
            break

    elif (want == "retrieve"):

        ret(str(input("\nEnter the person's name: ")))

        if (choice((str(input("\nDo you want to access the data?(Y/N): "))).lower()) == "n"):
            break
    elif(want=="exit"):
        break
    else:
        print("Invalid input. Please enter your choice again...\n")
    print("program finished...")
