#Final Project for Computing (Sarah & Krystian)
import numpy as np 
from tabulate import tabulate #to create the table
###################################################

user_name = str(input("Please Input your Name: ")) #this code is done for a building in NYC
print('')
print(('Welcome to S&K Estimating, {}. Please answer the following questions for your cost estimate.').format(user_name))
build_type = ''
user_in = False
tot_low = 0
tot_high = 0
sqft_low = 0
sqft_high = 0

class Cost: #creating a class to help organize the input values and to be able to store them for the total calculation
  def __init__(self, sqft, USD_sqft_low, USD_sqft_high): #these are the inputs that have numerical values that will be used to calculate the cost
    self.sqft = sqft #user inputs the size they want
    self.USD_sqft_low = USD_sqft_low #the high and low factors are based on the type of building and the building use they user chooses 
    self.USD_sqft_high = USD_sqft_high
  def range_cost(self, sqft, USD_sqft_low, USD_sqft_high): #high and low values are used to give the user a range of cost
    self.sqft_low = self.USD_sqft_low * int(self.sqft) # gives the cost of the building in general
    self.sqft_high = self.USD_sqft_high * int(self.sqft)
    return (self.sqft_low, self.sqft_high)
  def mat_range(self, sqft_low, sqft_high):  
    mat_low = 0.41 * self.sqft_low #this is done to calculate the cost of just the materials of the building
    mat_high = 0.41 * self.sqft_high
    return (mat_low, mat_high)
  def lab_range(self, sqft_low, sqft_high):
    lab_low = 0.59 * self.sqft_low #this is done to calculate just the cost of labor
    lab_high = 0.59 * self.sqft_high
    return (lab_low, lab_high)  
  def CM_range(self, sqft_low, sqft_high):
    CM_low = 0.1 * self.sqft_low #this is done to calculate the contractor fees
    CM_high = 0.1 * self.sqft_high
    return (CM_low, CM_high)

print('')
print('What type of building would you like to construct?')

while (user_in == False): # using a while loop to make sure the user inputs a valid response
  build_type = str(input('Select [Residential, Commercial, Industrial]: ')) #allows for the user to picka type of building construction they are interested in
  #build_type = str(input(' What type of building would you like? Select: [Residential, Commercial, Industrial] ')) #allows for the user to picka type of building construction they are interested in
  if build_type == 'Residential':
    user_in = True
  if build_type == 'Commercial':
    user_in = True
  if build_type == 'Industrial':
    user_in = True
  elif (user_in == False):
    print('Please re-type your input...') #has the user redo the input until a valid input is typed

if build_type == 'Residential':  
  user_in2 = False
  while (user_in2 == False):
    print('')
    R1_2 = str(input('Is the project Multifamily or Single Dwelling: ')) #this helps to sepcify the buildning use which later on affects the cost per sqft
    if R1_2 == 'Multifamily':
      user_in2 =True
    elif R1_2 == 'Single Dwelling':
      user_in2 = True
    else:
      print('Please re-type your input...')
elif build_type == 'Commercial': #repeated for each type o input to allow options of all the build types
  user_in3 = False
  while (user_in3 == False):
    print('')
    R1_2 = str(input('Is the project a Restaurant, Retail, or Office Space: '))
    if R1_2 == 'Restaurant':
      user_in3 = True
    elif R1_2 == 'Retail':
      user_in3 = True
    elif R1_2 == 'Office Space':
      user_in3 = True
    else:
      print('Please re-type your input...')  
elif build_type == 'Industrial': #repeated for each type o input to allow options of all the build types
  user_in4 = False
  while (user_in4 == False):
    print('')
    R1_2 = str(input('Is the project Light Industry or Heavy Industry: '))
    if R1_2 == 'Light Industry':
      user_in4 = True
    elif R1_2 == 'Heavy Industry':
      user_in4 = True
    else:
      print('Please re-type your input...')

print('')
sqft = str(input('Approximate square feet of the building to be constructed: ')) #asked the size the user wants the building to be 
print('')
R3 = input('Level of finishes desired: [Basic, Standard, High-end] ')
print('')

if R1_2 == 'Single Dwelling': #residential option
  if R3 == 'Basic': #different level of finishes to accomadate for simple construction projects 
    USD_sqft_low = 330 #values for the cost per sqft are based on the sources listed at the end
    USD_sqft_high = 363
  elif R3 == 'Standard':
    USD_sqft_low = 363
    USD_sqft_high = 396
  elif R3 == 'High-end': #different level of finishes to accomadate for over the top, ridiculously expensive construction projects
    USD_sqft_low = 396
    USD_sqft_high = 1000000
elif R1_2 == 'Multifamily': #residential option
  if R3 == 'Basic':
    USD_sqft_low = 461
    USD_sqft_high = 660
  elif R3 == 'Standard':
    USD_sqft_low = 660
    USD_sqft_high = 859
  elif R3 == 'High-end': 
    USD_sqft_low = 859
    USD_sqft_high = 1000000
elif R1_2 == 'Restaurant': #commercial option
  if R3 == 'Basic':
    USD_sqft_low = 50
    USD_sqft_high = 270
  elif R3 == 'Standard':
    USD_sqft_low = 270
    USD_sqft_high = 330
  elif R3 == 'High-end':
    USD_sqft_low = 330
    USD_sqft_high = 1000000
