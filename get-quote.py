#import random
def first():
 # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  #last = 13
  #rnd = random.randint(0, last)
  #for i in range(len(quotes)):
  count = 0
  for line in quotes:
    count += 1
    print(line)
  print("Please enter the line numbers from 0-", count,":")
  num = int(input())
  print(quotes[num])
 
 #Write New Line
  f = open("quotes.txt", "a")
  line = input("Enter new line:")
  f.write("\n")
  f.write(line)
  f.close()
  #f = open("quotes.txt")
  lst = list(open("quotes.txt"))
  lastline = lst[-1]  
  print("This is the latest line:", lastline)

if __name__== "__main__":
  first()
