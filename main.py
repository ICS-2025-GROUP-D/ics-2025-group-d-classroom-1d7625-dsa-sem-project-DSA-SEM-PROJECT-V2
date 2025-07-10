import tkinter as tk
from pymongo import MongoClient
from tkinter import ttk
from tkinter import messagebox  # Ensure this is imported



"""
    1.
    Set up the main window
    Specify the title
    Specify the size (Feel free to change)
"""
main_window = tk.Tk()
main_window.title("DSA CAT 2")
main_window.geometry("700x500")

"""
    2.
    Set up all the UI components for the main window:
    Table, Buttons, NoteBook, NoteBook Tabs
    .grid() to place the items in the main window
"""
# Table
data_table = ttk.Treeview(main_window, columns=("title", "description"), show="headings")

# Table headings
data_table.heading(column="title", text="Title")
data_table.heading(column="description", text="Description")

# Table headings size
data_table.column(column="title", width=250)
data_table.column(column="description", width=325)

# Buttons
all_notes_button = ttk.Button(main_window, text="Read All Notes")
select_notes_button = ttk.Button(main_window, text="Show Selected Note")
add_to_revision_queue_button = ttk.Button(main_window, text="Add to Revision Queue")
add_to_revision_stack_button = ttk.Button(main_window, text="Add to Revision Stack")
start_revision_queue_button = ttk.Button(main_window, text="Start Revision Queue")
start_revision_stack_button = ttk.Button(main_window, text="Start Revision Stack")

# Notebook
main_notebook = ttk.Notebook()

# Notebook tabs
manipulate_notebook_tab = tk.Frame(main_notebook)
revision_queue_notebook_tab = tk.Frame(main_notebook)
revision_stack_notebook_tab = tk.Frame(main_notebook)
all_notes_notebook_tab = tk.Frame(main_notebook)
frequent_paths_tab = tk.Frame(main_notebook)

# Add the tabs to Notebook
main_notebook.add(manipulate_notebook_tab, text="Data Operations")
main_notebook.add(revision_queue_notebook_tab, text="Revision Queue")
main_notebook.add(revision_stack_notebook_tab, text="Revision Stack")
main_notebook.add(all_notes_notebook_tab, text="All Notes")
main_notebook.add(frequent_paths_tab, text="Frequent Paths")

"""
    3.
    Place the components on the main window
"""
data_table.grid(column=0, row=0, columnspan=15)
all_notes_button.grid(column=1, row=1, columnspan=4)
select_notes_button.grid(column=1, row=2, columnspan=4)
add_to_revision_queue_button.grid(column=6, row=1, columnspan=4)
add_to_revision_stack_button.grid(column=11, row=1, columnspan=4)
start_revision_queue_button.grid(column=6, row=2, columnspan=4)
start_revision_stack_button.grid(column=11, row=2, columnspan=4)
main_notebook.grid(column=0, row=3, columnspan=15)

""""
    4.
    Place the Same text and label components on all notebook tabs except frequent tab
    Align them in the same position on each tab
"""
# Labels
title_label_manipulate_notebook_tab = ttk.Label(manipulate_notebook_tab, text="Title")
title_label_revision_queue_notebook_tab = ttk.Label(revision_queue_notebook_tab, text="Title")
title_label_revision_stack_notebook_tab = ttk.Label(revision_stack_notebook_tab, text="Title")
title_label_all_notes_notebook = ttk.Label(all_notes_notebook_tab, text="Title")
description_label_manipulate_notebook_tab = ttk.Label(manipulate_notebook_tab, text="Description")
description_label_revision_queue_notebook_tab = ttk.Label(revision_queue_notebook_tab, text="Description")
description_label_revision_stack_notebook_tab = ttk.Label(revision_stack_notebook_tab, text="Description")
description_label_all_notes_notebook = ttk.Label(all_notes_notebook_tab, text="Description")

