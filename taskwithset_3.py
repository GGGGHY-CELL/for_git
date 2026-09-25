original_list = input("Type list: ")

all_list = list(original_list.split())
print("Your list:", all_list)

unique_set = set(original_list.split())    
print(unique_set)

howmuch_dublicates = len(all_list) - len(unique_set)
print(howmuch_dublicates)
