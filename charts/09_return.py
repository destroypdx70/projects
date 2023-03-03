def find_volume(length=1, width=1, depth=1):
  return length * width * depth, width, "Hi"

result, width, string = find_volume(width=23)


print(result)
print(width)
print(string)

def calculate_volume(length=20, widht=80, depth=120):
  return length * widht * depth, "widht =>", widht

result, string, widht = calculate_volume()
print(result)
print("widht =>", widht)







