# Reconb

Reconb is a multi-module reconnaissance tool for my HDE Project.

## Installation
Clone into the repository:
```
git clone https://github.com/idanbuller/Reconb.git
```

Use the requirements.txt file to install all python packages needed:

```bash
pip3 install -r requirements.txt
```

### Setup
First, run the following command to start apache2 & MySQL services:
```
sudo service apache2 start && service mysql start
```
Second, please run setup.py for setting up things needed:
```bash
python3 setup.py
```
Results:

```
>> Please paste here your MySQL user name: 
>> Please paste here your MySQL password: 
>> reconb Scheme created <<


[*] Please fill the empty values on keys.py [*]
```
Now, please fill the following fields on keys.py:
```
hunter = "your_api_key"
virus_total = "your_api_key"
mysql_username = "your_MySQL_username"
mysql_password = "your_MySQL_password"
```

## usage
After setting all the things up, you may run *Reconb*:
```bash
python3 reconb.py
```
```
8 888888888o.   8 8888888888       ,o888888o.        ,o888888o.     b.             8 8 888888888o   
8 8888    `88.  8 8888            8888     `88.   . 8888     `88.   888o.          8 8 8888    `88. 
8 8888     `88  8 8888         ,8 8888       `8. ,8 8888       `8b  Y88888o.       8 8 8888     `88 
8 8888     ,88  8 8888         88 8888           88 8888        `8b .`Y888888o.    8 8 8888     ,88 
8 8888.   ,88'  8 888888888888 88 8888           88 8888         88 8o. `Y888888o. 8 8 8888.   ,88' 
8 888888888P'   8 8888         88 8888           88 8888         88 8`Y8o. `Y88888o8 8 8888888888   
8 8888`8b       8 8888         88 8888           88 8888        ,8P 8   `Y8o. `Y8888 8 8888    `88. 
8 8888 `8b.     8 8888         `8 8888       .8' `8 8888       ,8P  8      `Y8o. `Y8 8 8888      88 
8 8888   `8b.   8 8888            8888     ,88'   ` 8888     ,88'   8         `Y8o.` 8 8888    ,88' 
8 8888     `88. 8 888888888888     `8888888P'        `8888888P'     8            `Yo 8 888888888P   


+----------------------------+-----+
| [*] We1c0me T0 Reconb [*]  | No. |
+----------------------------+-----+
| Domain-Subdomain-Ip search |  1  |
|       People Search        |  2  |
|  Files & Leaks & Busting   |  3  |
|   Open ports for Oports    |  4  |
|         Wappalyzer         |  5  |
|  Show all past scannings   |  6  |
|     Show table results     |  7  |
|    Export data to (csv)    |  8  |
|            Exit            |  q  |
+----------------------------+-----+
>>  m = menu
    b = back
Enter your choise:
```
