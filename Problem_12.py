"""Set Operations:

* Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
* Find the union, intersection, and difference between the two sets.
* Add a new fruit to your set.
* Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?"""

mf = {"apple", "mango", "grapes"}
ff = {"butterfruit", "watermelon", "orange","apple"}

print(mf | ff)
print(mf & ff)
print(mf - ff)

mf.add("bananna")
print(mf)

mf.remove("mango")
print(mf)

mf.discard("mango")
print(mf)
