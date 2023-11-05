import json
import datetime


def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)


def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    return notes


def add_note():
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "text": text,
        "created": now,
        "updated": now,
    }
    notes.append(note)
    save_notes(notes)

    print("Заметка успешно сохранена.")


def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    title = input("Введите новый заголовок заметки: ")
    text = input("Введите новый текст заметки: ")

    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["text"] = text
            note["updated"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    else:
        print("Заметка с указанным ID не найдена.")
        return

    save_notes(notes)
    print("Заметка успешно отредактирована.")


def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))

    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            break
    else:
        print("Заметка с указанным ID не найдена.")
        return

    save_notes(notes)
    print("Заметка успешно удалена.")


def filter_by_date():
    date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Некорректный формат даты.")
        return

    notes = load_notes()
    filtered_notes = [note for note in notes if note["created"].split()[0] == date_str]

    print("Заметки, созданные на указанную дату:")
    for note in filtered_notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['text']}")
        print(f"Дата создания: {note['created']}")
        print(f"Дата последнего изменения: {note['updated']}")
        print("--------------")


def main():
    while True:
        command = input("Введите команду (add, edit, delete, filter, exit): ")

        if command == "add":
            add_note()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "filter":
            filter_by_date()
        elif command == "exit":
            break
        else:
            print("Некорректная команда.")


if __name__ == "__main__":
    main()