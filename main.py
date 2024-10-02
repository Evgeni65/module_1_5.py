# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
immutable_var = 1,2,'apple',True
print( immutable_var)
#immutable_var[0] = 4  в кортеже нельзя менять данные
#print( immutable_var) будет сообщение об ошибке
mutable_list = [3,4,5,'string',True]
print(mutable_list )
mutable_list[0] = 'coconut'
print(mutable_list )