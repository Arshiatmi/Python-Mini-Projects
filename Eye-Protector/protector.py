
from tkinter import *
import time

WORK_MINUTES = 20
REST_SECONDS = 20

while True:
    time.sleep(WORK_MINUTES * 60)

    start_time = time.time()

    win = Tk()

    current_time = StringVar(
        win, str(int((start_time + REST_SECONDS) - time.time())))

    win.title("You Need To Rest !")
    win.geometry("700x200")
    win.attributes('-fullscreen', True)
    win.configure(background='black')
    win_label = Label(win, text=f"You Need To Rest {REST_SECONDS} Seconds !", font=(
        'Helvetica', 25), fg="white", bg="black").pack(pady=40)
    time_label = Label(win, textvariable=current_time, font=(
        'Helvetica', 25), fg="white", bg="black").pack(pady=60)

    def update_text():
        current_time.set(str(int((start_time + REST_SECONDS) - time.time())))
        if int((start_time + REST_SECONDS) - time.time()) >= 0:
            win.after(1000, update_text)
        else:
            win.quit()
            win.destroy()

    update_text()

    def do_nothing():
        pass

    win.protocol("WM_DELETE_WINDOW", do_nothing)

    mainloop()
