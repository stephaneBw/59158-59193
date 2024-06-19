# 59158-59193

## Small scrapping program

### Program description
This program will scrape an [online book store](http://books.toscrape.com/).
It will collect several pieces of information such as the title of the book,
its description, … and put this information in a csv file, which has the name of the category.
It will also produce a folder that has the name of the category
and put all the cover images of the books in the category there.

### Step 1: installing python3
If you have python3 installed, skip this step.
To run the program you must have python3 installed.
Visit this [link](https://www.python.org/downloads/) and follow the installation steps.

### Step 2: Creating a virtual environment in python
Download all files from git repository and put in a specific folder.
In this same file, you have to create a virtual environment in which
we will install the necessary modules.
You can find the required modules in the requirement.txt.
To create this environment, click on this [link](https://docs.python.org/fr/3/library/venv.html) and follow the
steps.

### Step 3: Install the necessary modules
Using a terminal, install pip.
*For macOS, type:
 - sudo easy_install pip
 - sudo pip install --upgrade pip
* For Windows and Linux: pip is already installed

Then navigate to the folder where the downloaded .py files as well as your virtual environment.
Finally, install the modules with pip as follows:
Type 'pip install [module name]'

### Step 4: Launch the program
You need to run user_interface.py only.
You can do this in the terminal.
If you are located in the directory where the files are located
Type: 'Python main.py'
You can also launch the program in your editor
of preferred code.

The csv files and image folders will be
created in the current directory.

To ideally view these files, open
Excel→Data→Get data→From file→From csv text file→select file
that you want to consult

You will need to select the file(s) in question by browsing
to their location.