# Text Areas
title_text_area_manipulate_notebook_tab = tk.Text(manipulate_notebook_tab, height=1)
title_text_area_revision_queue_notebook_tab = tk.Text(revision_queue_notebook_tab, height=1)
title_text_area_revision_stack_notebook_tab = tk.Text(revision_stack_notebook_tab, height=1)
title_text_area_all_notes_notebook = tk.Text(all_notes_notebook_tab, height=1)
description_text_area_manipulate_notebook_tab = tk.Text(manipulate_notebook_tab, height=4)
description_text_area_revision_queue_notebook_tab = tk.Text(revision_queue_notebook_tab, height=4)
description_text_area_revision_stack_notebook_tab = tk.Text(revision_stack_notebook_tab, height=4)
description_text_area_all_notes_notebook = tk.Text(all_notes_notebook_tab, height=4)
graph_text_area_frequent_paths_tab = tk.Text(frequent_paths_tab, height=4)

# Text Area for the last data structure ... tbd
def update_graph_display():
    graph_text_area_frequent_paths_tab.delete("1.0","end")
    graph_text_area_frequent_paths_tab.insert("1.0",note_graph.get_adjacency_list())

# Align
title_label_manipulate_notebook_tab.grid(column=0, row=1, columnspan=15)
title_label_revision_queue_notebook_tab.grid(column=0, row=1, columnspan=15)
title_label_revision_stack_notebook_tab.grid(column=0, row=1, columnspan=15)
title_label_all_notes_notebook.grid(column=0, row=1, columnspan=15)
description_label_manipulate_notebook_tab.grid(column=0, row=3, columnspan=15)
description_label_revision_queue_notebook_tab.grid(column=0, row=3, columnspan=15)
description_label_revision_stack_notebook_tab.grid(column=0, row=3, columnspan=15)
description_label_all_notes_notebook.grid(column=0, row=3, columnspan=15)
title_text_area_manipulate_notebook_tab.grid(column=0, row=2, columnspan=15)
title_text_area_revision_queue_notebook_tab.grid(column=0, row=2, columnspan=15)
title_text_area_revision_stack_notebook_tab.grid(column=0, row=2, columnspan=15)
title_text_area_all_notes_notebook.grid(column=0, row=2, columnspan=15)
description_text_area_manipulate_notebook_tab.grid(column=0, row=4, columnspan=15)
description_text_area_revision_queue_notebook_tab.grid(column=0, row=4, columnspan=15)
description_text_area_revision_stack_notebook_tab.grid(column=0, row=4, columnspan=15)
description_text_area_all_notes_notebook.grid(column=0, row=4, columnspan=15)
graph_text_area_frequent_paths_tab.grid(column=0, row=0, columnspan=15)

"""
    5.
    Buttons for different tabs 
"""
# Buttons for manipulating database
add_notes_button = ttk.Button(manipulate_notebook_tab, text="Add Note")
delete_notes_button = ttk.Button(manipulate_notebook_tab, text="Delete Note")

# Align buttons for manipulating database
add_notes_button.grid(column=1, row=5)
delete_notes_button.grid(column=0, row=5)

# Buttons for moving forward in data structures
next_note_button_all_notes_notebook_tab = ttk.Button(all_notes_notebook_tab, text="Next Note")
next_note_button_revision_stack_notebook_tab = ttk.Button(revision_stack_notebook_tab, text="Next Note")
next_note_button_revision_queue_notebook_tab = ttk.Button(revision_queue_notebook_tab, text="Next Note")

# Align buttons for moving forward
next_note_button_all_notes_notebook_tab.grid(column=0, row=5)
next_note_button_revision_stack_notebook_tab.grid(column=0, row=5)
next_note_button_revision_queue_notebook_tab.grid(column=0, row=5)

"""
    6. Connect to the mongo db database
    -  Create the client connection
    -  Get the right database
    -  Get the right collection
"""
client = MongoClient("mongodb://localhost:27017")
database = client["db_mongodb_notes"]
collection = database["notes"]

