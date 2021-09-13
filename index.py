name = "Asia"


if name == "Asia":
    print("Hey, Asia")
else:
    print("access denied")


#task 2
bank_balance = 1
if (bank_balance < 9.50) and (name == "Asia"):
    print("declined")
 # else:
 #    print("declined")


#task3
my_list = ["Asia", "Abdul", "ben", "john"]
print(len(my_list))
if name in my_list:
    print("access granted")

#task 4
allowed_names = ["Asia", "Felicia", "ben", "john"]
enter_name = input("Enter name: ")
if enter_name in allowed_names :
    print("access granted")
else:
    print("not in list")

# username_dictionary = {
#     "Chris": "password1",
#     "Anna": "password2"
# }
#
# entered_name = input("Enter name: ")
# entered_password = input("Enter password: ")
#
# if username_dictionary["Chris"] == entered_password:
#     print("Access Granted")