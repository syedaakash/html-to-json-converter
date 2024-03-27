Project Setup Guide

## Step 1: Requirements

Ensure you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

## Step 2: Clone the Repository

Clone the project repository from the GitHub repository to your local machine.

Quick Steps to Clone a Repo:

Install Git: Make sure Git is installed on your computer. You can download it from [git-scm.com](https://git-scm.com/).

Copy the Repo URL: Get the URL of the repository you wish to clone. This is usually found on the repository's page on platforms like GitHub, under a button labeled "Clone or download".

Open Terminal or Command Prompt:
Windows: Open Command Prompt or PowerShell.
Mac/Linux: Open Terminal.

Navigate to Target Directory:
Use cd to move to the directory where you want the cloned repo to reside.
cd path/to/your/folder
Clone the Repository: 

Run the clone command with the copied URL.
git clone https://github.com/username/repository-name.git

Enter the Repo Directory: Change into the newly created directory.
cd repository-name

## Step 3: Install Dependencies

Open a terminal or command prompt and navigate to the project directory.
Run the following command to install the necessary dependencies:
pip install Flask beautifulsoup4

## Step 4: Run the Application

In the terminal or command prompt, navigate to the project directory.
Run the following command to start the Flask application:
python app.py
Open a web browser and go to http://127.0.0.1:5000 to access the application.

## Step 5: Usage

Once the application is running, you will see a button labeled "Convert HTML to JSON".
Click the button to start the conversion process. The application will automatically convert all HTML files inside the json directory to JSON format.
You will see a loader icon indicating that the conversion process is ongoing. Once the conversion is complete, a success message will be displayed.

## Step 6: Access the Generated JSON Files

After the conversion process is complete, you can find the generated JSON files in the json directory within the project.