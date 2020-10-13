from tkinter import *
from tkinter import ttk
import random
class book:
  """The book class stores the details of each book and has methods to restock, sell and calculate progress towards the Super Dude goal""""
  def __init__(self, name, stock, sold):
   self.name = name
   self.stock = stock
   self.sold = sold
   book_list.append(self)
    
  def restock(self, amount):
  if amount > 0:
   self.stock += amount
  return True
    else:
      return False
  def sell(self, amount):
    if amount > 0 and amount <= self.stock:
      self.stock -= amount
      self.sold += amount
      return True
    else:
      return False
def create_name_list():
  name_list = []
  for book in book_list:
    name_list.append(book.name)
  return name_list
def update_stock():
  total_sold = 0
  stock_string = ""

  for book in book_list:
    stock_string += "{}: {}\n".format(book.name, book.stock)
    total_sold += book.sold
  stock_string += "\nTotal Stock Sold: {}".format(total_sold)
  book_details.set(stock_string)
def restock_stock(book):
 if book.restock(amount.get()):
 message_text.set(restock_message)
 action_feedback.set("yo ! Total of {} restocked into {}".format(amount.get(), book.name))
 else:
   action_feedback.set("yo! enter a positive number")

def sell_stock(book):
 if book.sell(amount.get()):
  message_text.set(sell_message)
  action_feedback.set("yo! Total of {} sold from {}".format(amount.get(), book.name))
  else:
    action_feedback.set("Not enough stock in {} or not a valid amount, It will come on error".format(book.name))

def manage_action():
  try:
    for book in book_list:
      if chosen_book.get() == book.name:
    if chosen_action.get() == "Restock":
     restock_stock(book)
     else:
        sell_stock(book)
            
    update_stock()
    amount.set("")
  
  except ValueError:
    action_feedback.set("Please enter a valid number")
    
book_list = []
restock_message = ("you are Restocking yo!")
sell_message = ("you on aSale made yo!")

Comic1 = book("Super Dude", 8, 0)
Comic2 = book("Lizard Man", 12, 0)
Comic3 = book("Water Woman", 3, 0)
book_names = create_name_list()

root = Tk()
root.title("Comic book store")

top_frame = ttk.LabelFrame(root, text="Book's Details")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

message_text = StringVar()
message_text.set("hey hey yoyo ! Oscar root can help u restock, sell and view the tolal stock in here :")

message_label = ttk.Label(top_frame, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=11, pady=10)

book_details = StringVar()

details_label = ttk.Label(top_frame, textvariable=book_details)
details_label.grid(row=2, column=0, columnspan=2, padx=11, pady=10)

bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=11, pady=10, sticky="NSEW")

book_label = ttk.Label(bottom_frame, text="YO! Comic's Book: ")
book_label.grid(row=3, column=0, padx=10, pady=3)

chosen_book = StringVar()
chosen_book.set(book_names[0])

book_box = ttk.Combobox(bottom_frame, textvariable=chosen_book, state="readonly")
book_box['values'] = book_names
book_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")

action_label = ttk.Label(bottom_frame, text="YO! Action:")
action_label.grid(row=4, column=0)

action_list = ["Restock", "Sell"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

action_box = ttk.Combobox(bottom_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=4, column=1, padx=15, pady=8, sticky="WE")

amount_label = ttk.Label(bottom_frame, text="Amount:")
amount_label.grid(row=5, column=0, padx=10, pady=3)

amount = DoubleVar()
amount.set("")

amount_entry = ttk.Entry(bottom_frame, textvariable=amount)
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

submit_button = ttk.Button(bottom_frame, text="Submit", command=manage_action)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

action_feedback = StringVar()
action_feedback.set("")
action_feedback_label = ttk.Label(bottom_frame, textvariable=action_feedback)
action_feedback_label.grid(row=7, column=0, columnspan=2)

update_stock()
root.mainloop()


