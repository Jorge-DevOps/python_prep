def delete_duplications(n):
    result=[]

    for i in range (len(n)):
        if not n[i] in result:
            result.append(n[i])

    return "".join(result)

if __name__ == "__main__":
    n = input("Ingrese una cadena")
    print(delete_duplications(n))
