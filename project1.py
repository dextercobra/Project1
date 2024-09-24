#This project aims to calculate the water usage of a person and in turn make them think about their enviornmental impact
#I looked up how to do if/else commands on google this is advanced project 1.3
#There are three blank print functions in this project this is just to break up the text so it doesn't look like as much
print("")
showernum = int(input("How many showers do you take a week? "))
if showernum == '0':
 print("Come back once you've taken a shower.")
 exit()
else: 
 showerlength = int(input("How many minutes do your showers take on average? "))
 #This next part calculates how many gallons of water (10 gallons per 5 minutes) a person uses per week
 waterconsumption = (((int(showerlength)/5)*10)*int(showernum))
 print("You use " + str(waterconsumption) + " gallons of water a week on average.")
 print("")
 #Idk what the actual average is i just looked up the yearly average and divided it by 7
 print("The average person in the USA uses 120 gallons of water showering per week")
 avgusa = 120
 if avgusa == waterconsumption:
  print("You use the exact amount of water the average person does!")
 else:
  if avgusa < waterconsumption:
   print("You use " + str(round(((waterconsumption/120)*100)-100)) + "% more water than the average person" )
  elif avgusa > waterconsumption:
   print("You use " + str(round((100-(waterconsumption/120)*100))) + "% less water than the average person" )
print("")

