def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line:
                id, name, age = line.split(',')
                cat_info = {
                    "id": id,
                    "name": name,
                    "age": age
                }
                cats_info.append(cat_info)

        return cats_info
    
    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


cats_info = get_cats_info("cats.txt")
print(cats_info)
