from data_structures.queue import Queue


def multi_bracket_validation(bracket_string):
    split_string = list(bracket_string)
    open = Queue()
    close = Queue()
    o_curley = 0
    o_brack = 0
    o_parenth = 0
    o_bracket = o_parenth + o_brack + o_curley

    c_curley = 0
    c_brack = 0
    c_parenth = 0
    c_bracket = c_parenth + c_brack + c_curley

    for character in split_string:
        if character == "{" or character == "[" or character == "(":
            open.enqueue(character)
        if character == "}" or character == "]" or character == ")":
            open.enqueue(character)

    while open.front:
        if open.front.value == "{" or open.front.value == "[" or open.front.value == "(":
            if open.front.value == "{":
                o_curley += 1
            if open.front.value == "[":
                o_brack += 1
            if open.front.value == "(":
                o_parenth += 1

            open.dequeue()

        elif open.front.value == "}" or open.front.value == "]" or open.front.value == ")":
            if open.front.value == "}":
                c_curley += 1
            if open.front.value == "]":
                c_brack += 1
            if open.front.value == ")":
                c_parenth += 1
            open.dequeue()

        o_bracket = o_parenth + o_brack + o_curley
        c_bracket = c_parenth + c_brack + c_curley

        if c_bracket > o_bracket:
            return False

    # if o_bracket == 0 and c_bracket == 0:
    #     return False
    if o_curley == c_curley and o_parenth == c_parenth and o_brack == c_brack:
        return True
    else:
        return False


if __name__ == "__main__":

    actual = multi_bracket_validation("][")
    print(actual)
