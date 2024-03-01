# Journaling App

## Description

The Journaling App is a Python-based desktop application designed to offer users a simple yet engaging platform to journal their daily experiences, feelings and activities. Developed with `tkinter`, this app stands out for its user-friendly interface, seamless navigation, and personalized journaling experience. It encourages users to reflect on their day, fostering a habit of mindfulness and self-awareness.

## Features

- **Daily Journaling**: Users can write about their day, including feelings, activities, and memorable moments.
- **Customizable Questions**: The app includes a set of questions to guide users in their journaling, which can be customized to fit their preferences.
- **Date-wise Entry Viewing**: Users can view past entries by selecting dates from a calendar, making it easy to reminisce about past days.
- **XP Tracking**: Engage with the app daily to earn XP points, adding a gamified element to your journaling routine.
- **Multi-page Layout**: Navigate smoothly between different sections of the app, including journaling, viewing past entries, and settings.

## Installation

To get started with the Journaling App, follow these simple steps:

1. Ensure you have Python installed on your system. Python 3.6 or higher is recommended.
2. Clone this repository or download the source code.
3. Install the required dependencies:

    ```bash
    pip install pandas r- requirements.txt
    ```

4. Navigate to the project directory and run the application:

    ```bash
    python app.py
    ```

## Usage

Upon launching the Journaling App, you'll be greeted with a simple interface asking how you're feeling today. You can navigate through the app using the menu options at the top.

- **To Journal**: Simply answer the questions presented on the screen. Your responses will be saved for future reflection. At the end of each journal entry you can choose between 3 personalized quests based on your input.
- **View Past Entries**: Use the calendar to select a date and view the journal entry for that day, along with all the responses you made that day in a comprehensive format.
- **Statistics**: This site gives you a comprehensive review about all your feelings in your last month but also your activity on the app.

## Contributing

Contributions to the Journaling App are welcome! Whether it's adding new features, fixing bugs, or improving the documentation, your help is appreciated. Please feel free to fork the repository and submit pull requests.

## Acknowledgments

This project incorporates ideas, code snippets, and solutions from various sources to enhance its functionality and user experience:

- Dynamic button creation in Tkinter was inspired by a solution on [Stack Overflow](https://stackoverflow.com/a/22290388), which allowed for flexible UI elements in the application.
- Date handling and formatting were guided by insights from another [Stack Overflow post](https://stackoverflow.com/questions/50625818/how-to-get-the-selected-date-for-dateentry-in-tkcalendar-python), crucial for managing journal entries by date.
- The method to iterate through entries and perform data analysis benefited from techniques discussed on [Stack Overflow](https://stackoverflow.com/a/3059362), enabling the app to generate user insights.
- Usage of the `isin` method in pandas for data filtering was informed by the [pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html), vital for analyzing journal entries' content.
- The approach to concatenate rows of DataFrames in pandas, avoiding duplicate indexing, was learned from [Saturn Cloud's blog](https://saturncloud.io/blog/how-to-concatenate-rows-of-two-dataframes-in-pandas/), which helped in compiling the journal entries efficiently.

Your shared knowledge and solutions have been invaluable.

## Project Status

This project is currently in MVP stage and thus only for demonstration purposes. Yet the basic structure is already ready for further improvements and extension: The code is built dynamically, so infinite questions and choices can be added without adding seperate functions. For actual usage, the data should be stored using an online detabase which is not the case in this demo product.
