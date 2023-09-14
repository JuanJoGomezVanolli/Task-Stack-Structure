import customtkinter
import tkinterDnD

#customtkinter.set_ctk_parent_class(tkinterDnD.Tk)
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("CustomTkinter simple_example.py")

print(type(app), isinstance(app, tkinterDnD.Tk))


####################################
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
      new_element.next = self.head
      self.head = new_element

    def delete_first(self):
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted

    def returnFirstValue(self):
        return self.head

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()

    def getFirstValue(self):
        return self.ll.returnFirstValue()


def push_task():
    value1 = entry_1.get()
    if (value1):
        stack.push(Element(entry_1.get()))
        print(stack.getFirstValue().value)
        label_text.set(stack.getFirstValue().value)

    else :
        print("Error")

def pop_task():
    stack.pop()
    label_text.set(stack.getFirstValue().value)



####################################





frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

e1 = Element("No Tasks")

stack = Stack(e1)

label_text = customtkinter.StringVar()
label_text.set("No Tasks")

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT,textvariable=label_text,font=("Calibri",20))
label_1.pack(pady=50, padx=10)


btnColor = customtkinter.StringVar()

button_1 = customtkinter.CTkButton(master=frame_1, command=push_task,text="Push Task")
button_1.pack(pady=(40,20), padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, command=pop_task, text="Pop Task")
button_2.pack(pady=10, padx=10)


entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Task")
entry_1.pack(pady=10, padx=10)



app.mainloop()
