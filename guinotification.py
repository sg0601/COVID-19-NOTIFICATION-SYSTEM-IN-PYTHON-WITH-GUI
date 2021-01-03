# Message boxes are convenient dialogs that provide messages to the user of the application.
# IT IS THE TITLE OF THE GUI APPLICATION
from tkinter import messagebox, filedialog
# #  Plyer is a Python library for accessing features of your hardware / platforms.
# IT IS USED TO DISPLAY THE TEXT MESSAGE
import plyer
# using Tk and is Python's standard GUI framework.
from tkinter import *
#  pandas will help you to explore, clean and process your data. In pandas, a data table is called a DataFrame.
import pandas as pd
# # Beautiful Soup is a library that makes it easy to scrape information from web pages
from bs4 import BeautifulSoup
#  REQUEST MODULE HELPS#  TO SEND A GET  REQUEST TO A WEBSITE TO FETCH A WEBSITE
import requests
# PLYER HAS A FUNCTIO N NOTIFICATION PREBUILT TO PROVIDE NOTIFICATION
from plyer import notification
# SCRAP FUNCTION IS A FUNCTION FOR WEB SCRAPPING i.e FETCHING DATA FROM WEB
# WHEN SCRAP FUNCTION IS CALLED NOTIFICATION WILL POPUP AS IT HAS NESTED notifyme FUNCTION IN IT


def Scrap():
    # NOTIFYME IS A FUNCTION FOR DESKTOP NOTIFICATION
    # IT TAKES 2 ARGUMENTS TITLE AND MESSAGE
    def notifyme(title, message):
        #  IMPORT NOTIFY METHORD FROM NOTIFICATION CLASS OF PLYER MODULE
        plyer.notification.notify(
            # TITLE OF DESKTOP NOTIFICATION
            title=title,
            # MESSAGE OF DESKTOP NOTIFICATION
            message=message,
            # ICON OF DESKTOP NOTICATION (PATH CAN BE DIFFERENT)
            app_icon=r'D:\Programing\COVID 19 NOTIFICATION SYSTEM\Coronavirus-CDC-645x645.ico',
            # TIMEPERIOD FOR WHICH NOTIFICATION WILL BE ON SCREEN
            timeout=20
        )
        # URL OF THE WEBSITE FROM WHERE DATA IS FETCHED
    url = 'https://www.worldometers.info/coronavirus/'
    # r HOLDS THE DATA WHICH REQUEST GETS FROM THE URL
    r = requests.get(url)
    # # BS4 IS USED TO PARSE THE DATA WHICH TAKES 2 ARGUMENTS .1 HTML TEXT DOCUMENT AND
    # A HTML PARSER FOR WEB SCRAPPING DATA RETURNED IS STORED IN BS VARIABLE
    # CREATING A OBJECT OF BS4 NAMED soup
    soup = BeautifulSoup(r.content, 'html.parser')
    # TAKING HELP FROM bs4 DOCUMENTATION
    # soup.find SCRAPES THE DATA FROM THE tbody tag OF HTML TABLE AND GIVES IT TO VARIABLE tablebody
    tablebody = soup.find('tbody')
    # SCRAP ALL THE ROWS IN THE TABLEBODY
    # AS tr HAS THE NAME OF DIFFERENT STATES AND RETURN IT TO ttt VARIABLE
    ttt = tablebody.find_all('tr')
    # USING GET METHORD TO GET THE COUNTRY DATA IN VARIABLE notifycountry
    notifycountry = countrydata.get()
    # IF NO COUNTRY IS GIVEN AS INPUT SETTING IT BY DEFAULT TO INDIA
    if(notifycountry == ''):
        notifycountry = 'india'
        # CREATING THE LIST OF THE ATTRIBUTES OF THE TABLE SO THAT THEY CAN FURTHER BE TARGETED TO GET THE DESIRED DATA
        # LIST 0 IS COUNTRY 1 IS TOTAL CASES AND SO ON.. FOR ALL THE ATTRIBUTES OF THE TABLE
    countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases = [
    ], [], [], [], [], [], []
    serious, totalcases_permillion, totaldeaths_permillion, totaltests, totaltests_permillion = [], [], [], [], []
    # HEADERS ARE THE ATTRIBUTES OR THE COLOUMS OF THE TABLE
    headers = ['countries', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_recovered', 'active_cases',
               'serious', 'totalcases_permillion', 'totaldeaths_permillion', 'totaltests', 'totaltests_permillion']

