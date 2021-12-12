"""Problem 2.ipynb
Write a program in Python which prompts the user for their username in the format Domain
Name\Username as per Figure 1a below.

Original file is located at
  https://github.com/sangeeta196/Python_code_Problem"""

print("########################")
print(" WELCOME TO DBS CONSOLE ")
print("########################")
domain_username = (input('Please Provide Your Username: '))

# Create an empty lists for domain and username
domain_list=[]
user_name_list=[]

###Now usingg "string .append" method to append the required "domain_list" and the "user_name_list" in the console###

for a in domain_username:
    if(a.isalpha()):
        domain_list.append(a) 

    elif(a.isdigit()):
        user_name_list.append(a)
        
###Using "string .join" method() while running the value###
print("Domain: "+"".join(domain_list))
print("Username: "+"".join(user_name_list))