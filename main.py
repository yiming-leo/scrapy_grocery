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

str_jp = "内田元太"
str_cn = "内田元太"
for i in range(len(str_jp)):
    print(f"{str_jp[i].encode('utf-8')} {str_jp[i]}")
for i in range(len(str_jp)):
    print(f"{str_cn[i].encode('utf-8')} {str_cn[i]}")
