# List,dict and set comprehension:-

eco = """\t\nThis the programme based on the practice
for  list,dict,set and generator comprehension,use
this and modify according to your need.\n"""
print (eco)
print ("Practice exer. for data comprehension...")
print ("You're free to add number of elements according to your choice to comprehensionate:-")

while(True):
     how_many = int(input("\nTell the number of elements!\n"))
     elem_str = input("Add your elements seprated by space:\n ")
     tush = elem_str.split()

     print ("""What type of comprehension you want ?\n
1. List comprehension.
2. Dictionary comprehension.
3. Set comprehension.
4. Generator comprehension.""")
     com_type = int(input("Enter ur choice:\n"))
     if com_type==1: #List
        list= [i for i in tush]
        print (list)
        print (type(list))
     elif com_type==2: #Dict
          dict = {f"item,{i}":i for i in tush}
          print (dict)
          print (type(dict))
     elif com_type==3: #set
          set = {i for i in tush}
          print (set)
          print (type(set))
     elif com_type==4:
          gen = (i for i in tush)
          print (gen)
          print (type(gen))
          print ("Your generator is ready\n")
     else:
          print ("Select the right option")

     print ("Press e to quit and c to continue")
     press = input()
     if press=='e':
        exit()
     elif press=='c':
          continue
