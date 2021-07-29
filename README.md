# Parkbot-challenge

## Installation

> In order to use this bot you will need to have Python3 install
> You can do it <a href="https://www.python.org/downloads/" target="blank"> here!</a> 

## How to run it

1. Make sure you are at the right directory
2. Write the following command on your console in order to start:


> ./parkbot

3. Now you have to enter the command line with the following structure:

> [fileName] [command] [argument]

- [fileName]: the name of the json file you want to use. Make sure your file is in the same directory as your parkbot file. 
- [command]: you can choose within: 
    - locate: in case you want to search by location
    - find_price_hourly_lte: in case you want to enter a maximum price
    - find_price_hourly_gt: in case you want to enter a minimum price
- [argument]: the argument based on the command chosen. 
    - If your command was "locate", the argument should be the state you are looking for. For example: AZ
    - If your command was "find_price_hourly_lte", the argument should be a number and you will be searching for parking lots with less or equal price per hour (in cents). For example: 200
    - If your command was "find_price_hourly_gt", the argument should be a number and you will be searching for parking lots with greater or equal price per hour (in cents). For example: 100

- Examples
> airgarage-data.json locate AZ

> airgarage-data.json find_price_hourly_lte 200

> airgarage-data.json find_price_hourly_gt 100


## Contact me!

📫 How to reach me 
- **lucilamrossi@gmail.com**
- LinkedIn: <a href="https://linkedin.com/in/lucila-rossi" target="blank">/lucila-rossi </a>
- GitHub: <a href="https://github.com/Lucilamrossi" target="blank">/Lucilamrossi </a>