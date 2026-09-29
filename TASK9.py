число = float(input("Введите число: "))

match число:
    case x if x > 0:
        print("положительное")
    case x if x < 0:
        print("отрицательное")
    case 0:
        print("ноль")