"""Problem 3.ipynb###
Write a program in Python that prompts the user to enter a number of integer values. The 
program stores the integers, counts the frequency of each integer and displays the frequency 
as per Figure 2 below.###


Original file is located at
https://github.com/sangeeta196/Python_code_Problems"""

print("************************************************")
print("WELCOME TO THE DUBLIN BUSINESS SCHOOL CONSOLE")

print("************************************************")
num_elements = int(input("Enter number of elements: "))
print(num_elements)
print("Input " + str(num_elements) + " elements in the list: ")

###Now input an empty list (element)###

element_list = []
for x in range(num_elements):
  element_list.append(input('element - ' + str(x) + " : " ))

### Now creatING a dictionary in which each element value is considered as "key" and the frequency as the "value":"""

dict_elements={a:element_list.count(a) for a in element_list}

###printing the occurance as a "key value" pair in the following dictionary###

print("The frequency of all elements in the list : ")
for b in dict_elements:
    print(b+" occurs "+str(dict_elements[b])+" times")