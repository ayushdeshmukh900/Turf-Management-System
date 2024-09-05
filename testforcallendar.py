import tkinter as tk
import random
class Calendar(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calendar")
        self.grid(sticky="WENS")
        self.weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        self.timeslots = ["7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM",
                          "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM",
                          "7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM"]
        self.selected_slot = None
        self.create_widgets()

    def create_widgets(self):
        for i, weekday in enumerate(self.weekdays):
            label = tk.Label(self, text=weekday, width=10, font=("Arial", 12))
            label.grid(row=0, column=i+1, sticky="WENS")
        for i, timeslot in enumerate(self.timeslots):
            label = tk.Label(self, text=timeslot, width=10, font=("Arial", 12))
            label.grid(row=i+1, column=0, sticky="WENS")
            for j, weekday in enumerate(self.weekdays):
                button = tk.Button(self, bg="white", width=10, height=2)
                button.grid(row=i+1, column=j+1, sticky="WENS")
                button.bind("<Button-1>", lambda event, i=i, j=j: self.select_slot(event, i, j))
                button.bind("<Double-Button-1>", lambda event, i=i, j=j: self.select_slot(event, i, j, True))

    def select_slot(self, event, i, j, is_double=False):
        if self.selected_slot and not is_double:
            self.selected_slot.configure(bg="white")
        self.selected_slot = self.grid_slaves(row=i+1, column=j+1)[0]
        if is_double:
            self.selected_slot.configure(bg="red")
            self.parent.destroy()  # Proceed to next page
        else:
            self.selected_slot.configure(bg="orange")

    def create_widgets(self):
        for i, weekday in enumerate(self.weekdays):
            label = tk.Label(self, text=weekday, width=10, font=("Arial", 12))
            label.grid(row=0, column=i + 1, sticky="WENS")
        for i, timeslot in enumerate(self.timeslots):
            label = tk.Label(self, text=timeslot, width=10, font=("Arial", 12))
            label.grid(row=i + 1, column=0, sticky="WENS")
            for j, weekday in enumerate(self.weekdays):
                button = tk.Button(self, bg="white", width=10, height=2, fg="white", font=("Arial", 12))
                button.grid(row=i + 1, column=j + 1, sticky="WENS")
                button.bind("<Button-1>", lambda event, i=i, j=j: self.select_slot(event, i, j))
                button.bind("<Double-Button-1>", lambda event, i=i, j=j: self.select_slot(event, i, j, True))
                button.configure(text=str(random.choice([1000, 1500])))


if __name__ == '__main__':
    root = tk.Tk()
    app = Calendar(root)
    app.mainloop()
