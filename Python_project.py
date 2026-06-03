# my project - Data Analysis by Web Scraping Using Python
# i am using beautifulsoup to scrape data from a website
# then storing it in sqlite database
# and showing everything in a tkinter window

import requests
from bs4 import BeautifulSoup
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# ----- database connection -----
conn = sqlite3.connect("books_data.db")
c = conn.cursor()

# create table if not already there
c.execute("""CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            rating TEXT
          )""")
conn.commit()


# ----- scrape the website -----
def get_data():
    try:
        url = "https://books.toscrape.com/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        # all books are inside article tag with class product_pod
        all_books = soup.find_all("article", class_="product_pod")

        for book in all_books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text

            # rating is stored as a word like One Two Three etc in the class
            rating_tag = book.find("p", class_="star-rating")
            rating = rating_tag["class"][1]  # second class is the rating word

            # save to database
            c.execute("INSERT INTO books (title, price, rating) VALUES (?, ?, ?)",
                      (title, price, rating))

        conn.commit()
        show_data()
        messagebox.showinfo("Done", "Data scraped successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ----- show data in the table -----
def show_data():
    # first clear the table
    for row in tree.get_children():
        tree.delete(row)

    c.execute("SELECT * FROM books")
    rows = c.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)


# ----- search books by title -----
def search():
    word = search_box.get()

    for row in tree.get_children():
        tree.delete(row)

    c.execute("SELECT * FROM books WHERE title LIKE ?", ("%" + word + "%",))
    result = c.fetchall()

    for row in result:
        tree.insert("", "end", values=row)


# ----- delete all data -----
def clear_all():
    confirm = messagebox.askyesno("Confirm", "Do you want to delete all data?")
    if confirm:
        c.execute("DELETE FROM books")
        conn.commit()
        show_data()


# ----- simple analysis -----

def analyse():
    try:
        import re

        c.execute("SELECT price FROM books")
        all_prices = c.fetchall()

        if len(all_prices) == 0:
            messagebox.showinfo("Analysis", "No data found. Please scrape first.")
            return

        prices = []

        for p in all_prices:
            match = re.search(r"\d+\.\d+", p[0])
            if match:
                prices.append(float(match.group()))

        if len(prices) == 0:
            messagebox.showerror("Error", "Still no valid price data found")
            return

        lowest = min(prices)
        highest = max(prices)
        average = sum(prices) / len(prices)

        messagebox.showinfo(
            "Analysis Result",
            f"Total Books: {len(prices)}\n"
            f"Lowest Price: £{lowest}\n"
            f"Highest Price: £{highest}\n"
            f"Average Price: £{round(average, 2)}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))
# ==================== GUI ====================

window = tk.Tk()
window.title("Book Price Tracker")
window.geometry("850x550")
window.config(bg="#f0f0f0")

# top label
top = tk.Label(window, text="Data Analysis by Web Scraping",
               font=("Arial", 16, "bold"), bg="#2c3e50", fg="white")
top.pack(fill="x", pady=0)

sub = tk.Label(window, text="Source: books.toscrape.com",
               font=("Arial", 9), bg="#2c3e50", fg="#aaaaaa")
sub.pack(fill="x")

# buttons frame
btn_frame = tk.Frame(window, bg="#f0f0f0", pady=8)
btn_frame.pack()

scrape_btn = tk.Button(btn_frame, text="Scrape Data", command=get_data,
                       bg="#3498db", fg="white", padx=10, pady=4)
scrape_btn.grid(row=0, column=0, padx=6)

search_box = tk.Entry(btn_frame, width=25)
search_box.grid(row=0, column=1, padx=6)

search_btn = tk.Button(btn_frame, text="Search", command=search,
                       bg="#27ae60", fg="white", padx=10, pady=4)
search_btn.grid(row=0, column=2, padx=6)

analyse_btn = tk.Button(btn_frame, text="Analyse", command=analyse,
                        bg="#8e44ad", fg="white", padx=10, pady=4)
analyse_btn.grid(row=0, column=3, padx=6)

clear_btn = tk.Button(btn_frame, text="Clear All", command=clear_all,
                      bg="#e74c3c", fg="white", padx=10, pady=4)
clear_btn.grid(row=0, column=4, padx=6)

# table to show books
frame = tk.Frame(window)
frame.pack(fill="both", expand=True, padx=15, pady=5)

scroll = tk.Scrollbar(frame)
scroll.pack(side="right", fill="y")

cols = ("ID", "Title", "Price", "Rating")
tree = ttk.Treeview(frame, columns=cols, show="headings", yscrollcommand=scroll.set)
scroll.config(command=tree.yview)

tree.heading("ID", text="ID")
tree.heading("Title", text="Title")
tree.heading("Price", text="Price")
tree.heading("Rating", text="Rating")

tree.column("ID", width=40, anchor="center")
tree.column("Title", width=500, anchor="w")
tree.column("Price", width=80, anchor="center")
tree.column("Rating", width=100, anchor="center")

tree.pack(fill="both", expand=True)

# load existing data when app opens
show_data()

window.mainloop()

# close connection
conn.close()