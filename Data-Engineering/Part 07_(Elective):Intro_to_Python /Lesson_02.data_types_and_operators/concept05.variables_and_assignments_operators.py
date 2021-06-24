# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall -= (rainfall * 0.1)
# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume += (reservoir_volume * 0.05)
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume -= (reservoir_volume * 0.05)

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= (2.5e5)

# print the new value of the reservoir_volume variable
print(reservoir_volume)


#--------------------------------------------------------------------
#Juno's code
# The current volume of a water reservoir (in cubic metres)
#reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
#rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
#rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
#reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
#reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
#reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
#reservoir_volume -= 2.5e5 

# print the new value of the reservoir_volume variable
#print(reservoir_volume)
#---------------------------------------------------------------
"""
Quiz: Changing Variable Values
How does changing the value of a variable affect another variable that was defined in terms of it? Let's look at an example.

We're intentionally not providing a place to execute the code here, because we want to help you practice the important skill of walking through lines of code by hand.

Each line of code executes in order, one at a time, with control going from one line to the next.

>>> carrots = 24
>>> rabbits = 8
>>> crs_per_rab = carrots/rabbits
Now we add a new 4th line to this code, that assigns a new value to the rabbits variable:

>>> rabbits = 12

Variable Change


If we now add this new 5th line of code to the above, what will the output be?
```python

print(crs_per_rab) 
```Variable Change


If we now add this new 5th line of code to the above, what will the output be?
```python

print(crs_per_rab) 
```

SOLUTION:
3.0
"""
#----------------------------------------
"""
Here is a list of U.S. states in order of the date they entered the Union. Say you wanted to create a variable for Delaware and assign it a value to signify that it joined the Union first. Which of the following are valid variable names and assignments in Python?

 del = 1

 delaware = 1

 1 de = first

 de = 1



SOLUTION:

`delaware = 1`
`de = 1`

"""


