import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create header frame
        header_frame = tk.Frame(self, bg="lightgrey", height=50)
        header_frame.pack(side="top", fill="x")

        # Create buttons in header frame
        book_btn = tk.Button(header_frame, text="Book Online", relief="flat", bg="white")
        book_btn.pack(side="right", padx=10)

        sign_in_btn = tk.Button(header_frame, text="Sign In", relief="flat", bg="white")
        sign_in_btn.pack(side="right", padx=10)

        location_btn = tk.Button(header_frame, text="Location", relief="flat", bg="white")
        location_btn.pack(side="right", padx=10)

        # Create scrollable canvas
        canvas = tk.Canvas(self)
        canvas.pack(side="left", fill="both", expand=True)

        # Create frame inside canvas
        frame = tk.Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Add buttons and labels to frame
        all_sports_btn = tk.Button(frame, text="All Sports",bg='white',bd=0)
        all_sports_btn.grid(row=0, column=0, padx=10, pady=10)

        all_sports_lbl = tk.Label(frame, text="View all sports")
        all_sports_lbl.grid(row=1, column=0)

        football_btn = tk.Button(frame, text="Football",bg='white',bd=0)
        football_btn.grid(row=0, column=1, padx=10, pady=10)

        football_lbl = tk.Label(frame, text="View football games")
        football_lbl.grid(row=1, column=1)

        cricket_btn = tk.Button(frame, text="Cricket",bg='white',bd=0)
        cricket_btn.grid(row=0, column=2, padx=10, pady=10)

        cricket_lbl = tk.Label(frame, text="View cricket games")
        cricket_lbl.grid(row=1, column=2)

        fitness_events_btn = tk.Button(frame, text="Fitness & Events",bg='white',bd=0)
        fitness_events_btn.grid(row=0, column=3, padx=10, pady=10)

        fitness_events_lbl = tk.Label(frame, text="View fitness events")
        fitness_events_lbl.grid(row=1, column=3)

        offers_btn = tk.Button(frame, text="Offers",bg='white',bd=0)
        offers_btn.grid(row=0, column=4, padx=10, pady=10)

        offers_lbl = tk.Label(frame, text="View special offers")
        offers_lbl.grid(row=1, column=4)

        # Add scrollbar to canvas
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.config(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        name_frame=tk.Frame(self,bg="grey",height=100,width=300)
        name_frame.place(x=25,y=200)
        name_frame.pack(side='left',fill='both')

        # Create footer frame
        footer_frame = tk.Frame(self, bg="lightgrey", height=50)
        footer_frame.pack(side="bottom", fill="x")

        # Add widgets to footer frame (optional)
        tk.Label(footer_frame, text="Copyright © 2023").pack()

        # Create search bar in 1st frame
        search_label = tk.Label(header_frame, text="Search:")
        search_label.pack(side="left", padx=10)

        search_entry = tk.Entry(header_frame)
        search_entry.pack(side="left", padx=10)

        search_btn = tk.Button(header_frame, text="Search", relief="flat", bg="white")
        search_btn.pack(side="left", padx=10)



if __name__ == "__main__":
    app = App()
    app.geometry('1408x792+50+0')
    app.resizable(0,0)
    app.mainloop()

