movies = {
    "War": [3, 5],
    "Bourne": [18, 5],
    "Gully boy": [15, 5],
    "Uri": [12, 5]
}

film = input("Enter movie name: ")
age = int(input("Enter your age: "))

if film in movies:
    required_age, seats = movies[film]
    
    if age >= required_age:
        if seats > 0:
            print("You can watch the movie. Ticket booked.")
            movies[film][1] -= 1
        else:
            print("Sorry, no seats available.")
    else:
        print("You are not eligible to watch this movie.")
else:
    print("Movie not available.")
