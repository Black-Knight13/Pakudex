from pakudex import Pakudex       # import class


def main():                           # main function

    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        try:
            cap = int(input("Enter max capacity of the Pakudex: "))
            if cap < 0:
                raise ValueError                                            # checks for invalid entries
            break
        except ValueError:
            print("Please enter a valid size.")

    ash = Pakudex(cap)                                                   # variable for access to pakudex
    print(f"The Pakudex can hold {cap} species of Pakuri.")
    while True:
        print('''Pakudex Main Menu
-----------------
1. List Pakuri                                                                   
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit''')
                                                                                 # main menu
        option = input("What would you like to do? ")

        if option == "1":                                                    # shows list of pakuri
            i = 1
            red = 0
            if len(ash.pakuris) == 0:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")

                for species in ash.get_species_array():
                    print(f"{i}. {ash.get_species_array()[red]}")
                    i += 1
                    red += 1

        elif option == "2":
            name = input("Enter the name of the species to display: ")                 # shows Pakuri and stats
            if name in ash.get_species_array():
                print(f"Species: {name}")
                 
                print(f"Attack: {ash.get_stats(name)[0]}")
                print(f"Defense: {ash.get_stats(name)[1]}")
                print(f"Speed: {ash.get_stats(name)[2]}")
            else:
                print("Error: No such Pakuri!")

        elif option == "3":
            try:
                if ash.size != ash.capacity:                                                        # adds Pakuri
                    caught = input("Enter the name of the species to add: ")
                else:
                    raise ValueError

            except ValueError:
                print("Error: Pakudex is full!")                                                      # checks for full dex
                continue

            if ash.add_pakuri(caught) is True:
                print(f"Pakuri species {caught} successfully added!")

            elif caught in ash.get_species_array():
                print("Error: Pakudex already contains this species!")

        elif option == "4":
            name = input("Enter the name of the species to evolve: ")
                                                                                                       # evolves species
            if name in ash.get_species_array():
                ash.evolve_species(name)

                print(f"{name} has evolved!")

            else:
                print("Error: No such Pakuri!")

        elif option == "5":
            ash.sort_pakuri()                                                             # sorts species

            print("Pakuri have been sorted!")

        elif option == "6":
            print("Thanks for using Pakudex! Bye!")                                 # exits loop
            break
        else:
            print("Unrecognized menu selection!")                                       # accounts for invalid entries


if __name__ == "__main__":
    main()
