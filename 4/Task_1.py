
# Вычислить число π c заданной точностью d

# π = 2√3*(1 - (1/3)*(1/3) + (1/5)*(1/3)^2 -
# (1/7)*(1/3)^3… + 1/((2n + 1)*(-3)^n)…)

def count_pi(d):
    result = 0
    for i in range(d):
        result += 2 * 3**0.5 * (1/((2*i+1)*(-3)**i))
    return result


user_d = int(input("Введите точность d для вычесления числа ПИ "))
pi = count_pi(user_d)
print(pi)

