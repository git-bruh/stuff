import pyperclip


def string_split(string):
    max_len = int(input("Max Length: ")) + 1
    if len(string) <= max_len:
        print("Break")
        return
    new_str = ""
    while string != "":
        new_str += string[:max_len] + "/|"
        string = string[max_len:]
    str_list = new_str.split("/|")
    count = 0
    str_count = len(str_list)
    for string in str_list:
        count += 1
        input_ = input("Press ENTER to copy string {} of {}".format(
            count, str_count))
        if '' in input_:
            pyperclip.copy(string)
            print("Copied Successfully!")


if __name__ == "__main__":
    string_split(input("String: "))
