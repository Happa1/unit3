# Unit3 Project

**Fig.1**

# Criteria A: Planning

## Problem definition (Client Identification)
The client, a locan entrepreneur M, opened sustainable candle shop,"Candelique", just a month ago.
Candelique is at the forefront of innovation in the candle industry, blending sustainability with cutting-edge designs. 
Candles in her shop are popular for its sustainability and cute designs, so many customers come every day. 
The more customers come than she expected, and she only uses paper to track the order of candle materials. 
Therefore, sometimes shop staff forget to record the material purchased and many materials run out due to a defective inventory list.
As well as inventory, the track of money is recorded on the paper, and it makes it difficult for her to calculate profit and expenditure of materials.
it is vulnerable in terms of security because it is not clear who purchases materials or takes an order and handles money.
Keeping record inventory and money on paper leads to shop staff more likely to make mistakes, and the balance of money doesn't match due to steal by staff.
Also, there are many materials for the candle and each of them has various sustainability characteristics, producing area, and effects for mental relaxation.
This information is hard for new staff to memorize everything, so she needs the system to refer the description of materials.

(see evidence of consultation in AppendixA)


## Proposed Solution
Considering the client's requirements, a GUI (Graphical User Interface) application seems to be best option because it has clear visual which is easy to use.
- mistakes on tracking money on paper
    -> the application keeps track of money of purchase of materials and order by customers and calculate, profit, expenditure and balance by clicking a button(not number typing).
- mistakes on tracking inventory on paper
    ->the application keeps track of the number of materials which changes by the purchase of materials and order by customer. It also shows what kind of materials are lacking. 
- memorization of description of materials
    ->
- running out of inventory due to a lack of analysis of inventory and popularity of candle



## Tools of my solution

**Citation**


## Structure of my solution


## Success Criteria
1. The application has signup and login system that shop staff can be login by username and password.
2. The application keeps track of inventory of candle materials.
3. The application keeps track of money of purchase for materials and order from customers.
4. The application create a system to create a candle by using.
5. Client can see the description of each raw materials when they click the button.
6. Client automatically calculated the amount of purchase of materials next month depending on the inventory and also the popularity of candle. 

# Criteria B: Design

## System Diagram

## Flow Diagrams

# Criteria C: Development

