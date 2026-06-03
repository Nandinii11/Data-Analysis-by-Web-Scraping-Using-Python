# Book Price Tracker - Data Analysis by Web Scraping Using Python

A Python-based desktop application that performs **web scraping**, **data storage**, **data analysis**, and **data visualization through a GUI**. The project scrapes book information from the Books To Scrape website, stores it in an SQLite database, and allows users to search and analyze the collected data through a Tkinter interface.

---

##  Features

-  Web scraping using BeautifulSoup
-  Data storage using SQLite database
-  Search books by title
-  Basic price analysis
  - Total number of books
  - Lowest price
  - Highest price
  - Average price
-  User-friendly Tkinter GUI
-  Clear all stored data option

---

##  Technologies Used

- Python
- BeautifulSoup4
- Requests
- SQLite3
- Tkinter

---

##  Project Structure


Book-Price-Tracker/
│

├── Python_project.py

├── books_data.db (created automatically)

└── README.md


---

##  Workflow

1. Click **Scrape Data**
2. Data is fetched from `books.toscrape.com`
3. Book details are stored in SQLite database
4. Data is displayed in the GUI table
5. Search books by title
6. Analyze book prices using the Analyze button

---

##  Data Collected

The application extracts:

| Field | Description |
|---------|-------------|
| Title | Book Title |
| Price | Book Price |
| Rating | Book Rating (One to Five Stars) |

---

##  Installation

### Clone the Repository

bash
git clone https://github.com/your-username/book-price-tracker.git
cd book-price-tracker

- Install Dependencies
 
   pip install requests beautifulsoup4

- Run the Application

   python Python_project.py

- Sample Analysis Output
  
   Total Books: 20

   Lowest Price: £12.84

   Highest Price: £57.22

   Average Price: £34.56

### Learning Outcomes

This project helped in understanding:

- Web Scraping with BeautifulSoup
- HTTP Requests using Requests
- Database Operations using SQLite
- GUI Development using Tkinter
- Basic Data Analysis in Python
- Error Handling and User Interaction
### Future Improvements
- Export data to CSV or Excel
- Add charts and visualizations using Matplotlib
- Prevent duplicate entries in database
- Scrape multiple pages automatically
- Add filters based on rating and price
- Create a modern GUI using CustomTkinter
### Data Source

Website used for scraping:

https://books.toscrape.com/

(This website is specifically designed for practicing web scraping.)

### Author

Nandnee Kapse

Data Science & AI Student

