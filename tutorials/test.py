def main():
  #reversing a STRING
  var = "lets try this with dummy variables"
  print(" org var : %s " %var)
  var = var.replace('this','these')
  print("replaced var : %s " %var)
  print(":").join("python")
  var = ''.join(reversed(var))
  print(var)
  #shortcut and efficient way of reversing a string
  print(var[::-1]) 

  #tuples in python 
  tup = ("sathish", "vtu" , "east west intitute of technology");
  tup2 = ("dd", "vtu2", "ewit");
  print(tup2)
  (name, university, coll) = tup
  #(name, university, coll) = tup2
  print(name)
  print(university)
  print(coll)
  name = raw_input("enter the name " )
  print(name)

if __name__ == "__main__" :
  main()

