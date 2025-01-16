if __name__ == "__main__":
    size = int(input())
    countries = set([input() for _ in range(size)])
    print(len(countries))