import hashlib
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Block:
    def __init__(self, patient_data, previous_hash):
        self.patient_data = json.dumps(patient_data, sort_keys=True)
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = self.patient_data + str(self.previous_hash)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_data = {"patient_id": "Genesis", "reco*rd": "First Block"}
        previous_hash = "0"
        self.chain.append(Block(genesis_data, previous_hash))

    def add_patient_record(self, patient_data):
        previous_block = self.chain[-1]
        previous_hash = previous_block.hash
        self.chain.append(Block(patient_data, previous_hash))

    def print_chain(self):
        for block in self.chain:
            print("Patient Data:", block.patient_data)
            print("Hash:", block.hash)
            print("Previous Hash:", block.previous_hash)
            print()

class BlockchainGUI:
    def __init__(self, root, blockchain):
        self.blockchain = blockchain

        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#ffffff")
        style.configure("TEntry", font=("Helvetica", 12), padding=5)
        style.configure("TButton", font=("Helvetica", 12), padding=6, borderwidth=0, highlightthickness=0)
        style.configure("Add.TButton", background="#4CAF50", foreground="white")
        style.configure("Show.TButton", background="#2196F3", foreground="white")
        style.map("TButton", background=[("active", "#45a049"), ("pressed", "#4CAF50")])

        root.title("Blockchain Healthcare System")
        root.geometry("1000x650")
        root.configure(bg="#f0f0f0")

        title_label = ttk.Label(root, text="Healthcare Management System", font=("Helvetica", 16), background="#ffffe0")
        title_label.pack(pady=20)

        input_frame = ttk.Frame(root, padding="20")
        input_frame.pack(pady=10, fill=tk.X)

        self.label_name = ttk.Label(input_frame, text="Full Name:")
        self.label_name.grid(row=0, column=0, sticky=tk.W)
        self.entry_name = ttk.Entry(input_frame, width=40)
        self.entry_name.grid(row=0, column=1, pady=5, sticky=tk.E)  # Center align the entry

        self.label_age = ttk.Label(input_frame, text="Age:")
        self.label_age.grid(row=1, column=0, sticky=tk.W)
        self.entry_age = ttk.Entry(input_frame, width=40)
        self.entry_age.grid(row=1, column=1, pady=5, sticky=tk.E)

        self.label_gender = ttk.Label(input_frame, text="Gender:")
        self.label_gender.grid(row=2, column=0, sticky=tk.W)
        self.entry_gender = ttk.Entry(input_frame, width=40)
        self.entry_gender.grid(row=2, column=1, pady=5, sticky=tk.E)

        self.label_phone = ttk.Label(input_frame, text="Phone Number:")
        self.label_phone.grid(row=3, column=0, sticky=tk.W)
        self.entry_phone = ttk.Entry(input_frame, width=40)
        self.entry_phone.grid(row=3, column=1, pady=5, sticky=tk.E)

        self.label_email = ttk.Label(input_frame, text="Email Address:")
        self.label_email.grid(row=4, column=0, sticky=tk.W)
        self.entry_email = ttk.Entry(input_frame, width=40)
        self.entry_email.grid(row=4, column=1, pady=5, sticky=tk.E)

        self.label_address = ttk.Label(input_frame, text="Address:")
        self.label_address.grid(row=5, column=0, sticky=tk.W)
        self.entry_address = ttk.Entry(input_frame, width=40)
        self.entry_address.grid(row=5, column=1, pady=5, sticky=tk.E)

        self.label_record = ttk.Label(input_frame, text="Medical Record:")
        self.label_record.grid(row=6, column=0, sticky=tk.W)
        self.entry_record = ttk.Entry(input_frame, width=40)
        self.entry_record.grid(row=6, column=1, pady=5, sticky=tk.E)

        self.add_button = ttk.Button(root, text="Add Record", command=self.add_record)
        self.add_button.pack(pady=10)

        self.show_button = ttk.Button(root, text="Show Blockchain", command=self.show_blockchain)
        self.show_button.pack(pady=10)

    def add_record(self):
        full_name = self.entry_name.get()
        age = self.entry_age.get()
        gender = self.entry_gender.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        record = self.entry_record.get()

        if full_name and age and gender and phone and email and address and record:
            patient_data = {
                "full_name": full_name,
                "age": age,
                "gender": gender,
                "phone": phone,
                "email": email,
                "address": address,
                "medical_record": record
            }
            self.blockchain.add_patient_record(patient_data)
            messagebox.showinfo("Success", "Record added to the blockchain!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_gender.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_record.delete(0, tk.END)

    def show_blockchain(self):
        blockchain_window = tk.Toplevel()
        blockchain_window.title("Blockchain Records")
        blockchain_window.geometry("500x500")

        text_box = tk.Text(blockchain_window, height=15, width=55, font=("Arial", 10))
        text_box.pack(pady=10)

        for block in self.blockchain.chain:
            text_box.insert(tk.END, f"Patient Data: {block.patient_data}\n")
            text_box.insert(tk.END, f"Hash: {block.hash}\n")
            text_box.insert(tk.END, f"Previous Hash: {block.previous_hash}\n")
            text_box.insert(tk.END, "-------------------------\n")
        text_box.config(state=tk.DISABLED)

if __name__ == "__main__":
    blockchain = Blockchain()
    root = tk.Tk()
    gui = BlockchainGUI(root, blockchain)
    root.mainloop()
