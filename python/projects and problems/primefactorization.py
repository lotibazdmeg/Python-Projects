print("Welcome to the prime factorization game! Enter a number and find out the prime numbers.")



def main(n):
  running = True
  while running:
    list_of_prime_numbers = []
    inp = input("   Do you want to play? y or n: ")
    if inp == "n".lower():
      break
    elif inp == "y".lower():
      for i in range(1, n+1):
        if n % i == 0:
          list_of_prime_numbers.append(i)
      print(f'\t{list_of_prime_numbers}')
        

    





print(main(12))