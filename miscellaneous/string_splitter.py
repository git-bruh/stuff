import pyperclip


while True:
    character_limit = int(input("Character Limit : " ))
    input_text = str(input("Input : "))
    length = len(input_text)
    separator = ","
    if length > character_limit:
        print(f"Text is {length} characters long... Split ? (y/n)")
        choice = input("> ").lower()
        if "y" in choice:
            # Add separator after every character_limit characters
            new_string = ''
            while input_text != '':
                new_string += input_text[:character_limit] + '~'
                input_text = input_text[character_limit:]
            new_string = new_string[:-1]
            print(new_string)
            # Split String
            output = new_string.split("~")
            # variables = len(output)
            # print(variables)
            # user_variables = input("Type a, b, c ... according to the number above")
            # user_variables = output
            # print(user_variables)
            # input = input("Press [ENTER] to copy to clipboard")
            # if '' in input:
            #     pyperclip.copy()
        else:
            break
    elif length <= character_limit:
        print("There is nothing to do... Quitting")
        break
# og_str = "Every nth character should have a comma no more no less"
# n = 10
# new_str = ''
# while og_str != '':
#     new_str += og_str[:n] + ','
#     og_str = og_str[n:]
# print(new_str)