"""
    7. Add all documents to the data table
    -   Find all documents
    -   For each document place it at a new row at the end of the table
"""


def clear_table():
    # Method to delete data in table
    for row in data_table.get_children():
        data_table.delete(row)



def refresh_table():
    clear_table()
    all_documents = collection.find()
    for doc in all_documents:
        title = doc.get("title", "No Title Found")
        content = doc.get("content", "No Content Found")
        data_table.insert("", tk.END, values=(title, content))



# Method call to refresh the table as a first instance
refresh_table()

"""
    8. Method for getting text
"""


def get_text(data_field):
    content = data_field.get("1.0", "end-1c")
    return content


"""
    9. Get text and send to database ***Dictionary***
    -  Will implement the dictionary data structure
    -  Dictionary sets up the mongo db document
    -  Document is sent to collection
    -  Clear text areas
    -  Refresh table to show all collections
"""


def add_note():
    new_doc = {
        "title": get_text(title_text_area_manipulate_notebook_tab),
        "content": get_text(description_text_area_manipulate_notebook_tab)
    }
    collection.insert_one(new_doc)

    title_text_area_manipulate_notebook_tab.delete("1.0", "end")
    description_text_area_manipulate_notebook_tab.delete("1.0", "end")
    refresh_table()



# Set up the button to add data
add_notes_button.config(command=add_note)

"""
    10. Delete selected item from database
    - Get the title and the content from the viewable portion
    - Delete the data that matches
    - Clear text areas (From first character to the last) 
    - Refresh the table to show all collections
"""


def del_note():
    collection.delete_one({
        "title": get_text(title_text_area_manipulate_notebook_tab),
        "content": get_text(description_text_area_manipulate_notebook_tab)
    })

    title_text_area_manipulate_notebook_tab.delete("1.0", "end")
    description_text_area_manipulate_notebook_tab.delete("1.0", "end")
    refresh_table()



# Set up the button to delete data
delete_notes_button.config(command=del_note)

"""
    11. Set up the table to get data into the fields on the manipulate database tab upon selection
    - Clear anything if there
    - Select the new content
    - Add the new content
"""


def show_selected():
    global last_selected_note_title # start defining the function when a note is selected from the table
    title_text_area_manipulate_notebook_tab.delete("1.0", "end")
    description_text_area_manipulate_notebook_tab.delete("1.0", "end")
    # This returns an item_id
    selected_items = data_table.selection()

    for item_id in selected_items:
        # This gets the data stored under the found item_id:
        # values[0]-> first column 1, values[1] -> second column....
        values = data_table.item(item_id, "values")

        # Place the data in attributes
        title = values[0]
        description = values[1]
        title_text_area_manipulate_notebook_tab.insert("1.0", title)
        description_text_area_manipulate_notebook_tab.insert("1.0", description)

        #graph update: mark this as the last selected node
        note_graph.add_node(title)
        last_selected_note_title=title

        update_graph_display()


# Tell the button to carry out the specified function
select_notes_button.config(command=show_selected)

"""
    12. Set up the All notes tab functionality -> ***Linked List***
    - Set up the full linked list class: (Suggestion: singly linked for ease of coding and troubleshooting)
            - Have a method to add data to the linked list
            - Have a method to move forward in the linked list
    - Set up the linked list to have all the notes from the database
    - Set the next button **(next_note_button_all_notes_notebook_tab)** to allow forward traversal of the linked list
    - Should you need them:
            - The title text area is **()**
            - The description text area is **()**        

                ****Test to see all that you have done works👍You are the sole person responsible for this tab👍****

    - Additional: * Can have a button to make it go back to the first note
                  * If using a doubly linked list, can also add a button to go to the previous note
                  * Any other functionality you deem fit
"""

### **** Member implementing 12, code goes here **** ###

# 1. Linked List Node
class Node:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.next = None

