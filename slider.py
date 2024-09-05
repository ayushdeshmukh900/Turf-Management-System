import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create a canvas widget and a vertical scrollbar
        canvas = tk.Canvas(self, bg="white")
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas
        main_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=main_frame, anchor="nw")

        # Create the first frame
        frame1 = tk.Frame(main_frame, bg="white", padx=20, pady=20)
        frame1.pack(side="top", fill="x")

        # Create the search bar
        search_label = tk.Label(frame1, text="Search:")
        search_label.pack(side="left")
        search_entry = tk.Entry(frame1, bg="lightgrey", width=20)
        search_entry.pack(side="left")

        # Create the second frame
        frame2 = tk.Frame(main_frame, bg="white", padx=20, pady=20)
        frame2.pack(side="top", fill="both", expand=True)

        # Create a list of images to display
        image_list = ["cricket.jpg", "bg.jpg", "football.jpg", "facebook.jpg"]

        # Create a slider to slide through the images
        slider = tk.Scale(frame2, from_=0, to=len(image_list)-1, orient="horizontal", length=300)
        slider.pack(side="top")

        # Create a label to display the current image
        current_image = tk.Label(frame2, image="", bg="white")
        current_image.pack(side="top")

        def update_image(event):
            # Update the label with the current image
            index = int(slider.get())
            image_file = image_list[index]
            image = tk.PhotoImage(file="cricketballfor_logo.jpg")
            current_image.config(image=image)
            current_image.image = image

        slider.bind("<ButtonRelease-1>", update_image)
        slider.bind("<Motion>", update_image)

if __name__ == "__main__":
    app = App()
    app.mainloop()
