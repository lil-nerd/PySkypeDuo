import tkinter as tk

def save_png(master, image):

    entry_window = tk.Tk()
    entry_window.title("Save image")
    entry_window.geometry("400x400")
    name_entry = tk.Entry(entry_window)
    name_entry.grid(row = 0, column = 0)

    def snapshot_entry():
        name = name_entry.get()
        name = 'Shots/' + name + '.png'
        image.save(name)
#        entry_window.quit()
        entry_window.destroy()

    enter_button = tk.Button(entry_window, text = "Save .png", command = snapshot_entry)
    enter_button.grid(row = 1, column = 1)
    entry_window.mainloop()
