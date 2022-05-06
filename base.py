from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.font
import tkinter.scrolledtext
import tkinter.ttk
import tkinter.tix
import tkinter.ttk
import tkinter.tix
import tkinter.ttk

def stock(name):
    import yfinance as yf
    stock_info = yf.Ticker(name).info
    # stock_info.keys() for other properties you can explore
    market_price = stock_info['regularMarketPrice']
    previous_close_price = stock_info['regularMarketPreviousClose']
    print('market price ', market_price)
    print('previous close price ', previous_close_price)
    return 'market price ', market_price, 'previous close price ', previous_close_price


def hello():
    print("Hello")
    messagebox.showinfo("Hello", "Hello")
    # ask for my name
    name = tkinter.simpledialog.askstring("Hello", "Hello")
    print(name)
    messagebox.showinfo("Hello", stock(name))
  
    messagebox.showwarning("Hello", name)
    #show the current Apple inc. stocsk
    #ask for the stock value

hello()
