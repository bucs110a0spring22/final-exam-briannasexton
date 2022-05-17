import random
import Horoscope
import DailyDogFact

def main():
  name = input("User Name:")
  message = "Good Morning!,"+ (name) +", Have A Great Day!"
  print(message)
  answer = input("Would You Like Your Horoscope or A Dog Fact?")
  if answer == "Dog Fact":
    DailyDogFact.DogFacts()
    print(DailyDogFact)
  elif answer == "Horoscope":
    Horoscope.yourHoroscope()
    print(Horoscope)

  




main()