print("Hi! Welcome to the prime number game!")

def main():
  running = True
  while running:
    inp = input("   Do you want to play? y or n: ")
    if inp == "y".lower():
      lowest_range = int(input("      Please enter the lowest range you would like to see prime numbers: "))
      highest_range = int(input("     Please enter the highest range you would like to see prime numbers: "))

      for i in range(lowest_range, highest_range+1):
        if i > 1:
          for j in range(2, i):
            if (i % j) == 0:
              break
          else:
            print(i)
            continue

if __name__ == "__main__":
  main()
