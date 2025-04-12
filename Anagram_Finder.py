try :
    dictionary = {}
    with open("sample.txt","r") as file_txt:
        for words in file_txt:
            word = words.strip().lower()
            key = ''.join(sorted(word))
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(word)
    
    for valoare in dictionary.values():
        print(" ".join(valoare))
    
except FileNotFoundError:
    print("File `sample.txt` does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
    