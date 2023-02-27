from tqdm import tqdm


def palindromic(n):
    str_n = str(n)
    for i in range(len(str_n) // 2):
        if str_n[i] != str_n[len(str_n) - i - 1]:
            return False
    return True


def main():
    res = {}
    max_n_2 = 30000
    max_n_3 = 2000

    for i in tqdm(range(2, max_n_2)):
        for j in range(2, max_n_3):
            key = i * i + j * j * j
            res[key] = res.get(key, 0) + 1
    ans = []
    for item in res:
        if res[item] == 4 and palindromic(item):
            print(item)
            ans.append(item)
    ans = sorted(ans)
    print(ans)
    print(sum(ans[:5]))


if __name__ == "__main__":
    main()
