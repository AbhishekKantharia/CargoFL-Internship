import tkinter as tk
2 from tkinter import ttk, messagebox, filedialog
3 import os
4
5
6 def scary_action():
7 messagebox.showerror(title="Scary", message="Deleting hard disk. Please wait...")
8
9
10 def run_code():
11 text = ""
12 text += "Name: {}\n".format(name.get())
13 text += "Password: {}\n".format(password.get())
14 text += "Animal: {}\n".format(animal.get())
15 text += "Country: {}\n".format(country.get())
16 text += "Colors: "
17 for ix in range(len(colors)):
18 if colors[ix].get():
19 text += color_names[ix] + " "
20 text += "\n"
21
22 selected = list_box.curselection() # returns a tuple
23 text += "Animals: "
24 text += ', '.join([list_box.get(idx) for idx in selected])
25 text += "\n"
26
27 text += "Filename: {}\n".format(os.path.basename(filename_entry.get()))
28
29 resp = messagebox.askquestion(title="Running with", message=f"Shall I start runn\
30 ing with the following values?\n\n{text}")
31 if resp == 'yes':
32 output_window['state'] = 'normal' # allow editing of the Text widget
33 output_window.insert('end', f"{text}\n--------\n")
34 output_window['state'] = 'disabled' # disable editing
35 output_window.see('end') # scroll to the end as we make progress
GUI with Python/Tk 847
36 app.update()
37
38
39 def close_app():
40 app.destroy()
41
42
43 app = tk.Tk()
44 app.title('Simple App')
45
46 menubar = tk.Menu(app)
47 app.config(menu=menubar)
48
49 menu1 = tk.Menu(menubar, tearoff=0)
50 menubar.add_cascade(label="File", underline=0, menu=menu1)
51 menu1.add_separator()
52 menu1.add_command(label="Exit", underline=1, command=close_app)
53
54 top_frame = tk.Frame(app)
55 top_frame.pack(side="top")
56 pw_frame = tk.Frame(app)
57 pw_frame.pack(side="top")
58
59 # Simple Label widget:
60 name_title = tk.Label(top_frame, text=" Name:", width=10, anchor="w")
61 name_title.pack({"side": "left"})
62
63 # Simple Entry widget:
64 name = tk.Entry(top_frame)
65 name.pack({"side": "left"})
66 # name.insert(0, "Your name")
67
68 # Simple Label widget:
69 password_title = tk.Label(pw_frame, text=" Password:", width=10, anchor="w")
70 password_title.pack({"side": "left"})
71
72 # In order to hide the text as it is typed (e.g. for Passwords)
73 # set the "show" parameter:
74 password = tk.Entry(pw_frame)
75 password["show"] = "*"
76 password.pack({"side": "left"})
77
78 radios = tk.Frame(app)
GUI with Python/Tk 848
79 radios.pack()
80 animal = tk.StringVar()
81 animal.set("Red")
82 my_radio = []
83 animals = ["Cow", "Mouse", "Dog", "Car", "Snake"]
84 for animal_name in animals:
85 radio = tk.Radiobutton(radios, text=animal_name, variable=animal, value=animal_n\
86 ame)
87 radio.pack({"side": "left"})
88 my_radio.append(radio)
89
90
91 checkboxes = tk.Frame(app)
92 checkboxes.pack()
93 colors = []
94 my_checkbox = []
95 color_names = ["Red", "Blue", "Green"]
96 for color_name in color_names:
97 color_var = tk.BooleanVar()
98 colors.append(color_var)
99 checkbox = tk.Checkbutton(checkboxes, text=color_name, variable=color_var)
100 checkbox.pack({"side": "left"})
101 my_checkbox.append(checkbox)
102
103 countries = ["Japan", "Korea", "Vietnam", "China"]
104
105 def country_change(event):
106 pass
107 #selection = country.current()
108 #print(selection)
109 #print(countries[selection])
110
111 def country_clicked():
112 pass
113 #print(country.get())
114
115 country = ttk.Combobox(app, values=countries)
116 country.pack()
117 country.bind("<<ComboboxSelected>>", country_change)
118
119
120
121
GUI with Python/Tk 849
122 list_box = tk.Listbox(app, selectmode=tk.MULTIPLE, height=4)
123 animal_names = ['Snake', 'Mouse', 'Elephant', 'Dog', 'Cat', 'Zebra', 'Camel', 'Spide\
124 r']
125 for val in animal_names:
126 list_box.insert(tk.END, val)
127 list_box.pack()
128
129 def open_filename_selector():
130 file_path = filedialog.askopenfilename(filetypes=(("Any file", "*"),))
131 filename_entry.delete(0, tk.END)
132 filename_entry.insert(0, file_path)
133
134
135 filename_frame = tk.Frame(app)
136 filename_frame.pack()
137 filename_label = tk.Label(filename_frame, text="Filename:", width=10)
138 filename_label.pack({"side": "left"})
139 filename_entry = tk.Entry(filename_frame, width=60)
140 filename_entry.pack({"side": "left"})
141 filename_button = tk.Button(filename_frame, text="Select file", command=open_filenam\
142 e_selector)
143 filename_button.pack({"side": "left"})
144
145 output_frame = tk.Frame(app)
146 output_frame.pack()
147 output_window = tk.Text(output_frame, state='disabled')
148 output_window.pack()
149
150
151 buttons = tk.Frame(app)
152 buttons.pack()
153
154 scary_button = tk.Button(buttons, text="Don't click here!", fg="red", command=scary_\
155 action)
156 scary_button.pack({"side": "left"})
157
158 action_button = tk.Button(buttons, text="Run", command=run_code)
159 action_button.pack()
160
161 app.mainloop()
162
163 # TODO: key binding?
164 # TODO: Option Menu
GUI with Python/Tk 850
165 # TODO: Scale
166 # TODO: Progressbar (after the deleting hard disk pop-up)
167 # TODO: Frame (with border?)