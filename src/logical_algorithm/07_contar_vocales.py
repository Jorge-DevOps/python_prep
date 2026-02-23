def get_vocals(n):
    vocals = ["A","E","I","O","U", "Á", "É", "Í", "Ó", "Ú","a","e","i","o","u", "á", "é", "í", "ó", "ú"]
    count = 0
    for i in range(len(n)):
            if n[i] in vocals:
                count += 1
    return count


if __name__ == "__main__":
    n = input("Ingrese una palabra: ")
    print(get_vocals(n))
