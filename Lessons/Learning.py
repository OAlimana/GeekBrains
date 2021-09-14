sec = int(input("Введите время в секундах: "))
hours = sec // 3600
minutes = (sec % 3600) // 60
seconds = (sec % 3600) % 60
print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")
