import hashlib
import time
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
import string

# ---------- Authentication ----------
USERNAME = ""          # Change this to your own
PASSWORD = ""     # Change this to your own

# ---------- Mining Engine ----------
class MinerEngine:
    def __init__(self, log_callback, stats_callback):
        self.log = log_callback
        self.update_stats = stats_callback
        self.mining = False
        self.hashrate = 0
        self.shares = 0
        self.blocks = 0
        self.difficulty = 4  # adjustable

    def mine(self):
        self.mining = True
        self.log("Miner started. Connecting to local pool...")
        self.log(f"Difficulty: {self.difficulty} leading zeros")
        prefix = '0' * self.difficulty
        nonce = 0
        hashes_this_second = 0
        last_time = time.time()

        while self.mining:
            # Simulate a real job: a block header would be a mix of data
            job = f"block-{self.blocks}-{random.randint(0, 1_000_000_000)}"
            text = f"{job}{nonce}".encode()
            h = hashlib.sha256(text).hexdigest()

            hashes_this_second += 1

            # Update hashrate every second
            if time.time() - last_time >= 1:
                self.hashrate = hashes_this_second
                self.update_stats(self.hashrate, self.shares, self.blocks)
                hashes_this_second = 0
                last_time = time.time()

            if h.startswith(prefix):
                self.shares += 1
                self.log(f"Share found! Nonce: {nonce}, Hash: {h[:16]}...")
                # Occasionally find a "block" (simulate lower difficulty block)
                if h.startswith('0' * (self.difficulty + 2)):
                    self.blocks += 1
                    self.log(f"### BLOCK MINED! ### Total blocks: {self.blocks}")
                    # Increase difficulty slightly after a block
                    self.difficulty = min(8, self.difficulty + 1)
                    prefix = '0' * self.difficulty
                    self.log(f"Difficulty increased to {self.difficulty}")
                nonce = 0
                # Small pause to avoid CPU spinning too fast on zero nonce
                time.sleep(0.001)
            nonce += 1

    def stop(self):
        self.mining = False
        self.log("Miner stopped.")

# ---------- GUI Application ----------
class MinerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Miner Pro")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # Login
        self.show_login()

    def show_login(self):
        self.clear_window()
        tk.Label(self.root, text="🔒 Login Required", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.check_credentials, width=15).pack(pady=15)
        self.root.bind('<Return>', lambda event: self.check_credentials())

    def check_credentials(self):
        if self.username_entry.get() == USERNAME and self.password_entry.get() == PASSWORD:
            self.show_miner()
        else:
            messagebox.showerror("Access Denied", "Invalid username or password.")

    def show_miner(self):
        self.clear_window()
        self.engine = MinerEngine(log_callback=self.add_log, stats_callback=self.refresh_stats)

        # Control frame
        control = tk.Frame(self.root)
        control.pack(pady=10)

        self.start_btn = tk.Button(control, text="▶ Start Mining", command=self.start_mining, bg="green", fg="white", width=15)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(control, text="⏹ Stop Mining", command=self.stop_mining, bg="red", fg="white", width=15, state=tk.DISABLED)
        self.stop_btn.grid(row=0, column=1, padx=5)

        # Stats frame
        stats = tk.LabelFrame(self.root, text="Statistics", padx=10, pady=10)
        stats.pack(fill="x", padx=20, pady=5)

        self.hashrate_var = tk.StringVar(value="0 H/s")
        self.shares_var = tk.StringVar(value="0")
        self.blocks_var = tk.StringVar(value="0")

        tk.Label(stats, text="Hashrate:").grid(row=0, column=0, sticky="w")
        tk.Label(stats, textvariable=self.hashrate_var, font=("Courier", 12)).grid(row=0, column=1, padx=20)

        tk.Label(stats, text="Shares:").grid(row=1, column=0, sticky="w")
        tk.Label(stats, textvariable=self.shares_var, font=("Courier", 12)).grid(row=1, column=1, padx=20)

        tk.Label(stats, text="Blocks:").grid(row=2, column=0, sticky="w")
        tk.Label(stats, textvariable=self.blocks_var, font=("Courier", 12)).grid(row=2, column=1, padx=20)

        # Log area
        log_frame = tk.LabelFrame(self.root, text="Miner Log", padx=5, pady=5)
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.log_area = scrolledtext.ScrolledText(log_frame, height=12, state='normal')
        self.log_area.pack(fill="both", expand=True)
        self.log_area.insert(tk.END, "Welcome to Crypto Miner Pro!\nReady to mine.\n\n")
        self.log_area.see(tk.END)
        self.log_area.config(state='disabled')

        # Miner thread placeholder
        self.miner_thread = None

    def start_mining(self):
        if self.miner_thread and self.miner_thread.is_alive():
            return
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.miner_thread = threading.Thread(target=self.engine.mine, daemon=True)
        self.miner_thread.start()

    def stop_mining(self):
        self.engine.stop()
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

    def add_log(self, message):
        self.log_area.config(state='normal')
        self.log_area.insert(tk.END, f"{message}\n")
        self.log_area.see(tk.END)
        self.log_area.config(state='disabled')

    def refresh_stats(self, hashrate, shares, blocks):
        self.hashrate_var.set(f"{hashrate} H/s")
        self.shares_var.set(str(shares))
        self.blocks_var.set(str(blocks))

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def on_closing(self):
        if hasattr(self, 'engine'):
            self.engine.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MinerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()