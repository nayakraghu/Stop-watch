import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.attributes("-topmost", True)  # Keep the window always on top
        self.root.geometry("220x150")
        self.root.resizable(False, False)

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.time_label = tk.Label(self.root, text="00:00:00", font=("Helvetica", 24))
        self.time_label.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start, width=8)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop, width=8)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset, width=8)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.update_display()

    def update_display(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time))
        self.time_label.config(text=formatted_time)
        self.root.after(50, self.update_display)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()
