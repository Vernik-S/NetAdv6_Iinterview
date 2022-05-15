from random import randint
from MyStack import MyStack

from bracket_balance import brackets_balanced

from Messenger import GmailMessenger


# 1. Необходимо реализовать класс Stack со следующими методами
stack = MyStack()

print(stack.IsEmpty())

print(stack.pop())

for i in range(10):
    stack.push(randint(1, 10))

print(stack)

print(stack.IsEmpty())

print(stack.peek())

print(stack.pop())

print(stack.peek())

print(stack.size())


# 2.  Решить задачу на проверку сбалансированности скобок
print('*'*20)
brackets_to_test = [
    "(((([{}]))))",
    "[([])((([[[]]])))]{()}",
    "{{[()]}}",
    "}{}",
    "{{[(])]}}",
    "[[{())}]"
    ]

print(list(map(brackets_balanced, brackets_to_test)))

#3* рефакторинг кода (необязательное задание)
print('*'*20)
login_t = 'login@gmail.com'
password_t = 'qwerty'
messenger = GmailMessenger(login_t, password_t)
print(messenger)