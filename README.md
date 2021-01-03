Task 1:

Get the users and their followers in the CSV format:

To get the list of users https://api.github.com/users
Get the list of user Ids divisible by 10 -
Iterate the result and get the user details https://api.github.com/users/{login}
Get the followers list for that user https://api.github.com/users/{login}/followers
Create a virtual environment for this project.
Create a functions and convert into json format.
And using loop for user id divisible by 10.
Convert the data into CSV file.




Task 2:

Created credentials for google drive api.


Go to APIs Console and make your own project.
Search for ‘Google Drive API’, select the entry, and click ‘Enable’.
Select Credentials from the left menu, click Create Credentials, select ‘OAuth client ID’.
Now, the product name and consent screen need to be set. 
click ‘Configure consent screen’.
Select ‘Application type’ to be Web application.
Enter an appropriate name.
Click ‘Save’.
Click ‘Download JSON’ on the right side of Client ID to download.
The downloaded file has all authentication information of your application. 
Rename the file to “webclient.json” and place it in your working directory.
