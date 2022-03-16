import random

def choice_command(command):
    data = command.split()
    choiced = random.choice(data[1:]) # [1:]でリストの１番目行こうを渡す
    response = f'「{choiced}」ガ選バラマシタ。'
    return response

def dice_command():
    num = random.randrange(1, 7)
    response = f'「{num}」ガ出マシタ。'
    return response
