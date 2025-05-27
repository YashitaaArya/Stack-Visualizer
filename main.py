import tkinter as tk

class StackVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack Visualizer")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        self.stack = []
        self.max_stack_size = 8 
        self.box_height = 40
        self.box_width = 200

        self.setup_ui()

        self.root.bind("<Return>", lambda event: self.push())
        self.root.bind("<space>", lambda event: self.push())

    def setup_ui(self):
        title = tk.Label(self.root, text="STACK VISUALIZER", font=("Helvetica", 20, "bold"))
        title.pack(pady=10)

        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)

        self.entry_label = tk.Label(entry_frame, text="Enter a value:")
        self.entry_label.pack(side=tk.LEFT)

        self.entry = tk.Entry(entry_frame, font=("Helvetica", 14), width=15)
        self.entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="PUSH", background="red", width=10, command=self.push).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="POP", background="blue", width=10, command=self.pop).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="PEEK", background="yellow", width=10, command=self.peek).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="CLEAR", background="green", width=10, command=self.clear_stack).grid(row=0, column=4, padx=5)

        self.message_label = tk.Label(self.root, text="", font=("Helvetica", 12), fg="blue")
        self.message_label.pack(pady=5)

        self.canvas_height = 350
        self.canvas = tk.Canvas(self.root, width=300, height=self.canvas_height, bg="white", bd=2, relief=tk.SUNKEN)
        self.canvas.pack(pady=10)

        self.draw_stack()

    def draw_stack(self):
        self.canvas.delete("all")
        x0 = 50
        y_bottom = self.canvas_height
        x1 = x0 + self.box_width
        y_top = y_bottom - self.max_stack_size * (self.box_height + 5)

        # Draw stack container (open at the top)
        self.canvas.create_rectangle(x0, y_top, x1, y_bottom, outline="black")

        for index, value in enumerate(self.stack):
            y1 = y_bottom - index * (self.box_height + 5)
            y0 = y1 - self.box_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="skyblue", outline="black")
            self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=str(value), font=("Helvetica", 14))

    def push(self):
        value = self.entry.get().strip()
        if not value:
            self.message_label.config(text="Please enter a value to push.", fg="red")
            return
        if len(self.stack) >= self.max_stack_size:
            self.message_label.config(text="Stack Overflow! Max size reached.", fg="red")
            return
        self.stack.append(value)
        self.entry.delete(0, tk.END)
        self.message_label.config(text=f"Pushed '{value}' to stack.", fg="green")
        self.draw_stack()

    def pop(self):
        if not self.stack:
            self.message_label.config(text="Stack Underflow! Nothing to pop.", fg="red")
            return
        popped = self.stack.pop()
        self.message_label.config(text=f"Popped '{popped}' from stack.", fg="orange")
        self.draw_stack()

    def peek(self):
        if not self.stack:
            self.message_label.config(text="Stack is empty. Nothing to peek.", fg="red")
            return
        top = self.stack[-1]
        self.message_label.config(text=f"Top of stack: '{top}'", fg="blue")

    def clear_stack(self):
        self.stack.clear()
        self.message_label.config(text="Stack cleared.", fg="black")
        self.draw_stack()

if __name__ == "__main__":
    root = tk.Tk()
    app = StackVisualizer(root)
    root.mainloop()
