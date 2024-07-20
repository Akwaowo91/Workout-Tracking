##  📖 Table Of Contents
- About
- How to Build
- Code explanation
- Feedback and Contributions
- Contacts

## 🚀 About
**Workoout-Tracker** This project is a Python script that uses the Nutritionix API to track exercises and log the details in a Google Sheet. The script takes user input for the exercise performed, fetches details like duration and calories burned, and logs the information into a Google Sheet using the Sheety API.

## 📝 How to Build
**To build the project follow these steps:**
  -  **installation:**
```shell
# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

# Ensure Git is installed
# Visit https://git-scm.com to download and install console Git if not already installed
            
# Clone the repository
git clone https://github.com/Akwaowo91/Workout-Tracking.git
cd Workout-Tracking

# Install the required package
pip install requests
```

## 📄 Code Explanation

  - **Run the script:**
      ```shell
        python main.py
      ```
  - **Input your exercise:**
      - When prompted, type the exercise you did (e.g., "ran 3 miles").
        
  - **View the result:**
      - The script will fetch the exercise details from the Nutritionix API and log them into the specified Google Sheet.
   
  - **Enviroment Variable**
      - The following environment variables must be set for the script to function correctly:
          - APP_ID: Your Nutritionix API Application ID.
          - APP_ID: Your Nutritionix API Application ID.
          - ADD_ROW_ENDPOINT: The Sheety API endpoint for adding rows to your Google Sheet.
          - TOKEN: The Bearer Token for the Sheety API.
            
  - **Api Endpoint**
      - Nutritionix Exercise Endpoint
          - URL: https://trackapi.nutritionix.com/v2/natural/exercise
          - Method: POST
          - **Headers:**
              - x-app-id: Your Nutritionix APP ID.
              - x-app-key: Your Nutritionix API Key.
              - x-remote-user-id: "0"
          - **Body:**
              - query: The exercise description.
              - gender: User's gender.
              - weight_kg: User's weight in kilograms.
              - height_cm: User's height in centimeters.
              - age: User's age.
  - **Sheety Add Row Endpoint**
      - URL: The Sheety API endpoint for adding rows to your Google Sheet.
      - Method: POST
      - Headers:
          - Authorization: Bearer YOUR_TOKEN
      - Body:
          - workout: JSON object containing the workout details (date, time, exercise name, duration, calories).

## 🤝 Feedback and Contributions
I have made every effort to implement all the main aspects of the Workout-Tracking project in the best possible way. However, the development journey doesn't end here, and your input is crucial for our continuous improvement.

> [!IMPORTANT]
> Whether you have feedback on features, have encountered any bugs, or have suggestions for enhancements, we're eager to hear from you. Your insights help us make the Workout-Tracking project more robust and user-friendly.

Please feel free to submit an issue or open an issue on this repository, if you have any feedback or suggestions.
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.
I appreciate your support and look forward to making this product even better with your help!

## ©️ Contact
For more questions you can reach me through:  
- email: akwaowoudokop15@gmail.com
- LinkedIn: https://www.linkedin.com/in/akwaowo-udokop-474662229/
