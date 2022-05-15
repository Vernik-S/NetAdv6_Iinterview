def brackets_balanced(string):
    stack = []
    brackets_pairs = {'(': ')', '[': ']', '{': '}'}  # ключи - открывающие скобки, значения - закрывающие
    #if string == "": return True

    for char in string:
        if char in brackets_pairs:
            stack.append(char)  # в стеке храняться только открывающие скобки
        elif not stack or char != brackets_pairs[stack[-1]]:
            # если попалась закрываюшая скобка и на верху стека не её пара то ошибка балансровки
            # если стек пуст(закончились открывающие скобки) но есть закрываюшая, то несбалансировано
            return False
        else:
            stack.pop()
            # если удовлетворены предыдущие условия, то значит текущая пара скобок сбалансирована и отработана

    return not stack  # если стек к концу string непуст, то скобки несбалансированы. Недостаточно закрывающих скобок


if __name__ == "__main__":
    str1 = "(((([{}]))))"
    str2 = "{{[(])]}}"
    print(brackets_balanced(str1))
    print(brackets_balanced(str2))
    print(brackets_balanced(""))