# 2. Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def append(self, title, content):
        new_node = Node(title, content)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def reset(self):
        self.current = self.head

    def next(self):
        if self.current is None:
            return None
        data = (self.current.title, self.current.content)
        self.current = self.current.next
        return data

# 3. Create an instance of the Linked List
all_notes_linked_list = LinkedList()

#4. Load data from MongoDB into the linked list
def load_notes_into_linked_list():
    # Clear and repopulate the list
    all_notes_linked_list.__init__()
    all_documents = collection.find()
    for doc in all_documents:
        title = doc.get("title", "No Title Found")
        content = doc.get("content", "No Content Found")
        all_notes_linked_list.append(title, content)
    all_notes_linked_list.reset()
    show_next_note() # Show the first note

#5. Show the next note
def show_next_note():
    note = all_notes_linked_list.next()
    title_text_area_all_notes_notebook.delete("1.0", "end")
    description_text_area_all_notes_notebook.delete("1.0", "end")
    if note:
        title, description = note
        title_text_area_all_notes_notebook.insert("1.0", title)
        description_text_area_all_notes_notebook.insert("1.0", description)
    else: # To loop back to the start automatically
        all_notes_linked_list.reset()
        show_next_note()

#6. Restart the first note explicitly
def restart_notes():
    all_notes_linked_list.reset()
    show_next_note()

#7. Button set up
next_note_button_all_notes_notebook_tab.config(command=show_next_note)

#8. Restart button on the 'All Notes' tab
restart_notes_button_all_notes_notebook_tab = ttk.Button(all_notes_notebook_tab, text="Restart Notes")
restart_notes_button_all_notes_notebook_tab.grid(column=1, row=5)
restart_notes_button_all_notes_notebook_tab.config(command=restart_notes)

#9. Load notes when the app starts
load_notes_into_linked_list()

#10. Make the load notes occur anytime a note is added or deleted
def add_notes_button_functionality():
    add_note() # adds to the DB
    load_notes_into_linked_list() # reloads Linked List from the DB

add_notes_button.config(command=add_notes_button_functionality)


def del_notes_button_functionality():
    del_note() # deletes from the DB
    load_notes_into_linked_list()

delete_notes_button.config(command=del_notes_button_functionality)



"""
    13. Set up revision stack tab functionality -> ***Stack***
    - Set up the stack class: (Suggestion: use the array or python list implementation to save time)
            - Have a method to push to the stack
            - Have a method to pop from the stack
    - Set up the button **(add_to_revision_stack_button)** to add data to the stack
    - Set up the button **(start_revision_stack_button)** to pop of the first value and place in the revision stack tab
    - Should you need them: 
            - The title text area is **(title_text_area_revision_stack_notebook_tab)**
            - The description text area is **(description_text_area_revision_stack_notebook_tab)**
    - Set up the next button **(next_note_button_revision_stack_notebook_tab)** to keep popping off the next value(and showing it) in the revision stack tab
            - Have a way of showing the stack is now empty (Suggested: any further presses will show none)

            ****Test to see all that you have done works👍You are the sole person responsible for this tab👍****

    -Additional: * Any other functionality you deem fit
"""


#### **** Member implementing 13, code goes here  **** ###

# 1. Stack Data Structure
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, note):
        self.stack.append(note)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


# 2. Create the stack instance
revision_stack = Stack()


# 3. Add note to stack when button is clicked
def add_to_stack():
    print("add_to_stack() was called")  # Add this line at the top
    global last_selected_note_title 
    title = get_text(title_text_area_revision_stack_notebook_tab)
    description = get_text(description_text_area_revision_stack_notebook_tab)

    if title.strip() == "" and description.strip() == "":
        return  # Do not add empty notes

    # Push the note dictionary onto the stack
    revision_stack.push({"Title": title, "Content": description})

    note_graph.add_node(title)
    if last_selected_note_title:
        note_graph.add_edge(last_selected_note_title, title)

    update_graph_display()
    # Clear the text areas after adding
    title_text_area_revision_stack_notebook_tab.delete("1.0", "end")
    description_text_area_revision_stack_notebook_tab.delete("1.0", "end")
    messagebox.showinfo("Added", "Note added to revision stack and saved.")

