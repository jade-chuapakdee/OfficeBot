# OfficeBot



## Introduction

OfficeBot, a cutting-edge office assistant revolutionizing document delivery within the workplace. Powered by the Bellman-Ford algorithm, traditionally employed in network optimization, OfficeBot navigates the office space with precision, calculating the shortest paths for efficient document transfers.


## Requirements

- Python 3.x
- pyswip
- Pillow


## How to run this project

Clone the repository:
```bash
  git clone https://github.com/TRP64011655/OfficeBot.git
```
    
Navigate to the project directory:
```bash
  cd OfficeBot/
```

Run the Python script:
```bash
  python ui\main.py 
```

Follow the instructions in the application:
- Select Destination
- Select Your Seat
- Select the Tray Number
- Click Confirm to accept the document
- Click the history icon to view the history of one or more deliveries. (Optional) 

## Files

- `deliverPackagePage.py` : This file is the page that shows the shortest path that the robot is taking.
- `historyFileManager.py` : This files is the file that manages history files. 
- `historyPage.py` : This file is the page that shows the history of the OffieBot.
- `main.py` : This is the main file to run the file.
- `my_prolog.py` : This file is a bridge between prolog and python files
- `pageReject.py` : This file is the page that shows the user that the docuement has been rejected and the reason of it.
- `reachedPage.py` : This file is the page that shows the user that the package is delivered. 
- `returnPackagePage.py` : This file is the page that displays the return path when the package is being rejected.
- `StartPage.py` : This file is the start page of the program.
- `history.csv` : This file contains the history of the deliveries.
- `my_bellman.pl` : This file contains the prolog logic for the Bellman-Ford algorithm.