# LOOP TO FIND ALL td TAGS (tr has many table data's) LOOP FOR 220 COUNTRIES
################################DETAILS ABOUT countries.append#######################
# APPEND IS A FUNCTION THAT ADDS THE TEXT TO THE END OF THE STRING,
# .TEXT IS USED TO GET TEXT FROM THE TABLE
# The syntax of the strip() method is:
# string.strip([chars])
# If the chars argument is not provided, all leading and trailing whitespaces are removed from the string

# .STRIP() IS AN INBUILT FUNCTION USED TO REMOVE SPACES IN THIS CASE
# .replaces is used to replace all the comma's with spaces
# [id's] ARE GIVEN AS  PER THE POSITION OF THE COLOUM IN THE TABLE
# PROCEDURE IS REPEATED FOR ALL THE 11 COLOUMS OF THE TABLE

    for i in ttt:
        # id VARIABLE TO FIND ALL td FROM tr
        id = i.find_all('td')
# TRYING TO MATCH THE DATA OF THE TABLE WITH NOTIFY COUNTRY SO THAT CORRENT COUNTRY CAN BE FOUND
# # .STRIP() IS AN INBUILT FUNCTION USED TO REMOVE SPACES IN THIS CASE
# .TEXT GIVES TEXT DATA
# .LOWER CONVERTS THE GIVEN INPUT INTO ALL LOWER CASE
        if(id[1].text.strip().lower() == notifycountry):
            # NOW CREATING VARIABLES totalcases1,totaldeaths1,....to pass it to notifyme function for notification
            # .replaces is used to replace all the comma's with spaces
            # [id's] ARE GIVEN AS  PER THE POSITION OF THE COLOUM IN THE TABLE
            totalcases1 = (id[1].text.strip().replace(',', ''))
            totaldeaths1 = id[3].text.strip()
            newcases1 = id[2].text.strip()
            newdeaths1 = id[4].text.strip()
            # NOW CALLING notifyme FUNCTION WHICH WILL GIVE DESKTOP NOTIFICATION
            # The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.
# Syntax
# string.format(value1, value2...)
            notifyme('Corona Virus Details In {}'.format(notifycountry),
                     'Total Cases : {}\nTotal Deaths : {}\nNew Cases : {}\nNew Deaths : {}'.format(totalcases1,
                                                                                                   totaldeaths1,
                                                                                                   newcases1,
                                                                                                   newdeaths1))
        countries.append(id[0].text.strip())
        total_cases.append((id[1].text.strip().replace(',', '')))
        new_cases.append(id[2].text.strip())
        total_deaths.append(id[3].text.strip())
        new_deaths.append(id[4].text.strip())
        total_recovered.append(id[5].text.strip())
        active_cases.append(id[6].text.strip())
        serious.append(id[7].text.strip())
        totalcases_permillion.append(id[8].text.strip())
        totaldeaths_permillion.append(id[9].text.strip())
        totaltests.append(id[10].text.strip())
        totaltests_permillion.append(id[11].text.strip())
        ################################################################################USING PANDAS##################
        # ZIP FUNCTION OF PANDAS COMBINES ALL THE LISTS OF A PARTICULAR INDEX INTO ONE LIST
        # COLOUMS WILL BE ALL THE INDEXES OF ID'S WHICH ARE DEFINED AS HEADERS
    df = pd.DataFrame(list(zip(countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases, serious,
                               totalcases_permillion, totaldeaths_permillion, totaltests, totaltests_permillion)), columns=headers)
                            #    sorting the data on the basics of totalcases in descending order
    sor = df.sort_values('total_cases', ascending=False)
    # FOR A VARIABLE K IN FORMATLIST
    for k in formatlist:
        # IF BUTTON PRESSED IS HTML
        if(k == 'html'):
            # SAVE THE FILE AS alldata.html and display file path as well
            path2 = '{}/alldata.html'.format(path)
            # CONVERTS THE DATA FILE TO HTML
            sor.to_html(r'{}'.format(path2))
            # IF BUTTON PRESSED IS JSON
        if(k == 'json'):
            # SAVE THE FILE AS alldata.json and display file path as well

            path2 = '{}/alldata.json'.format(path)
            # CONVERTS THE DATA FILE TO JSON
            sor.to_json(r'{}'.format(path2))
            # IF BUTTON PRESSED IS csv
        if(k == 'csv'):
            # SAVE THE FILE AS alldata.csv and display file path as well
            path2 = '{}/alldata.csv'.format(path)
            #  CONVERTS THE DATA FILE TO JSON
            sor.to_csv(r'{}'.format(path2))
            # IF LIST IS NOT EMPTY
    if(len(formatlist) != 0):
        # DISPLAY THE MESSAGEBOX ONCE THE DATAFILE IS SAVED
        # PARENT DIRECTORY OF PATH IS ROOT
        messagebox.showinfo(
            "Notification", 'Corona Record Is saved {}'.format(path2), parent=root)

