
mount = len(tmp) // 2
for j in range(mount):
    if tmp[j] == tmp[len(tmp) - j]:
        continue
    else:
        print("0")
        break
    print("1")