add_to_revision_stack_button.config(command=add_to_stack)
  
# 4. Start revision: pop a note and display it
def start_revision():
    note = revision_stack.pop()
    if note:
        title_text_area_revision_stack_notebook_tab.delete("1.0", "end")
        description_text_area_revision_stack_notebook_tab.delete("1.0", "end")
        title_text_area_revision_stack_notebook_tab.insert("1.0", note["Title"])
        description_text_area_revision_stack_notebook_tab.insert("1.0", note["Content"])
    else:
        # If empty, show "No more notes"
        title_text_area_revision_stack_notebook_tab.delete("1.0", "end")
        description_text_area_revision_stack_notebook_tab.delete("1.0", "end")
        title_text_area_revision_stack_notebook_tab.insert("1.0", "No more notes")
        description_text_area_revision_stack_notebook_tab.insert("1.0", "")


# 5. Bind the buttons
add_to_revision_stack_button.config(command=add_to_stack)
start_revision_stack_button.config(command=start_revision)
next_note_button_revision_stack_notebook_tab.config(command=start_revision)

#### **** Member implementing 13, code goes here  **** ###

"""
    14. Set up revision queue tab functionality -> ***Queue***
    - Set up the queue class: (Suggestion: use the array or python list implementation to save time)
            - Have a method to enqueue
            - Have a method to dequeue
    - Set up the button **(add_to_revision_queue_button)** to add data to the queue
    - Set up the button **(start_revision_queue_button)** to dequeue the first value and place in the revision queue tab
    - Should you need them:
            - The title text area is **(title_text_area_revision_queue_notebook_tab)**
            - The description text area is **(description_text_area_revision_queue_notebook_tab)**
    - Set up the button **()** to keep on the dequeue process(and showing the value) in the revision queue tab
            - Have a way of showing the queue is now empty (Suggested: any further presses will show none)

            ****Test to see all that you have done works👍You are the sole person responsible for this tab👍****

    - Additional: * Any other functionality you deem fit        

# """
#Queue implementation#
class RevisionQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, note):
        self.queue.append(note)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

# ---- Step 2: Queue Instance ----
revision_queue = RevisionQueue()

# ---- Step 3: Button Functions ----

def add_to_revision_queue():
    print("add_to_revision_queue was called")

    global last_selected_note_title

    title = title_text_area_revision_queue_notebook_tab.get("1.0", tk.END).strip()
    content = description_text_area_revision_queue_notebook_tab.get("1.0", tk.END).strip()

    if not last_selected_note_title:
        messagebox.showwarning("No Selection", "Please select a note first.")
        return
    
    if title and content:
        note = {"title": title, "content": content}
        revision_queue.enqueue(note)
        collection.insert_one(note)  # Save to MongoDB
       
        #graph logic
        note_graph.add_node(title)
        note_graph.add_edge(last_selected_note_title,title)
        
        print("last selecte note:",last_selected_note_title)
        update_graph_display()

        messagebox.showinfo("Added", "Note added to revision queue and saved.")
        title_text_area_revision_queue_notebook_tab.delete("1.0", tk.END)
        description_text_area_revision_queue_notebook_tab.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Missing Info", "Please fill in both title and description.")
add_to_revision_queue_button.config(command=add_to_revision_queue)

def start_revision_queue():
    if revision_queue.is_empty():
        title_text_area_revision_queue_notebook_tab.delete("1.0", tk.END)
        description_text_area_revision_queue_notebook_tab.delete("1.0", tk.END)
        messagebox.showinfo("Done", "Revision queue is empty.")
    else:
        note = revision_queue.dequeue()
        title_text_area_revision_queue_notebook_tab.delete("1.0", tk.END)
        description_text_area_revision_queue_notebook_tab.delete("1.0", tk.END)
        title_text_area_revision_queue_notebook_tab.insert(tk.END, note["title"])
        description_text_area_revision_queue_notebook_tab.insert(tk.END, note["description"])

