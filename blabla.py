def diagonal_sums(a):
    chislo = 3
    main_sum = 0
    side_sum = 0
    for i in range(chislo):
        main_sum += a[i][i]         
        side_sum += a[i][chislo - 1 - i] 
    total = main_sum + side_sum
    return main_sum, side_sum, total

def rotate_90_clockwise(a):
    chislo = 3
    b = [[0] * chislo for _ in range(chislo)]
    for i in range(chislo):
        for j in range(chislo):
            b[j][chislo - 1 - i] = a[i][j]
    return b

print("Введіть 9 цілих чисел (по рядках)<3")
a = []
for _ in range(3):
    row = list(map(int, input().split()))
    while len(row) != 3:
        print("Ти не правильно робиш. 9 чисел по рядку. Спробуй ще раз)))")
        row = list(map(int, input().split()))
    a.append(row)

print("\nПочатковий масив:")
for row in a:
    print(*row)

m, s, t = diagonal_sums(a)
print(f"\nСума головної діагоналі = {m}")
print(f"Сума побічної діагоналі = {s}")
print(f"Разом (головна + побічна) = {t}")

rot = rotate_90_clockwise(a)
print("\nПісля повороту на 90° за годинниковою стрілкою:")
for row in rot:
    print(*row)