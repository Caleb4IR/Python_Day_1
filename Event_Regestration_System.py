# Exercise: Event Registration System
# Objective: Write a Python program that includes a function to register participants for an event. The registration function should handle participant details and their preferences with default values for some parameters.
# Initial Setup
# Participants need to provide their name and email. Additionally, they can specify their meal preference (vegetarian or non-vegetarian) and if they need accommodation. By default, the meal preference should be set to "non-vegetarian", and accommodation required should be False.
# Task
# Registration Function: Write a function register_participant(name, email, meal_preference="non-vegetarian", needs_accommodation=False) that registers a participant with their provided details and preferences.
# Display Registered Participants: After registration, display the participant's details, including their name, email, meal preference, and accommodation needs.
# Expected Functionality
# Registering a participant with all details specified.
# Registering a participant with only the name and email, using default values for the other parameters.

def register_participant(name, email, meal_preference="non-vegetarian", needs_accommodation=False):
  participant_details = {
      "Name": name,
      "Email": email,
      "Meal Preference": meal_preference,
      "Accommodation Needed": needs_accommodation
  }
  return participant_details

def display_registered_participant(participant_details):
  print("Registered Participant Details:")
  for key, value in participant_details.items():
      print(f"{key}: {value}")

# Get participant details
name = input("Enter your name: ")
email = input("Enter your email address: ")
meal_preference_input = input("Enter your meal preference (vegetarian/non-vegetarian): ").lower()
meal_preference = meal_preference_input if meal_preference_input in ["vegetarian", "non-vegetarian"] else "non-vegetarian"
needs_accommodation_input = input("Do you need accommodation? (yes/no): ").lower()
needs_accommodation = needs_accommodation_input == "yes"

# Register the participant with provided details
participant_details = register_participant(name, email, meal_preference, needs_accommodation)

# Display registered participant details
display_registered_participant(participant_details)