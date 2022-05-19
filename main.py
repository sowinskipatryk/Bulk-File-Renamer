import os
from tkinter import filedialog, messagebox, Tk, Label, Entry, Button

tk = Tk()

tk.title("Bulk File Renamer")
tk.geometry('222x250')

dir_path = ['']


def get_files_dir(path, button):
    path[0] = filedialog.askdirectory()
    if path[0]:
        button.destroy()
        button = Button(tk, text="Change directory", command=lambda:
                        get_files_dir(dir_path, button))
        button.grid(row=1, padx=(50, 0), pady=(12, 0))


def rename_files(path, filename=""):
    i = 1

    if path[0]:
        for file in os.listdir(path[0]):
            old_filename = os.path.splitext(file)
            file_extension = old_filename[1]
            new_filename = f'{filename}{i}{file_extension}'
            old_filepath = path[0] + '/' + file
            new_filepath = path[0] + '/' + new_filename

            os.rename(old_filepath, new_filepath)
            i += 1
        messagebox.showinfo('Process completed!',
                            'Files have been renamed successfully!')
    else:
        messagebox.showerror("Error - No directory selected!",
                             "Choose the directory of files to be renamed!")


dir_path_label = Label(tk, text="Enter files path:")
dir_path_label.grid(row=0, pady=(12,0))

dir_path_button = Button(tk, text="Select directory",
                         command=lambda: get_files_dir(dir_path,
                                                       dir_path_button))
dir_path_button.grid(row=1, padx=(50,0), pady=(12,0))

file_name_label = Label(tk, text="Enter new filename:")
file_name_label.grid(row=2, padx=(20,0), pady=(35,0))

file_name_entry = Entry(tk)
file_name_entry.grid(row=3, padx=(50,0), pady=(12,0))

rename_files_button = Button(tk, text="Rename files", command=lambda:
                             rename_files(dir_path, file_name_entry.get()))
rename_files_button.grid(row=4, padx=(50,0), pady=(30,0))

tk.mainloop()
