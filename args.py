# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

normal = "I am a normal Argument and the students are:"

lst = ["Tayyab", "Sufi", "Skillf", "Sami",
       "Affan", "Khizer"]

kw = {"Skillf":"Monitor", "Sufi":"Fitness Instructor",
      "Khizer": "Coordinator", "Affan":"Cook"}

funargs(normal, *lst, **kw)
