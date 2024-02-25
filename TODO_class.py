class ToDoList:
    def __init__(self):
        self.list = []
        self.status = 'TODO'

    def show(self):
        for x, task in enumerate(self.list, 1):
            print(f"{x}. {task['task']} - {task['status']}")

    def add_to(self):
        task = input("Podaj treść zadania: ")
        self.list.append(
            {
                "task": task,
                "status": self.status,
            }
        )
        return self.list

    def move(self):
        for x, task in enumerate(self.list):
            print(f"{x + 1}. {task['task']} - {task['status']}")

        idx = int(input("Podaj numer zadania: "))
        idx -= 1

        if not 0 <= idx < len(self.list):
            print("Nie ma takiego zadania.\n")
            return

        current_status = self.list[idx]["status"]
        if current_status == 'TODO':
            self.list[idx]["status"] = 'IN_PROGRES'
            self.status = 'IN_PROGRES'
        elif current_status == "IN_PROGRES":
            self.list[idx]["status"] = 'DONE'
            self.status = 'DONE'
        else:
            print("Nie można zmienić statusu zadania.")


first_try = ToDoList()


def main():
    while True:
        choice = input("Wybierz polecenie [show, add, move, exit]: ").lower()
        if choice == "show":
            first_try.show()
        elif choice == "add":
            first_try.add_to()
        elif choice == "move":
            first_try.move()
        elif choice == "exit":
            break


main()
