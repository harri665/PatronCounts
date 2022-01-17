#  Patron Counts Code 

program created to speed up the entry of Patron and Chem check into Digiquatics 

1. Yes the Code is messy if this project takes off i will fix that 
2. you can read through the code to check for malisous use
    - Usernames and Passwords are stored in plain text which is the only bad use of them. they are never sent to the internet or stored anywhere else 


## What do you need to build/run? 
- Chrome version `97`
- Python 
  - make sure python is added to path 
- Pip (if not already included)
  - Selenium
    - `pip install selenium`
    - used to control Chrome
  - Open Py Xl
    - `pip install openpyxl`
    - read and write to excel docs
  - EEL
    - `pip install eel`
    - used for GUI
  - Either Auto-Py-to-Exe or Pyinstaller
    - Auto-py-to-exe
      - `pip install auto-py-to-exe`
      - build program 
    - Pyinstaller
      - `pip install pyinstaller`
      - build program 

## Build 
- Using Auto py to exe
  1. Set Version in Version.txt to Correct Version
  2. Arm the program 
  3. delete all in input.txt
  4. run auto-py-to-exe
  5. select main.py
  6. add files 
      - From Project Directory: 
          - Files
              - input.txt
              - Version.txt
              - All updateX.X.txt
              - ChemicalRecordTemplate.xlsx
          - Folder
              - Website
      - From Python Root 
          - Files
              - chromedriver.exe
              - geckodriver.exe
              - IEDriverServer.exe
  7. Add Icon in Downloads 
  8. Advanced -> name = Digiquatics V2
  9. RUN !!

