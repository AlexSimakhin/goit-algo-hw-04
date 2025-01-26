"""taskBonus.py"""

def merge_k_lists(lists):
    if not lists:
        return []  # Якщо список порожній, повернути пустий список

    def merge_two_lists(list1, list2):
        merged = []
        i, j = 0, 0
        # Об'єднання двох списків
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        # Додавання залишків з першого списку
        while i < len(list1):
            merged.append(list1[i])
            i += 1
        # Додавання залишків з другого списку
        while j < len(list2):
            merged.append(list2[j])
            j += 1
        return merged

    # Об'єднуємо списки парами, поки не залишиться один список
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if i + 1 < len(lists) else []  # Обробка непарної кількості списків
            merged_lists.append(merge_two_lists(list1, list2))
        lists = merged_lists

    return lists[0]  # Повернути остаточний відсортований список

# Приклад використання
lists_data = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists_data)
print("Відсортований список:", merged_list)  # Очікуваний результат: [1, 1, 2, 3, 4, 4, 5, 6]
