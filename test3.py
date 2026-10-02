def gog(**kwargs):   # посмотреть поподробнее 
    for key, value in kwargs.items():
        print(f"{key}: {value}")

gog(name="Иван", age=25, city="Москва")
