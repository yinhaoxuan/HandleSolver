# check if the word is still possible with the information from feedback
def agree(word_to_check, guessed_word, feedback):
    # if word_to_check[0] == '怨天尤人' and guessed_word[0] == '偷天换日':
    #     x = 0
    used = set()
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
            if word_to_check[1][i][2] != guessed_word[1][i][2]:
                return 0

        # wrong
        if feedback.c_list[i].zi == 0 or feedback.c_list[i].zi == 2:
            if word_to_check[0][i] == guessed_word[0][i]:
                return 0
            else:
                flag = 0
                for j in range(4):
                    if word_to_check[0][j] == guessed_word[0][i] and feedback.c_list[j].zi != 1 and (j, 'zi') not in used:
                        flag = 2
                        used.add((j, 'zi'))
                        break
                if flag != feedback.c_list[i].zi:
                    return 0

        if feedback.c_list[i].shengmu == 0 or feedback.c_list[i].shengmu == 2:
            if word_to_check[1][i][0] == guessed_word[1][i][0]:
                return 0
            else:
                flag = 0
                for j in range(4):
                    if word_to_check[1][j][0] == guessed_word[1][i][0] and feedback.c_list[j].shengmu != 1 and (
                    j, 'sm') not in used:
                        flag = 2
                        used.add((j, 'sm'))
                        break
                if flag != feedback.c_list[i].shengmu:
                    return 0

        if feedback.c_list[i].yunmu == 0 or feedback.c_list[i].yunmu == 2:
            if word_to_check[1][i][1] == guessed_word[1][i][1]:
                return 0
            else:
                flag = 0
                for j in range(4):
                    if word_to_check[1][j][1] == guessed_word[1][i][1] and feedback.c_list[j].yunmu != 1 and (j, 'ym') not in used:
                        flag = 2
                        used.add((j, 'ym'))
                        break
                if flag != feedback.c_list[i].yunmu:
                    return 0

        if feedback.c_list[i].yindiao == 0 or feedback.c_list[i].yindiao == 2:
            if word_to_check[1][i][2] == guessed_word[1][i][2]:
                return 0
            else:
                flag = 0
                for j in range(4):
                    if word_to_check[1][j][2] == guessed_word[1][i][2] and feedback.c_list[j].yindiao != 1 and (j, 'yd') not in used:
                        flag = 2
                        used.add((j, 'yd'))
                        break
                if flag != feedback.c_list[i].yindiao:
                    return 0

    return 1


def remove(l, feedback, word):
    l1 = []
    for w1 in l:
        if agree(w1, word, feedback):
            l1.append(w1)
    return l1
