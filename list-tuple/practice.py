#WAP to ask the user to enter names of their 3 favorite movies and store them in list .
# movie1 = input("Enter your favorite movie name:")
# movie2 = input("Enter your favorite movie name:")
# movie3 = input("Enter your favorite movie name:")
# list = (movie1, movie2, movie3)
# print (list)
# print (type (list))


movies = []
mov1 = input("Enter your first movie name :")
mov2 = input("Enter your second movie name :")
mov3 = input("Enter your third  movie name :")

movies.append(mov1)
movies.append (mov2)
movies.append (mov3)

print(movies)
print (type (movies))


# WAP to check if a list containss a palindrome od element . (hint: use copy ()method )
# [1,2,3,2,1]

list = ["m", "a", "a", "m"]
copy_list = list.copy()
copy_list.reverse

if (copy_list==list):
    print("palindrome")
else:
    print("not palindrome ")