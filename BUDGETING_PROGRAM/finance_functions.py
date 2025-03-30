import numpy as np
import pandas as pd
import plotly.graph_objects as go
import datetime
import calendar

def budgeting(income, expense):
    net = income - expense
    allowance = 600
    check = input("Do you want to add allowance?: ")
    if check == "yes":
        total = net + allowance
    else:
        total = net

    grocery, fast_food, total_food, ff_days = basic_needs(total)
    days_in_month = datecheck()

    # initialize subscriptions
    subscriptions_total = 0

    investment_style = input("Choose (safe) or (risky) investment style: ") #Choose conservative or risky style for rebalancing
    dict = finance(total, grocery, fast_food, total_food, subscriptions_total, investment_style)
    
    s = pd.Series(dict)

def basic_needs(total):
    grocery = (total * 0.075) * 4
    fast_food = (total * 0.075) * 4
    total_food = grocery + fast_food
    ff_days = fast_food / 20
    return grocery, fast_food, total_food, ff_days

def datecheck():
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    days_in_month = calendar.monthrange(year,month)[1]
    return days_in_month

def finance(total, grocery, fast_food, total_food, subscriptions_total, investment_style):
    savings = total * 0.2
    remainder = round(((total - (total_food + subscriptions_total + savings))), 2)
    fun = round((remainder * 0.2), 2)
    allocation = remainder - fun
        
    if investment_style == "safe":
        stocks = round((allocation * 0.25), 2)
        bonds = round((allocation * 0.40),2)
        realestate = round((allocation * 0.1),2)
        commodities = round((allocation * 0.1),2)
        money_fund = round((allocation * 0.15))
    else:
        stocks = round((allocation * 0.4), 2)
        bonds = round((allocation * 0.3), 2)
        realestate = round((allocation * 0.1),2)
        commodities = round((allocation * 0.15), 2)
        money_fund = round((allocation * 0.05),2)
        
    Saving = (savings / 3)
    Roth_IRA = (savings / 3)
    e_fund = (savings / 3)
    schwab = Roth_IRA + stocks + bonds + realestate + commodities + money_fund

    dict = {
        "Income":total,
        "Grocery":grocery,
        "Fast_Food":fast_food,
        "Total Food":total_food,
        "Subscriptions":subscriptions_total,
        "N26 Saving":Saving,
        "Roth_IRA":Roth_IRA,
        "Emergency Fund":e_fund,
        "Remainder":remainder,
        "Stocks":stocks,
        "Bonds":bonds,
        "REITs":realestate,
        "Commodities":commodities,
        "Money Market Fund":money_fund,
        "Schwab Total":schwab,
        "Fun":fun
        }
    
    return dict