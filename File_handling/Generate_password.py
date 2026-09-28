import random

alphabet = "abcdefghijklmnopqrstuvwxy"
password = random.choice(alphabet)+ str(random.randint(0,10)) + random.choice(alphabet)+ str(random.randint(0,10)) + random.choice(alphabet)+ str(random.randint(0,10))
print("Your password is :",password)