from tkinter import *


def center(root, fw, fh):

    """
    :param root: the root or Toplevel to center
    :param fw: the frame width you want
    :param fh: the frame height you want
    :return: None
    """
    root.update_idletasks()     # Updates the dimensions of the screen

    frame_width = fw   # width of the frame on which our content will be(the grey space)
    frame_height = fh  # height of the frame

    # frame_width = root.winfo_width()
    # frame_height = root.winfo_height()

    side_width = root.winfo_rootx() - root.winfo_x()   # Width of each outer sides of window
    window_width = frame_width + 2 * side_width         # The complete width of the window + left side

    titlebar_height = root.winfo_rooty() - root.winfo_y()
    window_height = frame_height + titlebar_height + frame_width    # the complete height of the window + upper side

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (window_width/2)
    y = (screen_height/2) - (window_height/2)

    root.geometry('%dx%d+%d+%d' % (frame_width, frame_height, x, y))


root = Tk()
root.title("TwitterBot 2.0")

# bg_img = PhotoImage(file="img\\login_bg.png")
# bg_label = Label(root, image=bg_img)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

root.configure(background='#5CAEFF')
center(root, 620, 369)

root.mainloop()
