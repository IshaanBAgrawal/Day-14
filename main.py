# import required things
import random
import art
from game_data import data
from replit import clear


user_winning = True
user_status = ''
user_score = 0
running_no = 0
person_b_duplicate = ''
def game():
  global user_winning
  global user_status
  global user_score
  global running_no
  global person_b_duplicate
  clear()
# define the 2 personalities
  print(art.logo)
  print(user_status)

  person_a = random.choice(data)
  if running_no != 0:
    person_a = person_b_duplicate
  follower_count_of_person_a = person_a['follower_count']

  person_b = random.choice(data)
  follower_count_of_person_b = person_b['follower_count']

  while person_a == person_b:
    person_b = random.choice(data)

  person_b_duplicate = person_b

  print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")

  print(art.vs)
  print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")

  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  if user_choice == "a":
    user_choice = person_a['follower_count']
  elif user_choice == "b":
    user_choice = person_b['follower_count']

  larger_follower_person = 0
  if follower_count_of_person_a > follower_count_of_person_b:
    larger_follower_person = follower_count_of_person_a
  elif follower_count_of_person_b > follower_count_of_person_a:
    larger_follower_person = follower_count_of_person_b

  if user_choice == larger_follower_person:
    user_score += 1
    user_status = f"You're right! Current score: {user_score}."
  else:
    user_status = f"Sorry, that's wrong. Final score: {user_score}."
    user_winning = False

  running_no += 1


while user_winning is True:
  game()

if user_winning == False:
  clear()
  print(art.logo)
  print(user_status)
