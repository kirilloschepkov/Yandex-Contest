with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines() if line != '\n']
    clients = dict()
    for line in lines:
        words = line.split()
        if words[0] == 'DEPOSIT':
            clients[words[1]] = clients.get(words[1], 0) + int(words[2])
            continue
        if words[0] == 'WITHDRAW':
            clients[words[1]] = clients.get(words[1], 0) - int(words[2])
            continue
        if words[0] == 'BALANCE':
            if clients.get(words[1]) is None:
                print('ERROR')
                continue
            print(str(clients.get(words[1])))
            continue
        if words[0] == 'TRANSFER':
            clients[words[1]] = clients.get(words[1], 0) - int(words[3])
            clients[words[2]] = clients.get(words[2], 0) + int(words[3])
            continue
        if words[0] == 'INCOME':
            for person, money in clients.items():
                if money > 0: clients[person] += money * int(words[1]) // 100