<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>
    <h1>Workout Tracking Application</h1>
    <p>The Workout Tracking Application is a Python script that helps users track their exercises and calories burned by integrating with the Nutritionix API and storing data using the Sheety API.</p>

  <h2>Features</h2>
    <ul>
        <li><strong>Exercise Tracking:</strong> Users can input their exercise details, including type and duration.</li>
        <li><strong>Calorie Calculation:</strong> The application calculates the calories burned based on the user's input and physical attributes like weight, height, age, and gender.</li>
        <li><strong>API Integration:</strong> Utilizes the Nutritionix API to retrieve exercise details and the Sheety API to store workout data.</li>
        <li><strong>Dynamic Date and Time:</strong> Automatically records the current date and time for each exercise entry.</li>
    </ul>

  <h2>Usage</h2>
    <ol>
        <li><strong>API Credentials:</strong> Obtain the Nutritionix API credentials (App ID and API Key) and Sheety API endpoint URL.</li>
        <li><strong>User Input:</strong> Input the exercise details when prompted, including the type of exercise.</li>
        <li><strong>Data Processing:</strong> The application sends a request to the Nutritionix API with the provided exercise details and retrieves the calorie information.</li>
        <li><strong>Data Storage:</strong> The exercise data, including date, time, exercise type, duration, and calories burned, is stored using the Sheety API.</li>
    </ol>

  <h2>Requirements</h2>
    <ul>
        <li>Python</li>
        <li>Requests library</li>
    </ul>

  <h2>License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a>. See the LICENSE file for details.</p>

   <h2>Author</h2>
    <p>Created by Kush Kokate. For inquiries and feedback, please contact kokatekush@gmail.com.</p>
</body>
</html>