| Task No | Planned Action                                        | Planned Outcome                                                                                                                  | Time estimate | Target completion date | Criterion |
|---------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Decide crypto currency which I use                    | To decide what type of crypto currency I use in this project.                                                                    | 10 min        | Sep 11                 | A         |
| 2       | Write a description about LTC                         | To understand the crypto currency which I use in this project, and to create a currency description to use it in code.           | 20 min        | Sep 12                 | A         |
| 3       | Create system diagram                                 | To have a clear idea of the hardware and software requirements for the proposed solution.                                        | 15min         | Sep 13                 | B         |
## Testing plan
| Test                         | Type               | Process (input)                                                                                                                                                                                                                                    | Expected output                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User Signup                  | Unit testing       | 1. Choose 1 as a signup option (1) 2. Enter a username. (mano) 3. Enter a password. (1357) 4. Enter a confirmation password. (1357)                                                                                                                | If the username is not used already sign upped users,  and the password and a confirmation password match,  record the username and the password in the csv file. If the user successfully can sign up, the login menu is displayed.                                                                                                                                                                                                |
| User Login                   | Unit testing       | 1. Enter a username. (mano) 2. Enter a password. (1357)                                                                                                                                                                                            | If the username and the password that the user entered match with the  data on the csv file of user data, the user successfully logged in.                                                                                                                                                                                                                                                                                          |
| Validate the Integer of menu | Unit testing       | 1. Enter the number depending on the menu the user chooses. (1 or 2 or 3 or 4 or 5 or 6)                                                                                                                                                           | If the thing that the user entered is an integer and either one of the numbers in menu, program move on to the session depending on the number the user chooses.                                                                                                                                                                                                                                                                    |
| Deposit                      | Unit testing       | 1. Choose deposit in menu (1). 2. Enter a description of the deposit. (food) 3. Enter the amount of the deposit. (150)                                                                                                                             | If the user enter description and the amount in integer, date, description, deposit(category), amount, balance is recorded in the user's own atm csv file. If the deposit system is successfully done, it displays "Saved" and shows the balance that the user currently has. Also, if the balance is bigger than 0, it displays "You're not debt", and if it is below 0, displays "You're debt"                                    |
| Currency exchange            | Unit testing       | 1. Choose either us dollar or Japanese yen and enter  the choice in integer (1 or 2)                                                                                                                                                               | If the user enter her currency exchange option in integer in 1 or 2, the currency exchange starts. If the user chooses us dollar, get the LTC price in us dollar and multiply with balance, and displays it. If the user chooses Japanese dollar, get the LTC price in Japanese dollar and multiply with balance, and displays it.                                                                                                  |
| Withdrawal                   | Unit testing       | 1. Choose withdrawal in menu (2). 2. Enter a description of the withdrawal. (house) 3. Enter the amount of the deposit. (200)                                                                                                                      | If the user enter description and the amount in integer, date, description, withdrawal(category), amount, balance is recorded in the user's own atm csv file. If the withdrawal system is successfully done, it displays "Saved" and shows the balance that the user currently has. Also, if the balance is bigger than 0, it displays "You're not debt", and if it is below 0, displays "You're debt"                              |
| Balance                      | Unit testing       | 1. Choose balance in menu (3).                                                                                                                                                                                                                     | By reading the user's own atm csv file, it displays the recent balance.                                                                                                                                                                                                                                                                                                                                                             |
| Transaction table            | Unit testing       | 1. Choose transaction table in menu (4).                                                                                                                                                                                                           | By readin the user's own atm csv file, it displays the table without index in markdown style.                                                                                                                                                                                                                                                                                                                                       |
| Chart                        | Unit testing       | 1. Choose chart in menu (5). 2. Choose deposit, withdrawal or balance and enter the option in number. (1 or 2 or 3).                                                                                                                               | If the number that the user entered is an integer and either 1, 2, or 3, it successfully moves to draw the chart. If the number is not fill the requirement above, the program ask the user to enter number again. Depending on the category the user choose, draws line graph which x_axis is date and y_axis is amount.                                                                                                           |
| Logout                       | Unit testing       | 1. Choose logout in menu (6). 2. Enter y or Y if the user wants to logout,  and enter n or N if the user wants to go back to the main menu.                                                                                                        | If the user doesn't enter y, Y, n, or N, the program asks user to enter the letter again. If the user enters y or Y, it displays "You logged out", exit the program by exit code(1).  If the user enter n or N, it displays the main menu.                                                                                                                                                                                          |
| Going back to Main Menu      | Integrated testing | 1. Enter the number depending on the menu the user chooses. (1 or 2 or 3 or 4 or 5 or 6) 2. Session successfully occurs. 3. Go back to the menu and the user enter the number depending on the menu the user chooses. (1 or 2 or 3 or 4 or 5 or 6) | If the thing that the user entered is an integer and either one of the numbers in menu, program move on to the session depending on the number the user chooses. After the session is done, set option_book as False go back to the code of the main menu, and displays the menu. If the user enter the option number correctly as following the above process, this code runs permanently  except when the user chooses to logout. |
| Overall review               | System testing     | 1. Open the pycharm and start the program. 2. Choose signup or login and follow the procedure above. 3. Choose one of the options from the main menu, go to that session, and follow the procedure above. 4. Choose logout. (y or Y)               | All of the output went through well, and there was no error or confusion during the program. If the user chooses to logout, the program ends successfully without any errors.                                                                                                                                                                                                                                                       |

# Criteria C: Development

## Signup System (Success Criteria 3)
My client requires a system to protect the private data. I thought about using a singup system to accomplish this requrement using if condition, for loop, while loop and the open command to work with csv file.


## Record of Tasks
  