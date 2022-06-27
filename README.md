# About
This program collects essential data from IT job offers posted on a popular website.  
Only offers from Poland are taken into account.  
Collected data includes:
- position
- seniority level
- salary
- company
- requirements
# How to use
## Necessary libraries:
- requests  
Installation command: ```pip install requests```
- Beautiful Soup  
Installation command: ```pip install bs4```  
- colorama  
Installation command: ```pip install colorama```

## Running the program
- open your terminal and clone the repository using the following command:  
```git clone https://github.com/ad-jusk/IT-WebScraper```  
- navigate to the cloned repository's directory
- enter this command:  
```python main.py```


## Demonstration
First, the program will ask you for your seniority level.  
The scale is as follows:
- **1 - trainee**
- **2 - junior**
- **3 - mid**
- **4 - senior**
- **5 - expert**  
  
Next, you will be asked to enter the name of the city where you want to search for offers.
Currently these cities are supported:
- **Warsaw**
- **Lodz**
- **Cracow**
- **Gdansk**
- **Wroclaw**  

![](/img/filters.png)

Based on your criteria, a set of offers will be returned.  
Each offer looks like this:  

![](/img/offer.png)

If you like a certain offer, you can choose to generate a direct link to it by entering its ID.  

![](/img/gettingLink.png)

After analysing the first set of offers, you can choose to search for more offers (which is equivalent to looking through another http site),
change filters or quit the programm.

![](/img/options.png)




