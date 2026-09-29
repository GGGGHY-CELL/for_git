speedwagon = input("Введите команду (старт, стоп, пауза): ")

match speedwagon:
    case "start":
        print("Starting process...")
    case "stop":
        print("Process stoped")
    case "pause":
        print("Process paused")
    case _:
        print("BEEP Unknown command")