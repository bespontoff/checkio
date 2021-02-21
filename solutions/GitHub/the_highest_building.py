#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run the-highest-building

# The main architect of the city wants to build a new highest building.
# You have to help him find the current highest building in the city.
# 
# 
# 
# Input:Heights of the buildings as a 2D-array.
# 
# Output:The number of the highest building and height of it as a list of integers (Important: in this task the building numbers starts from "1", not from "0")
# 
# Precondition:
# array width<= 10
# array height<= 10
# There is only 1 highest building in each array
# 
# 
# END_DESC

def highest_building(buildings):
    for floor in buildings:
        if 1 in floor: # 1 means roof
            return [floor.index(1)+1, len(buildings)-buildings.index(floor)]