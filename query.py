from movies import Movies

def main() :
    movies = Movies('./movies.txt')
    choice = ""
    keyword = ""
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
            keyword = input("enter a word to search: ")
            movies.search_movies_by_name(keyword)
            break
        elif choice == "sc" :
            keyword = input("enter a word to search: ")
            movies.search_movies_by_cast(keyword)
            break
        elif choice == "list" :
            movies.list_all_movies()
            break
        print()

main()
