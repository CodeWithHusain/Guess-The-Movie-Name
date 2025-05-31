import random
movies = ['anand',"drishyam",'nayak','golmal','good-dinosour','frady','dangal','titanic','manichitrathazhu','tare-zameen-par','suryavanshi','bahubali','mission-mangal']

picked_movie=random.choice(movies)

processing_movie=list(picked_movie)


for i in range (len(picked_movie)):
    if (random.random()<0.5):
        processing_movie[i]='_'

print(processing_movie)
guessed_movie=input("guess the movie name:")

if(guessed_movie.lower()!=picked_movie.lower()):
    print(f"you are a faliure, rigth answer was {picked_movie} ")
    
else:
    print("take your trophy ")
