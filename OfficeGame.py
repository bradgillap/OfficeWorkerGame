# ! /usr/bin/python

print("**********************")
print("* Office Worker Game *")
print("**********************")

rooms = {
    1 : {
            "name" : "== Parking Lot ==",
            "desc" : "The parking lot is drab and grey with a large square building facing you. The only discernable feature is a blue door that leads to the side of the building stairwell."
        },
    2 : {
            "name" : "== Stairwell ==",
            "desc" : "Stairwell Description"
          },
    3 : {
            "name" : "== Office ==",
            "desc" : "Office Description"

        },
    4 : {
            "name" : "== Meeting Room ==",

          }
}

#print(rooms)

roomNum = int(input("Choose a room nummber: "))

print(rooms[roomNum]["name"])
print(rooms[roomNum]["desc"])