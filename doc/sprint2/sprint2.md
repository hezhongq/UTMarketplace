# Sprint Goal

The goal for this sprint is to complete the epics listed in the Sprint 2 backlog. For the backend, user interaction with the website is of top priority. Most of the frontend framework is already complete. At the end of this sprint, users will be able to use basic functionalities of UTMarketplace such as creating, editing, and searching for listings, while being able to edit their profile.

# Spikes

How to create and be able to browse listing dynamically
How to let users choose courses and have recommendations upon chosen courses
How to have editing features for the user
How to verify user emails with the utoronto database

# Team capacity

Since we are not working with 8 hour days, as a team we decided to complete 41 user stories for sprint 2 which will allow for the main user interaction with the website to work, and we decided that we have no more than 45 user stories in a single sprint. We also have documentation to complete during sprint 2.

# Participants

Chris
Joshua
Renfrew
Andrew
Tin
Eric
Arush

# Decisions & User Stories & Subtasks
As a team, we decided to all work together on the backend components of having a user being able used to have an account that is authenticated and being able to create listings and edit their account. Through this decision, we then decided which tasks from the backlog to include into sprint 2, while making sure the work was doable within the time frame of sprint 2.

**(UT-11)** - As an admin, verify the emails that the users register with
* **(UT-34)** Make a server address to send emails
* **(UT-54)** Check the existence of the email in the database
* **(UT-72)** Make a code schema to store the verify code
* **(UT-73)**   Create active pages for user
* **(UT-74)** Link sending emails and register actions.

**(UT-24)** - As a user, I want to be able to make a listing
* **(UT-38)** Create a category class
* **(UT-39)** Store information of listing created
* **(UT-61)**  Organize and format listing page
* **(UT-62)** Create Listing and Category table in database
* **(UT-65)** Create category page that displays and navigates to different subjects
* **(UT-66)** Create inner listing page that shows all listings in that subject

**(UT-7)** - As a user, I want to be able to browse categories

**(UT-10)** - As a user, I want to search for listings

**(UT-26)** - As a user, I want to be able to update my listing
* **(UT-33)** Update the database
* **(UT-36)** Update the listing in the category
* **(UT-51)** Make listing page dynamic
* **(UT-78)** Make database responsive when user makes actions in html page

**(UT-75)** - As a user, I want to be able to choose courses
* **(UT-76)**  I want to be able to customize my courses
* **(UT-80)** Add courses to database
* **(UT-81)** Change courses in the database and reflect on website

**(UT-16)** - As a user, I want to be able to delete my account
* **(UT-29)** Remove emails, password from specified user
* **(UT-30)** The user's postings should not show up after they delete their account
* **(UT-35)** Add visuals to the delete account function (ex. button on user's setting page) which starts the delete process

**(UT-15)** - As a user, I want to be able to bookmark listing for future use

**(UT-3)** - As a user, I want to be able to sort listings based on settings

**(UT-5)** - As a user, I want to be able to have courses recommended to me
* **(UT-83)** Sort courses based by user's selected courses
* **(UT-84)** Dynamically change recommendation as courses are changed or dropped

**(UT-4)** - As a user, I want to be able to update my password
* **(UT-12)** Update information in the database
* **(UT-42)** Validate old password before updating
* **(UT-82)** Have a visual page for the information

**(UT-20)** - As a user, I want to be have and customize my profile picture
* **(UT-55)** Create a profile page
* **(UT-85)** Save profile picture to database
* **(UT-86)** Update html template with new profile image
