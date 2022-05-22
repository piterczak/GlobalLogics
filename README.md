To run the project download GIT Repository to your local machine
Navigate to the directory with downloaded repository
Go to GlobalLogics directory

Run the CMD and navigate to directory "...(directory where you downloaded the repository)/GlobalLogics"
Now navigate to ".../GlobalLogics/venv/Scripts/"
Type in CMD "activate" to start the virtual enviroment with all the packages required to run the project
Go back to ".../GlobalLogics/"
Type in CMD "uvicorn main:shop" to start the web server of the project!

Now if earlier steps were done properly, we have our server up and running on localhost. You can check it by typing
in your web-browser address "127.0.0.1:8000/"

Now to access the shop, go to file browser, navigate to directory with downloaded repository, then to folder GlobalLogics 
Run the interface.py file

It shall show console with application's main menu that asks the user to provide number defying which option to choose.

Type in console 1 to view products in shop and their current number

Type in console 2 to buy a product. It will ask you to provide the product name (Case sensitive!) so it's better to check with option 1 what do we have in the shop before deciding what to buy! 
Then it'll ask you to provide the ammount of the product that you'd like to buy.

Type in console 3 to close the application.