elif R1_2 == 'Retail': #commercial option
  if R3 == 'Basic':
    USD_sqft_low = 384
    USD_sqft_high = 573
  elif R3 == 'Standard':
    USD_sqft_low = 573
    USD_sqft_high = 687
  elif R3 == 'High-end':
    USD_sqft_low = 687
    USD_sqft_high = 1000000
elif R1_2 == 'Office Space': #commercial option
  if R3 == 'Basic':
    USD_sqft_low = 373
    USD_sqft_high = 744
  elif R3 == 'Standard':
    USD_sqft_low = 744
    USD_sqft_high = 892
  elif R3 == 'High-end':
    USD_sqft_low = 892
    USD_sqft_high = 1000000
elif R1_2 == 'Light Industry': #industrial option
  if R3 == 'Basic':
    USD_sqft_low = 231
    USD_sqft_high = 323
  elif R3 == 'Standard':
    USD_sqft_low = 323
    USD_sqft_high = 341
  elif R3 == 'High-end':
    USD_sqft_low = 341
    USD_sqft_high = 1000000
elif R1_2 == 'Heavy Industry': #industrial option
  if R3 == 'Basic':
    USD_sqft_low = 359
    USD_sqft_high = 747
  elif R3 == 'Standard':
    USD_sqft_low = 747
    USD_sqft_high = 895
  elif R3 == 'High-end':
    USD_sqft_low = 895
    USD_sqft_high = 1000000
else:
  pass

user_YN = False
while (user_YN == False):
  timeline = str(input('Would you like to accelerate the timeline from 12 months to 9 months? [Yes or No]: '))
  print('')
  
  if timeline == 'Yes':
    user_YN = True
  if timeline == 'No':
    user_YN = True
  else:
    print('Please re-type your input...')

user_input = Cost(sqft, USD_sqft_low, USD_sqft_high) #stores ine inputs into the class listed at the beginning

cost_sqft_low = user_input.range_cost(sqft, USD_sqft_low, USD_sqft_high)[0] 
cost_sqft_high = user_input.range_cost(sqft, USD_sqft_low, USD_sqft_high)[1]

cost_mat_low = user_input.mat_range(sqft_low, sqft_high)[0] #first value listen in defintion is the low end of the range of cost
cost_mat_high = user_input.mat_range(sqft_low, sqft_high)[1] #first value listen in defintion is the high end of the range of cost
USD_mat_low = "${:,.2f}".format(cost_mat_low) #presents value of materials in USD
USD_mat_high = "${:,.2f}".format(cost_mat_high)

if timeline == 'No':
  cost_lab_low = user_input.lab_range(cost_sqft_low, cost_sqft_high)[0] # the 0 an 1 help to separate the low and high out of one definition rather than having two definitions
  cost_lab_high = user_input.lab_range(cost_sqft_low, cost_sqft_high)[1]
  USD_lab_low = "${:,.2f}".format(cost_lab_low) #presents value of labor in USD
  USD_lab_high = "${:,.2f}".format(cost_lab_high)
  project_time = '12 months'
elif timeline == 'Yes':
  cost_lab_low = (user_input.lab_range(cost_sqft_low, cost_sqft_high)[0]) + (0.25 * (user_input.lab_range(cost_sqft_low, cost_sqft_high)[0])) #adding on a percentage of labor for an acclerated timeline
  cost_lab_high = user_input.lab_range(cost_sqft_low, cost_sqft_high)[1] + (0.25 * (user_input.lab_range(cost_sqft_low, cost_sqft_high)[1])) #labor is the only value that changes since overtime needs to be accounted for 
  USD_lab_low = "${:,.2f}".format(cost_lab_low) #presents value of labor in USD
  USD_lab_high = "${:,.2f}".format(cost_lab_high)
  project_time = '9 months'
else:
  pass

cost_CM_low = user_input.CM_range(cost_sqft_low, cost_sqft_high)[0]
cost_CM_high = user_input.CM_range(cost_sqft_low, cost_sqft_high)[1]
USD_CM_low = "${:,.2f}".format(cost_CM_low) #presents contractor fees in USD
USD_CM_high = "${:,.2f}".format(cost_CM_high)

tot_low = cost_mat_low + cost_lab_low + cost_CM_low #total cost taking the sum of the materials, labor and CM fees
USD_tot_low = "${:,.2f}".format(tot_low) #total cost in USD
tot_high = cost_mat_high + cost_lab_high + cost_CM_high
USD_tot_high = "${:,.2f}".format(tot_high)


table = [['Range', 'Cost of Materials', 'Cost of Labor', 'Contractor Fees', 'Total Cost'], ['Low', USD_mat_low, USD_lab_low, USD_CM_low, USD_tot_low], ['High', USD_mat_high, USD_lab_high, USD_CM_high, USD_tot_high]] #formats resultes into a table

print(tabulate(table, headers='firstrow', tablefmt='fancy_grid')) #make the table look nice
print('')
print('Thank you {} for selecting S&K Estimating.'.format(user_name), '\n')
print('Your proposed {} {} project with {} finishes'.format(build_type, R1_2, R3))
print('will be approximately {} - {}, with a timeline of {}.'.format(USD_tot_low, USD_tot_high, project_time))


#Sources
#https://www.rsmeans.com/model-pages/restaurant
#https://ccorpinsights.com/costs-per-square-foot/





