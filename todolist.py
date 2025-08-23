import tkinter as tk
from tkinter import messagebox

# ฟังก์ชั่นสำหรับเพิ่มงาน
def add_task():
    task = entry_task.get()  # รับข้อมูลจากช่องกรอก
    if task != "":
        listbox_tasks.insert(tk.END, task)  # เพิ่มงานใน Listbox
        entry_task.delete(0, tk.END)  # ล้างช่องกรอก
        update_file()  # อัปเดตไฟล์หลังจากเพิ่มงาน
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")  # แสดงข้อความเตือนหากไม่มีการกรอกงาน

# ฟังก์ชั่นสำหรับลบงาน
def delete_task():
    try:
        task_index = listbox_tasks.curselection()  # เลือกงานที่ต้องการลบ
        listbox_tasks.delete(task_index)  # ลบงานที่เลือก
        update_file()  # อัปเดตไฟล์หลังจากลบงาน
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")  # แสดงข้อความเตือนหากไม่ได้เลือกงาน

# ฟังก์ชั่นสำหรับมาร์คงานว่าเสร็จแล้ว
def mark_completed():
    try:
        task_index = listbox_tasks.curselection()  # เลือกงานที่ต้องการมาร์ค
        task = listbox_tasks.get(task_index)  # รับข้อมูลงานที่เลือก
        listbox_tasks.delete(task_index)  # ลบงานเก่า
        listbox_tasks.insert(task_index, task + " - Completed")  # เพิ่มงานที่มาร์คเสร็จแล้ว
        update_file()  # อัปเดตไฟล์หลังจากมาร์คงาน
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")  # แสดงข้อความเตือนหากไม่ได้เลือกงาน

# ฟังก์ชั่นสำหรับอัปเดตไฟล์
def update_file():
    with open("tasks.txt", "w") as file:  # เปิดไฟล์เพื่อเขียนข้อมูล
        tasks = listbox_tasks.get(0, tk.END)  # รับข้อมูลทั้งหมดใน Listbox
        for task in tasks:
            file.write(task + "\n")  # เขียนแต่ละงานลงในไฟล์

# ฟังก์ชั่นสำหรับโหลดข้อมูลจากไฟล์
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:  # เปิดไฟล์เพื่ออ่านข้อมูล
            tasks = file.readlines()  # อ่านข้อมูลทั้งหมดในไฟล์
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())  # เพิ่มงานใน Listbox
    except FileNotFoundError:
        pass  # หากไฟล์ไม่พบก็ไม่ต้องทำอะไร

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("To-Do List")

# ช่องกรอกงาน
entry_task = tk.Entry(root, width=35)
entry_task.grid(row=0, column=0, padx=10, pady=10)

# ปุ่มเพิ่มงาน
button_add = tk.Button(root, text="Add Task", width=20, command=add_task)
button_add.grid(row=0, column=1, padx=10, pady=10)

# Listbox สำหรับแสดงงาน
listbox_tasks = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
listbox_tasks.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# ปุ่มลบงาน
button_delete = tk.Button(root, text="Delete Task", width=20, command=delete_task)
button_delete.grid(row=2, column=0, padx=10, pady=10)

# ปุ่มมาร์คงานเสร็จ
button_completed = tk.Button(root, text="Mark as Completed", width=20, command=mark_completed)
button_completed.grid(row=2, column=1, padx=10, pady=10)

# โหลดข้อมูลจากไฟล์เมื่อเริ่มโปรแกรม
load_tasks()

# เริ่มโปรแกรม
root.mainloop()
