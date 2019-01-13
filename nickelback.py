# Define a set that contains tuples. Each tuple should contain two strings:

# The name of an artist
# A song by that artist
# Make sure that some of the songs are from the band Nickelback. You can see a list of their greatest hits on Amazon.

# # Example set
# songs = {
#     ('Nickelback', 'How You Remind Me'),
#     ('Will.i.am', 'That Power'),
#     ('Miles Davis', 'Stella by Starlight'),
#     ('Nickelback', 'Animals')
# }
# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

songs = {
  ("John Mayer", "Gravit"),
  ("Lenny Kravitz", "American WOman"),
  ('Nickelback', 'How You Remind Me'),
  ('Nickelback', 'Animals'),
  ('Earth Wind And Fire',"Do you remember" )
}

nonNickleBack = [song for song in songs if song[0] != "Nickelback" ]

print(nonNickleBack)


# Messing with lambda for fun

def myFun(a):
  return lambda b: a*b

doubler = myFun(2)
trippler = myFun(3)

print(doubler(10))
print(trippler(10))