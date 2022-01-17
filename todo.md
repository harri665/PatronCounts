# Todo stuff 
# Packaging instructions 
1. Set Version in Version.txt to Correct Version
2. Arm the program 
3. delete all in input.txt
4. run auto-py-to-exe
5. select main.py
6. add files 
    - From Project Directory: C:\Users\Harri\OneDrive\Projects\PatronCounts
        - Files
            - input.txt
            - Version.txt
            - All updateX.X.txt
            - ChemicalRecordTemplate.xlsx
        - Folder
            - Website
    - From Python Root C:\Users\Harri\AppData\Local\Programs\Python\Python310
        - Files
            - chromedriver.exe
            - geckodriver.exe
            - IEDriverServer.exe
7. Add Icon in Downloads 
8. Advanced -> name = Digiquatics V2
9. RUN !!
10. Go to pastebin https://pastebin.com/bB4wBAPP
    - insert new update logs !
- Command to Run 
  - pyinstaller --noconfirm --onedir --windowed --icon "C:/Users/Harri/Downloads/Logomark.ico" --name "DigiquaticsV2" --version-file "C:/Users/Harri/OneDrive/Projects/PatronCounts/file_version_info.txt" --add-data "C:/Users/Harri/OneDrive/Projects/PatronCounts/ChemicalRecordTemplate.xlsx;." --add-data "C:/Users/Harri/OneDrive/Projects/PatronCounts/input.txt;." --add-data "C:/Users/Harri/OneDrive/Projects/PatronCounts/update1.1.txt;." --add-data "C:/Users/Harri/OneDrive/Projects/PatronCounts/update1.2.txt;." --add-data "C:/Users/Harri/OneDrive/Projects/PatronCounts/update1.3.txt;." --add-data "C:/Users/Harri/OneDrive/Projects/PatronCounts/Version.txt;." --add-data "C:/Users/Harri/OneDrive/Projects/PatronCounts/Website;Website/" --add-data "C:/Users/Harri/AppData/Local/Programs/Python/Python310/chromedriver.exe;." --add-data "C:/Users/Harri/AppData/Local/Programs/Python/Python310/geckodriver.exe;." --add-data "C:/Users/Harri/AppData/Local/Programs/Python/Python310/IEDriverServer.exe;."  "C:/Users/Harri/OneDrive/Projects/PatronCounts/main.py"

git filter-branch --index-filter "git rm -rf --cached --ignore-unmatch C:\Users\Harri\OneDrive\Projects\PatronCounts\input.txt" HEAD
# small 
- Change Opening and closing to approperate times 


# big 

- Make it look nice 
- Import big xcel file after written to 
- make a way to detect login failure 


# issues 
- Clicking pages too fast hit error when loading setup scripts 