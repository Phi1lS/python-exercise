from movies import Movies

def main() :
    movies = Movies('./movies.txt')
    choice = ""
    word = ""
    while True :
        print("q: quit")
        print("sn: search movie names")
        print("sc: search casts")
        print("list: print all the movie names")
        choice = input()
        if choice == 'q' :
            print("Exiting the program")
            break
        elif choice == "sn" :
            word = input("enter a word to search: ")
            break
        elif choice == "sc" :
            word = input("enter a word to search: ")
            break
        elif choice == "list" :
            break
        print()

main()
