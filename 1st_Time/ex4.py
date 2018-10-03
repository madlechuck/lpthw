# These lines defines the variables:

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#These next few lines will print text:

#This particular lines tells how many cars are available.
print "There are", cars, "cars available."
#This line tells how many drivers are available.
print "There are only", drivers, "drivers available."
#This line tells how many cars aren't driven today.
print "There will be", cars_not_driven, "empty cars today."
#This line tells how many people can be carpooled today.
print "We can transport", carpool_capacity, "people today."
#This line tells how many passengers needs to carpool today.
print "We have", passengers, " passengers to carpool today."
#This line tells the average of passengers per car.
print "We need to put about", average_passengers_per_car, "passengers in each car." 