def keep_dequeuing_notes():
    if revision_queue.is_empty():
        title_text_area_revision_queue_notebook_tab.delete("1.0", tk.END)
        description_text_area_revision_queue_notebook_tab.delete("1.0", tk.END)
        messagebox.showinfo("Queue Empty", "All notes revised.")
        return 
    else:
        note = revision_queue.dequeue()
        title_text_area_revision_queue_notebook_tab.delete("1.0", tk.END)
        description_text_area_revision_queue_notebook_tab.delete("1.0", tk.END)
        title_text_area_revision_queue_notebook_tab.insert(tk.END, note["title"])
        description_text_area_revision_queue_notebook_tab.insert(tk.END, note["description"])
        title_text_area_revision_queue_notebook_tab.after(3000, keep_dequeuing_notes)

# ---- Step 4: Buttons for Queue Tab ----
# not required because button are already defined at the top

# add_to_revision_queue_button = tk.Button(
#     main_window, text="Add to Revision Queue", command=add_to_revision_queue, name="add_to_revision_queue_button"
# )
# add_to_revision_queue_button.pack(pady=5)

# start_revision_queue_button = tk.Button(
#     main_window, text="Start Revision Queue", command=start_revision_queue, name="start_revision_queue_button"
# )
# start_revision_queue_button.pack(pady=5)

# keep_revision_queue_button = tk.Button(
#     main_window, text="Keep Revising (Auto)", command=keep_dequeuing_notes
# )
# keep_revision_queue_button.pack(pady=5)

#### **** Member implementing 14, code goes here  **** ###

"""
    15. Set up the frequent tab functionality -> ***Graph***
    - Set up the graph: (Suggestion: Use the add node and the add edge functionality discussed in class)
            - Have a method to add nodes
            - Have a method to add edges

    - You are free to set up the functions to be called at any point you deem fit:
            - Suggestion: Alter the command attribute of the select_notes button
                                                             add_to_revision_queue button
                                                             add_to_revision_stack button
             to also add nodes and edges in addition to what they already do.
    - Print the adjacency list or the adjacency matrix used to set up the graph in the text area **(graph_text_area_frequent_paths_tab)**

        ****Test to see all that you have done works👍Make sure it does not collide with work from anyone at the top👍****

    - Additional: * Any other functionality you deem fit
"""
#graph data struture
class Graph:
    def __init__(self):
        self.adjacency = {} #key: node title, value: list of connected titles
    
    # adds a new note(node) to the graph
    def add_node(self,title):
        if title not in self.adjacency:
            self.adjacency[title]=[]

    # create a connection (edge) btwn two notes
    def add_edge(self, title1, title2):
        self.add_node(title1)
        self.add_node(title2)
        if title2 not in self.adjacency[title1]:
            self.adjacency[title1].append(title2)

    #generates a printable string of the graphs connections
    def get_adjacency_list(self):
        result=""
        for node,neighbors in self.adjacency.items():
            result += f"{node} → {', '.join(neighbors)}\n"
        return result

# create a graph instance and tracker
note_graph = Graph()
last_selected_note_title= None # tracks note to create edges 

#### **** Member implementing 15, code goes here  **** ###

"""
    16. Final app tester
    - Test the app to make sure everything works
    - Generate the readme.md file specified in the project guidelines
    - Generate a user guide
    - Generate the final report (Keep it as simple as possible, other group members will contribute where necessary)

            ****You will not write code other than to the README.md👍 IF you find any error, ask for the person responsible to resolve it👍****
"""

if __name__ == "__main__":
    # Run the main function body
    main_window.mainloop()