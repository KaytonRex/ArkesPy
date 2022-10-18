# Welcome to ArkesPy!

Arkes was first developed as a way to automate a large workflow where 2 hours of checking email attachments, seeing if there are any errors, then logging them, just became too tedious!

Within this project, we will hopefully be able to do the below:
- **Keys** - Utilising JSON, we will be creating a key that we can use to compare emails, and find an output e.g. From Address - Subject, if this matches, utilise the client name as the ID.
- **Exchange** - We will be connecting to Exchange both on-premises and on the cloud. This will then download the attachments.
- **Storage** - With the email attachments, we will offer both a file store solution for storing, or the conversion into a SQL Database.
- **Future** - Later we will look at adding a reporting aspect which is user friendly. This may be hard coded to start with.



# To-Do List
To do the above, I will need to learn the below:
- **Services** - How will this script run automatically e.g. Windows Service Integration or Windows Scheduled Tasks?
- **JSON** - How to import and export JSON files and create usable variables
- **SQL** - How to connect to SQL databases, change database structures and tables. Including how to insert into tables
- **Exchange EWS** - How to access the API and find emails and download attachments
- **Security** - Are there any security aspects I need to be concerned about