# download function to download and store downloaded data at a particular location


def download():
    # PATH IS A GLOBAL VARIABLE AS PATH CAN BE ANYWHERE
    global path
    # IF ANY CLICK IS MADE i.e (IF NOT EMPTY)
    if(len(formatlist) != 0):
        # ASK WHERE TO STORE THE DATA
        path = filedialog.askdirectory()
        # IF CLICK IS NOT MADE IGNORE
    else:
        pass
    # CALLING OF SCRAP FUNCTION
    # SCRAP FUNCTION FETCHES DATA FROM  THE WEBSITE
    # SCRAP FUNCTION ALSO CONTAINS notifyme FUNCTION NESTED
    Scrap()
    # CLEAR THE LIST FOR ANOTHER ROUND ONCE THE DATA IS SAVED,NOTIFICATION IS DISPLAYED
    InHtml.configure(state='normal')
    formatlist.clear()
    # BRING INHTML FUNCTION BACK TO NORMAL STATE ONCE NOTIFICATION IS DISPLAYED
    InHtml.configure(state='normal')
    # BRING INJSON FUNCTION BACK TO NORMAL STATE ONCE NOTIFICATION IS DISPLAYED
    InJson.configure(state='normal')
    # # BRING Incsv FUNCTION BACK TO NORMAL STATE ONCE NOTIFICATION IS DISPLAYED
    InCsv.configure(state='normal')

# INHTML FUNCTION FOR EXECUTING THE PRESSED BUTTON COMMAND


def inhtml():
    # HTML IS PRESSED SO APPENDING HTML
    formatlist.append('html')
    # STOP APPENDING ONCE  HTML BUTTON IS PRESSED USING CONFIGURE METHORD
    InHtml.configure(state='disabled')

# incsv FUNCTION FOR EXECUTING THE PRESSED BUTTON COMMAND


def incsv():
    # csv IS PRESSED SO APPENDING csv
    formatlist.append('csv')
    # STOP APPENDING ONCE csv  BUTTON IS PRESSED USING CONFIGURE METHORD
    InCsv.configure(state='disabled')

# injason FUNCTION FOR EXECUTING THE PRESSED BUTTON COMMAND


def injson():
    # jason IS PRESSED SO APPENDING HTML

    formatlist.append('json')
    # STOP APPENDING ONCE JASON BUTTON IS PRESSED USING CONFIGURE METHORD
    InCsv.configure(state='disabled')
    InJson.configure(state='disabled')


################### TKINTER FUNCTION CONTINUED#########################################
# tkinter FUNCTIONN USES DIFFERENT WIDGETS
# The root widget has to be created before any other widgets and there can only be one root widget.
root = Tk()
# THIS IS THE TITLE OF THE GUI
root.title('Corona Virus Information ')
# geometry() method. This method is used to set the dimensions of the Tkinter window
# (length*width+fixing the window always at one position)
root.geometry('530x300+200+80')
# root.configure HELPS TO CHANGE BACKGROUND OF THE GUI WINDOW
root.configure(bg='plum2')
# PATH FOR ICON OF GUI APPLICATION AND r TO AVOID UNICODE ERROR
# root.iconbitmap to Set Window Icon
root.iconbitmap(r'D:\Programing\COVID 19 NOTIFICATION SYSTEM\Coronavirus-CDC-645x645.ico')
# FORMAT LIST IS A LIST TO STORE THE DATA WHEN CLICK IS MADE
formatlist = []
# path where downloaded data will be stored e.g Desktop
path = ''
################################ Labels#################################################
# This widget implements a display box where you can place text or images.
# SYNTAX:w = Label ( master, option, ... )
# master − This represents the parent window.
# options − Here is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas.

