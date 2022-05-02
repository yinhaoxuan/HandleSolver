# check if the word to check is still possible with the information from feedback
def agree(word_to_check, guessed_word, feedback):
    if word_to_check[0] == '临深履薄':
        x = 0
    for i in range(4):
        # right
        if feedback.c_list[i].zi == 1:
            if word_to_check[0][i] != guessed_word[0][i]:
                return 0
        if feedback.c_list[i].shengmu == 1:
            if word_to_check[1][i][0] != guessed_word[1][i][0]:
                return 0
        if feedback.c_list[i].yunmu == 1:
            if word_to_check[1][i][1] != guessed_word[1][i][1]:
                return 0
        if feedback.c_list[i].yindiao == 1:
            #print(word_to_check[0][i])
            #print(guessed_word[0][i])
            if word_to_check[1][i][2] != guessed_word[1][i][2]:
                return 0
        # wrong
        if feedback.c_list[i].zi == 0:
            # print(word_to_check[1][i][0])
            # print(guessed_word[1][i][0])
            if word_to_check[0][i] == guessed_word[0][i]:
                return 0
        if feedback.c_list[i].shengmu == 0:
            if word_to_check[1][i][0] == guessed_word[1][i][0]:
                return 0
        if feedback.c_list[i].yunmu == 0:
            if word_to_check[1][i][1] == guessed_word[1][i][1]:
                return 0
        if feedback.c_list[i].yindiao == 0:
            if word_to_check[1][i][2] == guessed_word[1][i][2]:
                return 0
        # occur
        if feedback.c_list[i].zi == 2:
            if word_to_check[0][i] == guessed_word[0][i]:
                return 0
            else:
                flag = 0
                for j in range(4):
                    if j != i:
                        if word_to_check[0][j] == guessed_word[0][i]:
                            flag = 1
                            break
                if flag == 0:
                    return 0

        if feedback.c_list[i].shengmu == 2:
            if word_to_check[1][i][0] == guessed_word[1][i][0]:
                return 0
            else:
                flag = 0
                for j in range(4):
                    if j != i:
                        if word_to_check[1][j][0] == guessed_word[1][i][0]:
                            flag = 1
                            break
                if flag == 0:
                    return 0

        if feedback.c_list[i].yunmu == 2:
            if word_to_check[1][i][1] == guessed_word[1][i][1]:
                return 0
            else:
                flag = 0
                for j in range(4):
                    if j != i:
                        if word_to_check[1][j][1] == guessed_word[1][i][1]:
                            flag = 1
                            break
                if flag == 0:
                    return 0

        if feedback.c_list[i].yindiao == 2:
            # print(word_to_check[1][i])
            # print(guessed_word[1][i])
            if word_to_check[1][i][2] == guessed_word[1][i][2]:
                return 0
            else:
                flag = 0
                for j in range(4):
                    if j != i:
                        #print(word_to_check[1][j])
                        if word_to_check[1][j][2] == guessed_word[1][i][2]:
                            flag = 1
                            break
                if flag == 0:
                    return 0

    return 1


def remove(l, feedback, word):
    l1 = []
    for w1 in l:
        if agree(w1, word, feedback):
            l1.append(w1)
    return l1
