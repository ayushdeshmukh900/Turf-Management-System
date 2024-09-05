import tkinter as tk


class App(tk.Tk):
    def _init_(self):
        super()._init_()

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

        # Create footer frame
        footer_frame = tk.Frame(self, bg="lightgrey", height=50)
        footer_frame.pack(side="bottom", fill="x")

        # Add widgets to footer frame
        tk.Label(footer_frame, text="Copyright © 2023").pack()

        # Create button frame
        button_frame = tk.Frame(self, bg="white", height=50)
        button_frame.pack(side="top", fill="x")

        # Create buttons in button frame
        all_sports_btn = tk.Button(button_frame, text="All Sports", relief="flat", bg="white")
        all_sports_btn.pack(side="left", padx=10)

        football_btn = tk.Button(button_frame, text="Football", relief="flat", bg="white")
        football_btn.pack(side="left", padx=10)

        cricket_btn = tk.Button(button_frame, text="Cricket", relief="flat", bg="white")
        cricket_btn.pack(side="left", padx=10)

        fitness_btn = tk.Button(button_frame, text="Fitness & Events", relief="flat", bg="white")
        fitness_btn.pack(side="left", padx=10)

        offers_btn = tk.Button(button_frame, text="Offers", relief="flat", bg="white")
        offers_btn.pack(side="left", padx=10)

        # Create descriptions for buttons
        all_sports_desc = tk.Label(button_frame, text="All sports activities")
        all_sports_desc.pack(side="left", padx=10)

        football_desc = tk.Label(button_frame, text="Football activities")
        football_desc.pack(side="left", padx=10)

        cricket_desc = tk.Label(button_frame, text="Cricket activities")
        cricket_desc.pack(side="left", padx=10)

        fitness_desc = tk.Label(button_frame, text="Fitness and events")
        fitness_desc.pack(side="left", padx=10)

        offers_desc = tk.Label(button_frame, text="Special offers")
        offers_desc.pack(side="left", padx=10)


if __name__ == "_main_":
    app = App()
    app.mainloop()
