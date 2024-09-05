import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

def On_enter(event):
    if searchEntry.get()=='Enter First name & Last name':
        searchEntry.delete(0,END)

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

        # Create footer frame
        footer_frame = tk.Frame(self, bg="lightgrey", height=50)
        footer_frame.pack(side="bottom", fill="x")

        # Add widgets to footer frame
        tk.Label(footer_frame, text="Copyright © 2023").pack()

        # Create main frame
        main_frame = tk.Frame(self, bg="black")
        main_frame.pack(side="left", fill="both", expand=True)

        # Create canvas
        canvas = tk.Canvas(main_frame, bg="white")
        canvas.pack(side="left", fill="both", expand=True)



        # Create inner frame for widgets
        inner_frame = tk.Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        # # Create first frame
        # frame1 = tk.Frame(inner_frame, bg="white")
        # frame1.pack(side="top",fill='both',expand= True)
        #
        # all_sports_btn = tk.Button(frame1, text="All Sports", bg="white", relief="flat")
        # # all_sports_btn.place(x=0,y=500)
        # all_sports_btn.pack(side="left",padx=250,pady=100)
        #
        # # all_sports_lbl = tk.Label(frame1, text="View all sports")
        # # all_sports_lbl.grid(row=1, column=0)
        #
        # football_btn = tk.Button(frame1, text="Football", bg="white", relief="flat")
        # football_btn.pack(side="left",padx=20)
        #
        # # football_lbl = tk.Label(frame1, text="View football games")
        # # football_lbl.grid(row=1, column=1)
        #
        # cricket_btn = tk.Button(frame1, text="Cricket", bg="white", relief="flat")
        # cricket_btn.pack(side="left",padx=30)
        #
        # # cricket_lbl = tk.Label(frame1, text="View cricket games")
        # # cricket_lbl.grid(row=1, column=2)
        #
        # fitness_events_btn = tk.Button(frame1, text="Fitness & Events", bg="white", relief="flat")
        # fitness_events_btn.pack(side="left", padx=10)
        #
        # # fitness_events_lbl = tk.Label(frame1, text="View fitness events")
        # # fitness_events_lbl.grid(row=1, column=3)
        #
        # offers_btn = tk.Button(frame1, text="Offers", bg="white", relief="flat")
        # offers_btn.pack(side="left", padx=80)
        #
        # # offers_lbl = tk.Label(frame1, text="View special offers")
        # # offers_lbl.grid(row=1, column=4)
        #
        # # Create search bar in 1st frame
        # search_label = tk.Label(header_frame, text="Search:")
        # search_label.pack(side="left", padx=10)
        #
        # search_entry = tk.Entry(header_frame)
        # search_entry.pack(side="left", padx=10)
        #
        # search_btn = tk.Button(header_frame, text="Search", relief="flat", bg="white")
        # search_btn.pack(side="left", padx=10)
        #
        # '''# Create second frame
        # frame2 = tk.Frame(inner_frame, bg="white")
        # frame2.pack(side="top", pady=10)
        #
        # search_label = tk.Label(frame2, text="Search", bg="white")
        # search_label.pack(side="left", padx=10)
        #
        # search_entry = tk.Entry(frame2, bg="white")
        # search_entry.pack(side="left", padx=10)'''
        #
        # frame3 = tk.Frame(inner_frame, bg="white")
        # frame3.pack(side="top",fill='both')
        #
        # offers_lbl = tk.Label(frame3, text="View special offers")
        # offers_lbl.grid(padx=0,pady=0)




if __name__ == "__main__":

    app = App()
    app.geometry('1408x792+50+0')
    app.resizable(0,0)

    # Add scrollbar to canvas
    scrollbar = Scrollbar(app)
    scrollbar.pack(side="right", fill="y")

    all_sports_btn = Button(app, text="All Sports",font=('Microsoft Yahei UI Light',13,'bold') ,bg="white", relief="flat")
    all_sports_btn.place(x=190,y=120)

    football_btn = Button(app, text="Football",font=('Microsoft Yahei UI Light',13,'bold'), bg="white", relief="flat")
    football_btn.place(x=410, y=120)

    cricket_btn = Button(app, text="Cricket",font=('Microsoft Yahei UI Light',13,'bold'), bg="white", relief="flat")
    cricket_btn.place(x=630, y=120)

    fit_btn = Button(app, text="Fitness and event",font=('Microsoft Yahei UI Light',13,'bold'), bg="white", relief="flat")
    fit_btn.place(x=830, y=120)

    offer_btn = Button(app, text="Offer",font=('Microsoft Yahei UI Light',13,'bold'), bg="white", relief="flat")
    offer_btn.place(x=1110, y=120)

    all_sports_lbl = Label(app, text="View all sports",bg='white')
    all_sports_lbl.place(x=198,y=170)

    football_lbl = Label(app, text="View football games",bg='white')
    football_lbl.place(x=410,y=170)

    cricket_lbl = Label(app, text="View cricket games",bg='white')
    cricket_lbl.place(x=630,y=170)

    fitness_events_lbl = Label(app, text="View fitness events",bg='white')
    fitness_events_lbl.place(x=860,y=170)

    offers_lbl = Label(app, text="View special offers",bg='white')
    offers_lbl.place(x=1110,y=170)

    cricket_logo = PhotoImage(file='cricketball_for_logo.png')
    clLabel = Label(app, image=cricket_logo, cursor='hand2')
    clLabel.place(x=600, y=140)

    football_logo = PhotoImage(file='football_image_for_logo.png')
    flLabel = Label(app, image=football_logo, cursor='hand2')
    flLabel.place(x=380, y=140)

    fitness_logo = PhotoImage(file='callendar_for_logo.png')
    ftlLabel = Label(app, image=fitness_logo, cursor='hand2')
    ftlLabel.place(x=800, y=140)

    search_label = tk.Label(app, text="Search:")
    search_label.place(x=300,y=260)

    searchEntry = Entry(app, width=30, font=('Microsoft Yahei UI Light', 12), bg='darkslategray',
                          fg='light cyan', bd=2)
    searchEntry.place(x=990, y=300)
    searchEntry.insert(0, 'Enter First name & Last name')

    searchEntry.bind('<FocusIn>', On_enter)
    search_btn = tk.Button(app, text="Search", relief="flat", bg="white")
    search_btn.place(x=400,y=260)

    football_logo = PhotoImage(file='football_image_for_logo.png')
    flLabel = Label(app, image=football_logo, cursor='hand2')
    flLabel.place(x=380, y=940)

    app.mainloop()
