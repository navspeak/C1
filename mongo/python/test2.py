name = str(input("Name: " ).strip())
age = int(input("Age: " ).strip())

# Taking additional attributes as key=value pairs
kwargs_input = input("Extra attribs in for key1=val1 key2=val2: ").strip()
kwargs = {}

# Parse the key=value pairs
if kwargs_input:
    for item in kwargs_input.split():
        if '=' in item:
            key, value = item.split('=', 1)
            kwargs[key] = value

def build_user_profile(name, age, **kwargs):
    # ret = {"name": name, "age": age}
    # ret.update(kwargs)
    # return ret
    # return {"name": name, "age": age, **kwargs}
    return {"name": name, "age": age} | kwargs

print(build_user_profile(name, age, **kwargs))

def f(a,/,b,*,c):
    return a +b+c

print(f(1,2,c=3))

a = 5
b = 0

def safe_divide(a, b):
    # Write your code here
    try:
       return a/b
    except ZeroDivisionError:
        return "Error: division by zero"
    finally:
        return "Operation attempted"



# Print the output
print(safe_divide(a, b))

def filtered_zip(a, b):
    # Correct Syntax: [ (element to keep) for (loop) if (condition) ]
    return [(x, y) for x, y in zip(a, b) if x is not None and y is not None]

# Example Usage:
list_a = [10, 20, None, 40]
list_b = ["A", None, "C", "D"]

result = filtered_zip(list_a, list_b)
print(result) 
# Output: [(10, 'A'), (40, 'D')]