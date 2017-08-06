# GeeksForGeeksBookDownloader
Scrapes [GeeksForGeeks](http://www.geeksforgeeks.org) and creates html & PDF for chosen category along with syntax highlighting for the code.

## Installation
To use the scrapper, install the following:

`$ sudo apt-get install wkhtmltopdf`

Now install BeautifulSoup as:

`$ pip install beautifulsoup4`

or via package manager as:

`$ sudo apt-get install python-bs4`

or for Python dependencies, you can just install via `requirements.txt` inside the virtual environment.

`$ pip install -r requirements.txt`

## Run the G4G_Scrapper

$ python g4gMainAll.py

You can find the output as `G4G_<chunk number>.html` and `G4G_<chunk number>.pdf` in the same directory.

### Disclaimer: This is strictly for educational purpose only.
### Mostly issues if any then you would need to drop down the default value of maxCount defined in method downloadAll according to your system capacity.