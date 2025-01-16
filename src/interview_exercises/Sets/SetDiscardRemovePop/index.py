if __name__ == "__main__":
    size = int(input())
    set_1 = set(map(int, input().split()))
    size_commands = int(input())

    for _ in range(size_commands):
        command = input().split()
        if command[0] == "remove":
            element = int(command[1])
            if element in set_1:
                set_1.remove(element)
        elif command[0] == "discard":
            set_1.discard(int(command[1]))
        elif command[0] == "pop":
                set_1.pop()

    print(sum(set_1))
