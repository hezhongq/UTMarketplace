# Sprint Goal

The goal for this sprint is to complete the epics listed in the Sprint 1 backlog. For the backend, creation of accounts and authentication is the top priority for this sprint. For the frontend, creating a responsive webpage and login form is the top priority for this sprint. At the end of this sprint, users will be able to log in into UTMarketplace and log out.

# Spikes

How to authenticate a University of Toronto student
How to authenticate an administrator user
How to encrypt user information properly
How to have a bot email account that is used to reset user password

# Team capacity

Since we are not working with 8 hour days, as a team we decided to complete 26 user stories for sprint 1 which will allow for the account creation and authentication to work, and we decided that we have no more than 45 user stories in a single sprint. We also have documentation to complete during sprint 1.

# Participants

* Chris
* Joshua
* Renfrew
* Andrew
* Tin
* Eric
* Arush

# Decisions & User Stories & Subtasks
As a team, we decided to work on the frontend and backend components of having a user being able to log into UTMarketplace and making sure that their account is authenticated on creation. Through this decision, we then decided which tasks from the backlog to include into sprint 1, while making sure the work was doable within the timeframe of sprint 1.

**(UT-1)** - As a user, I want to create an account to access UTMarketplace
* **(UT-43)** Implement a page on the website where a user can enter their information.
* **(UT-45)** Ensure that when the form is filled out with correct information, the user gets added to the database and a user object is made.

**(UT-11)** - As an admin, I want to verify the emails that the users register with
* **(UT-34)** Make a server address to send emails
* **(UT-54)** Check if the email already exists in the database

**(UT-2)** - As a user, I want to be able to log into UTMarketplace
* **(UT-50)** Create a visually pleasing login form that provides security and authentication when providing credentials to the site

**(UT-6)** - As a user, I want to be able to log out of UTMarketplace
* **(UT-47)** Create button to allow user to logout
* ** (UT-53)** After logout prevent current session to edit user settings and posts

**(UT-8)** - As an admin, I want to ensure all new accounts are unique
* **(UT-49)** Notify user if account is unique or not

**(UT-18)** - As a user, I want to be able to reset my password if forgotten
* **(UT-44)** Make sure that the password entered by the user is same for both new password and re-entered password
* **(UT-48)** Store the new password in the database by associating it with the use email.
* **(UT-51)** Make a button for users to click when they forget their password, and send the reset password email to the user

**(UT-4)** - As a user, I want to be able to update my password regardless if I forgot it or not
* **(UT-41)** Change the database password stored for user
* **(UT-52)** Enter old password to validate it really is the user, then allow for password change

**(UT-16)** - As a user, I want to be able to delete my account
* **(UT-29)** Remove emails, password from specified user
* **(UT-30)** The user's postings should not show up after they delete their account
* **(UT-35)** Add visuals to the delete account function (ex. button on user's setting page) which starts the delete process
