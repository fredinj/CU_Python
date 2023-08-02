## 1 - List Comprehension

li=[i for i in range(1,101)]
li.extend([22,45,65,24,54,68,99,21])

by3=[i for i in li if i%3==0]
print("\nThere are",len(by3),"numbers in the list divisible by 3:\n",by3)

sq=[i**2 for i in li if i%2==0]
print("\nSquares of",len(sq),"even numbers:\n",sq)

s=sum([i for i in li if i%2==0])
print("\nSum of all even numbers in the list = ",s)

print("\nOriginal List:\n",li)
li=list(set(li))
print("\nDuplicates Removed:\n",li,"\n\n")


## 2 - Witcher books and their release dates

witcher={"The Last Wish":"21 December 2000","Sword of Destiny":"20 December 2001","Blood of Elves":"19 December 2002","Time of Contempt":"30 October 2005",
"Baptism of Fire":"18 January 2006","The Tower of Swallow":"15 April 2007","The Lady of the Lake":"April 1 2008","Season of Storms":"April 28 2010"}

def releaseDate(name):
    print(name,"was released in",witcher[name],"\n")