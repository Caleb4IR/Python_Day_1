rooms_list = [
  {"room_number": 101, "bed_type": "Single", "smoking": False, "availability": True},
  {"room_number": 102, "bed_type": "Double", "smoking": True, "availability": True},
  {"room_number": 103, "bed_type": "Single", "smoking": False, "availability": True},
  {"room_number": 104, "bed_type": "Double", "smoking": True, "availability": False}
]

def add_room(rooms, room_number, bed_type="Double", smoking=False): 
  room = {
      "room_number": room_number, "bed_type": bed_type, "smoking": smoking, "availability": True 
  }
  rooms.append(room)

def book_room(rooms, preferred_bed_type="Double", smoking_preference=False):
  available_rooms = [room for room in rooms if room["availability"] and room["bed_type"] == preferred_bed_type and room["smoking"] == smoking_preference]
  if available_rooms:
      booked_room = available_rooms[0]
      booked_room["availability"] = False
      print(f"Room {booked_room['room_number']} booked successfully.")
  else:
      print("No available room matching the preferences.")

def list_available_rooms(rooms):
  print("Available rooms:")
  for room in rooms:
      if room["availability"]:
          print(f"Room {room['room_number']}: {room['bed_type']} bed, Smoking: {room['smoking']}")

# Add a room
room_number = int(input("Enter room number: "))
bed_type = input("Enter bed type (Single/Double): ").capitalize()
smoking = input("Is smoking allowed in the room? (True/False): ").capitalize()
added_smoke_preference = True if smoking == "True" else False

add_room(rooms_list, room_number, bed_type, added_smoke_preference)

# List available rooms after adding
list_available_rooms(rooms_list)

# Book a room
preferred_bed_type = input("Enter preferred bed type (Single/Double): ").capitalize()
smoking_preference = input("Smoking preference (True/False): ").capitalize()
smoke_preference = True if smoking_preference == "True" else False

book_room(rooms_list, preferred_bed_type, smoke_preference)

# List available rooms after booking
list_available_rooms(rooms_list)







