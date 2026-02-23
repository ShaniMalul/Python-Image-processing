import math

def degrees_to_radians(degrees):
    return degrees * math.pi / 180


degrees_values = [1, 5, 10, 30, 45, 180, 90, 0]

# הדפסת כותרת CSV
print("cos,sin,radians,degree")

for degree in degrees_values:
    radians = degrees_to_radians(degree)
    sin_val = math.sin(radians)
    cos_val = math.cos(radians)
    
    print(f"{cos_val},{sin_val},{radians},{degree}")