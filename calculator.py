# Import thư viện tkinter để tạo giao diện đồ họa
import tkinter as tk
from tkinter import messagebox

# Hàm kiểm tra đầu vào có phải là số tự nhiên không
def is_natural_number(value):
    # Kiểm tra xem chuỗi có phải là số nguyên dương không
    if value.isdigit() and int(value) >= 0:
        return True
    return False

# Hàm thực hiện phép tính khi người dùng nhấn nút
def calculate(operation):
    # Lấy giá trị từ hai ô nhập liệu
    num1_str = entry_num1.get().strip()
    num2_str = entry_num2.get().strip()
    
    # Kiểm tra xem người dùng đã nhập đủ hai số chưa
    if not num1_str or not num2_str:
        result_label.config(text="Vui lòng nhập đủ hai số tự nhiên")
        return
    
    # Kiểm tra xem đầu vào có phải là số tự nhiên không
    if not is_natural_number(num1_str) or not is_natural_number(num2_str):
        result_label.config(text="Vui lòng nhập hai số tự nhiên")
        return
    
    # Chuyển đổi chuỗi thành số nguyên
    num1 = int(num1_str)
    num2 = int(num2_str)
    
    # Thực hiện phép tính tương ứng
    if operation == "+":
        result = num1 + num2
        result_label.config(text=f"Kết quả: {num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        result_label.config(text=f"Kết quả: {num1} - {num2} = {result}")
    elif operation == "×":
        result = num1 * num2
        result_label.config(text=f"Kết quả: {num1} × {num2} = {result}")
    elif operation == "÷":
        # Kiểm tra chia cho 0
        if num2 == 0:
            result_label.config(text="Không thể chia cho 0")
            return
        # Thực hiện phép chia và làm tròn kết quả đến 2 chữ số thập phân
        result = num1 / num2
        result_label.config(text=f"Kết quả: {num1} ÷ {num2} = {result:.2f}")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Máy Tính Đơn Giản")
window.geometry("400x300")  # Kích thước cửa sổ
window.resizable(False, False)  # Không cho phép thay đổi kích thước cửa sổ

# Tạo tiêu đề
title_label = tk.Label(window, text="MÁY TÍNH ĐƠN GIẢN", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Tạo khung chứa các thành phần
frame = tk.Frame(window)
frame.pack(pady=10)

# Tạo nhãn và ô nhập liệu cho số thứ nhất
num1_label = tk.Label(frame, text="Số thứ nhất:", font=("Arial", 12))
num1_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_num1 = tk.Entry(frame, font=("Arial", 12), width=15)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

# Tạo nhãn và ô nhập liệu cho số thứ hai
num2_label = tk.Label(frame, text="Số thứ hai:", font=("Arial", 12))
num2_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_num2 = tk.Entry(frame, font=("Arial", 12), width=15)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Tạo khung chứa các nút phép tính
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Tạo các nút phép tính
button_add = tk.Button(button_frame, text="+", font=("Arial", 14), width=5, 
                      command=lambda: calculate("+"))
button_add.grid(row=0, column=0, padx=5, pady=5)

button_subtract = tk.Button(button_frame, text="-", font=("Arial", 14), width=5, 
                           command=lambda: calculate("-"))
button_subtract.grid(row=0, column=1, padx=5, pady=5)

button_multiply = tk.Button(button_frame, text="×", font=("Arial", 14), width=5, 
                           command=lambda: calculate("×"))
button_multiply.grid(row=0, column=2, padx=5, pady=5)

button_divide = tk.Button(button_frame, text="÷", font=("Arial", 14), width=5, 
                         command=lambda: calculate("÷"))
button_divide.grid(row=0, column=3, padx=5, pady=5)

# Tạo nhãn hiển thị kết quả
result_label = tk.Label(window, text="Kết quả sẽ hiển thị ở đây", font=("Arial", 14))
result_label.pack(pady=10)

# Tạo nút xóa dữ liệu
def clear_entries():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="Kết quả sẽ hiển thị ở đây")

clear_button = tk.Button(window, text="Xóa dữ liệu", font=("Arial", 12), 
                        command=clear_entries)
clear_button.pack(pady=5)

# Bắt đầu vòng lặp sự kiện chính
window.mainloop()