# CREATING CARONA VIRUS INFO LABEL IN GUI
# IN ROOT,TEXT,FONT,FONT-SIZE,BACKGROUND COLOUR AND WIDTH
IntroLabel = Label(root, text='Corona Virus Info', font=(
    'new roman', 30, 'italic bold'), bg='blue', width=22)
# SPECIFYING THE POSTION OF INTROLABEL X AND Y COORDINATES
IntroLabel.place(x=0, y=0)
# CREATING NOTIFY COUNTRY IN GUI
# # IN ROOT,TEXT,FONT,FONT-SIZE,BACKGROUND COLOUR AND WIDTH
EntryLabel = Label(root, text='Notify Country : ', font=(
    'arial', 20, 'italic bold'), bg='plum2')
# # SPECIFYING THE POSTION OF INTROLABEL(notify-country) X AND Y COORDINATES
EntryLabel.place(x=10, y=70)
# CREATING download in OF GUI IN ROOT
FormatLabel = Label(root, text='Download In : ', font=(
    'arial', 20, 'italic bold'), bg='plum2')
# SETTING THE POSITION OF DOWNLOAD IN
FormatLabel.place(x=10, y=150)

# CREATING A BOX FOR ENTERING A COUNTRY
# CREATING VARIABLE countrydata TO STORE THE STRING ENTERED IN NOTIFY-COUNTRY BOX
countrydata = StringVar()
# VALUE IS STORED IN ent1 in root,TAKING DATA FROM countrydata,
# GIVING FONT FONT-FAMILY ,BORDER,WIDTH
ent1 = Entry(root, textvariable=countrydata, font=(
    'arial', 20, 'italic bold'), relief=RIDGE, bd=2, width=20)
# SETTING THE POSITION OF NOTIFY COUNTRY BOX
ent1.place(x=220, y=70)
# CREATING 3 Buttons(Html,Csv,Jason IN VARIABLES InHtml,InCsv,InJason AND SPE-CIFYING THEIR VARIOUS ATTRIBUTES)
# The relief style of a widget refers to certain simulated 3-D effects around the outside of the widget
#  Background color for the widget when the widget is active.
# activeforeground − Foreground color for the widget when the widget is active.
# SAME FOR ALL THE 3 BUTTONS CREATED
# COMMAND IS A CALL TO INHTML FUNCTION
InHtml = Button(root, text='Html', bg='green', font=('arial', 15, 'italic bold'), relief=RIDGE, activebackground='blue', activeforeground='white',
                bd=5, width=5, command=inhtml)
#  SETTING THE POSITION OF HTML BUTTON
InHtml.place(x=210, y=150)
# CREATING A JASON BUTTON AND SETTING ITS POSITION
# COMMAND IS A CALL TO INJSON FUNCTION
InJson = Button(root, text='Json', bg='green', font=('arial', 15, 'italic bold'), relief=RIDGE, activebackground='blue', activeforeground='white',
                bd=5, width=5, command=injson)
# SETTING THE POSITION OF JSON BUTTON
InJson.place(x=320, y=150)
# CREATING A BUTTON CSV FOR GUI AND SETTING ITS POSITION
# COMMAND IS A CALL TO INcsv FUNCTION
InCsv = Button(root, text='Csv', bg='green', font=('arial', 15, 'italic bold'), relief=RIDGE, activebackground='blue', activeforeground='white',
               bd=5, width=5, command=incsv)
InCsv.place(x=430, y=150)
# CREATING A SUBMIT BUTTON SIMILARLY AND SETTING ITS POSITION
# # COMMAND IS A CALL TO download FUNCTION
Submit = Button(root, text='Submit', bg='red', font=('arial', 15, 'italic bold'), relief=RIDGE, activebackground='blue', activeforeground='white',
                bd=5, width=25, command=download)
Submit.place(x=110, y=250)

# mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
root.mainloop()
