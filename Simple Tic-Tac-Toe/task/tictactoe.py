def str_to_number_list_parse(numbers_list):
    return [int(i) for i in numbers_list]

def valid_number_checker(numbers_list):
    for i in numbers_list:
        if not i.replace('-', '').isdigit():
            return False
    return True

def coordinates_checker(numbers_list):
    for i in str_to_number_list_parse(numbers_list):
        if not i in [1,2,3]:
            return False
    return True

def coordinates_assigner(user_list, numbers_list):
    coordinates_list = [[1, 1],[1, 2],[1, 3],[2, 1],[2, 2],[2, 3],[3, 1],[3, 2],[3, 3]]
    for index, coordinates in enumerate(coordinates_list):
        numbers_list = str_to_number_list_parse(numbers_list)
        if numbers_list[0] == coordinates[0] and numbers_list[1] == coordinates[1]:
            if not user_list[index] in ["X", "O"]:
                return index+1
            return False

def toggle_user(user):
    return "O" if user == "X" else "X"

# write your code here
user_input = [i.replace("_", " ") for i in "_________"]
print("-" * 9)
print("| {} {} {} |".format(user_input[0],user_input[1],user_input[2]))
print("| {} {} {} |".format(user_input[3],user_input[4],user_input[5]))
print("| {} {} {} |".format(user_input[6],user_input[7],user_input[8]))
print("-" * 9)
# write your code here
lets_pay = True
user = "X"
while lets_pay:
    user_next_move = input().split()
    if not valid_number_checker(user_next_move):
        print("You should enter numbers!")
        continue
    elif not coordinates_checker(user_next_move):
        print("Coordinates should be from 1 to 3!")
        continue
    else:
        assigned_coordinate = coordinates_assigner(user_input, user_next_move)
        if not assigned_coordinate:
            print("This cell is occupied! Choose another one!")
            continue
        else:
            user_input[assigned_coordinate-1] = user
            print("-" * 9)
            print("| {} {} {} |".format(user_input[0],user_input[1],user_input[2]))
            print("| {} {} {} |".format(user_input[3],user_input[4],user_input[5]))
            print("| {} {} {} |".format(user_input[6],user_input[7],user_input[8]))
            print("-" * 9)
            sequence_list = [[0,1,2], [0,3,6], [6,7,8], [2,5,8], [0,4,8], [2,4,6], [1,4,7], [3,4,5]]
            x_wins = [True for s1, s2, s3 in sequence_list if user_input[s1] == user_input[s2] == user_input[s3] == "X"]
            o_wins = [True for s1, s2, s3 in sequence_list if user_input[s1] == user_input[s2] == user_input[s3] == "O"]
            if len(x_wins) > len(o_wins):
                print("X wins")
                lets_pay = False
            elif len(x_wins) < len(o_wins):
                print("O wins")
                lets_pay = False
            elif (len(x_wins) == 0) and (len(o_wins) == 0) and user_input.count(" ") == 0:
                print("Draw")
                lets_pay = False
            elif len(x_wins) == len(o_wins) != 0 and ((user_input.count("X") - user_input.count("O") in [1,0]) or (user_input.count("O") - user_input.count("X") in [1,0])):
                print("Impossible")
                lets_pay = False
            elif (len(x_wins) == 0) and (len(o_wins) == 0) and ((user_input.count("X") - user_input.count("O") >= 2) or (user_input.count("O") - user_input.count("X") >= 2)):
                print("Impossible")
                lets_pay = False
            else:
                user = toggle_user(user)
            # elif (len(x_wins) == 0) and (len(o_wins) == 0) and user_input.count("_") != 0:
            #     print("Game not finished")