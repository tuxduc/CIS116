def reverse_text():
    while True:
        user_input = input("Enter a line of text (or 'Done', 'done', or 'd' to exit): ")
        if user_input in ["Done", "done", "d"]:
            break
        print(user_input[::-1])

reverse_text()