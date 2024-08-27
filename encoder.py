import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import io
import random

def parse_seed(seed):
    random.seed(seed)

    count = random.randint(1, 20)
    complete = ""

    while count > 0:
        x = random.randint(1, 200)
        y = random.randint(1, 30)
        complete = complete + str(x) + ":" + str(y) + ";"
        count = count - 1
        continue
    complete = complete[:-1]

    """
    Parse the seed into a list of (position, shift) tuples for Caesar cipher.
    Example seed: '92:2' where
    - '92' means the position in the base64 string
    - '2' means shift the character at this position by 2
    """
    chunks = complete.split(';')
    parsed_seed = []
    for chunk in chunks:
        if ':' in chunk:
            try:
                pos, shift = chunk.split(':', 1)
                position = int(pos)  # Position to apply the cipher
                shift = int(shift)  # Caesar shift value
                parsed_seed.append((position, shift))
                print(f"Parsed seed: position={position}, shift={shift}")
            except (ValueError, IndexError):
                messagebox.showerror("Error", f"Invalid seed format: {chunk}")
                return []
        else:
            messagebox.showerror("Error", f"Invalid seed format: {chunk}")
            return []
    return parsed_seed

def caesar_cipher(char, shift):
    """
    Apply Caesar cipher shift to a single character.
    """
    if 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    elif 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        return char  # Non-alphabetic characters are not changed

def apply_seed_to_base64(seed, base64_str, reverse=False):
    parsed_seed = parse_seed(seed)
    if not parse_seed:
        return base64_str

    transformed_str = list(base64_str)  # Convert to list for mutable operations

    for position, shift in parsed_seed:
        if position < len(base64_str):
            char = base64_str[position]
            if reverse:
                # Reverse the Caesar cipher shift
                shift = -shift
            transformed_str[position] = caesar_cipher(char, shift)

    return ''.join(transformed_str)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        file_url_entry.delete(0, tk.END)
        file_url_entry.insert(0, file_path)

def save_image(content):
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if save_path:
        with open(save_path, 'wb') as file:
            file.write(content)
        messagebox.showinfo("Saved", f"Image saved successfully at {save_path}")

def transform_image(encode=True):
    seed = seed_entry.get()
    file_path = file_url_entry.get()

    if not seed or not file_path:
        messagebox.showerror("Error", "Please provide both a seed and a file path.")
        return

    try:
        with open(file_path, 'rb') as image_file:
            base64_str = base64.b64encode(image_file.read()).decode()

        if encode:
            transformed_str = apply_seed_to_base64(seed, base64_str)
        else:
            transformed_str = apply_seed_to_base64(seed, base64_str, reverse=True)

        transformed_bytes = base64.b64decode(transformed_str)

        save_image(transformed_bytes)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        

# Setup GUI

root = tk.Tk()
root.title("Base64 Image Transformer and Decoder")

tk.Label(root, text="Seed:").grid(row=0, column=0, padx=10, pady=10)
seed_entry = tk.Entry(root, width=50)
seed_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="File URL:").grid(row=1, column=0, padx=10, pady=10)
file_url_entry = tk.Entry(root, width=50)
file_url_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Browse", command=select_file).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Save Transformed Image", command=lambda: transform_image(encode=True)).grid(row=2, column=0, columnspan=3, padx=10, pady=10)

tk.Button(root, text="Save Decoded Image", command=lambda: transform_image(encode=False)).grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
