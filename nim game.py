from functools import reduce

print("Enter stacks seperated by space.")
print("Example: 1 3 5 7")
print("Solves the game with above input.\n")

while True:
    stack = input("Enter stacks: ").split()
    if not stack:
        print('Finished!')
        break
    int_stack = list(map(lambda x:int(x), stack))
    nim_sum = reduce(lambda x,y: x^y, int_stack)
    if not nim_sum:
        print("You are the loser probably if your rival works well!")
    min_stack = list(map(lambda x:x^nim_sum if x-(x^nim_sum) >= 0 else 100000, int_stack))
    min_value = min(min_stack)
    min_index = min_stack.index(min_value)
    to_drop_items = (int_stack[min_index] - min_value) or 1
    print(f"Remove {to_drop_items} item(s) from stack {min_index+1}")