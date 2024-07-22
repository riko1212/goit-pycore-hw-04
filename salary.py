def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        total = 0
        count = 0

        for line in lines:
            name, salary = line.strip().split(',')
            total += int(salary)
            count += 1

        if count == 0:
            return (0, 0)
        
        average = total / count
        return (total, average)
    
    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
        return (0, 0)
    except ValueError:
        print("Error: One or more lines in the file are not formatted correctly.")
        return (0, 0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return (0, 0)


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


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
