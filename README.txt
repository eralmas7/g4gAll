Goal
=====
Download problems listed on GeeksForGeeks.org in an easy to read pdf format.

Requirement:
-------------
GeeksForGeeks is an excellent site for preparing algorithm and data structures. It has helped many people in getting jobs at Google, Amazon, Microsoft etc.

One things that people find problem with is, Everytime i need to look at the problems on GeeksForGeeks.org, i have to turn on data plan or logon to internet and start reading problems one by one.

With static file, i can open and read from anywhere and can work out without the need of internet. All the problems are at one place.

The only thing i would be missing is the comments around the solution and if any new problem is added onto the site.

With this in mid, we have designed a project that Scrapes [GeeksForGeeks](http://www.geeksforgeeks.org) and creates html & PDF for all the categories listed along with syntax highlighting for the code.

Instructions to build and run the application.
---------------------------------------------

##### Pre-requisite for this project:
	- To use the scrapper, install the following:
		`$ sudo apt-get install wkhtmltopdf`
	- Now install BeautifulSoup as:
		`$ pip install beautifulsoup4`
		or via package manager as:
		`$ sudo apt-get install python-bs4`
		or for Python dependencies, you can just install via `requirements.txt` inside the virtual environment as below:
		`$ pip install -r requirements.txt`

##### To build and run the application:
	$ python g4gMainAll.py
	
##### Output from the application:
You can find the output as `G4G_<chunk number>.html` and `G4G_<chunk number>.pdf` in the same directory.

### Disclaimer: This is strictly for educational purpose only.
### Mostly issues if any then you would need to drop down the default value of maxCount defined in method downloadAll according to your system capacity.