# Import the required libraries
import speech_recognition as sr  # For speech recognition
import pyttsx3  # For text-to-speech conversion
import datetime  # For handling date and time
import webbrowser  # For performing web searches

# Initialize the recognizer (for recognizing the speech) and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Process the text and speak it out loud

# Function to listen for voice commands
def listen():
    with sr.Microphone() as source:  # Use the default microphone as the audio source
        print("Listening...")  # Print a message to indicate that the assistant is listening
        audio = recognizer.listen(source)  # Listen for the first phrase and extract it into audio data
        try:
            command = recognizer.recognize_google(audio).lower()  # Use Google's speech recognition
            print(f"You said: {command}")  # Print what the user said
            return command  # Return the recognized command
        except sr.UnknownValueError:  # Error handling for unknown words
            speak("Sorry, I did not understand that.")  # Inform the user that the speech was not understood
            return "None"  # Return None if nothing was understood
        except sr.RequestError:  # Error handling for recognizer not connected
            speak("Sorry, my speech service is down.")  # Inform the user that the speech service is down
            return "None"  # Return None if the service is down

# Function to respond to greetings
def greet(command):
    if 'hello' in command:  # Check if the word 'hello' is in the command
        speak("Hello! How can I assist you today?")  # Respond with a greeting

# Function to tell the current time
def tell_time(command):
    if 'time' in command:  # Check if the word 'time' is in the command
        now = datetime.datetime.now()  # Get the current time
        current_time = now.strftime("%H:%M")  # Format the time as hour:minute
        speak(f"The current time is {current_time}")  # Tell the current time

# Function to tell the current date
def tell_date(command):
    if 'date' in command:  # Check if the word 'date' is in the command
        today = datetime.date.today()  # Get the current date
        current_date = today.strftime("%B %d, %Y")  # Format the date as Month day, Year
        speak(f"Today's date is {current_date}")  # Tell the current date

# Function to perform a web search
def web_search(command):
    if 'search' in command:  # Check if the word 'search' is in the command
        speak("What do you want to search for?")  # Ask the user what they want to search for
        query = listen()  # Listen for the user's response
        if query != "None":  # Check if a query was recognized
            url = f"https://www.google.com/search?q={query}"  # Create a URL for the search query
            webbrowser.open(url)  # Open the URL in the web browser
            speak(f"I have found some information about {query}")  # Inform the user that information has been found

# Main function to run the voice assistant
def main():
    speak("Welcome to the voice assistant. Please say something!")  # Greet the user
    while True:  # Loop to continuously listen for commands
        command = listen()  # Listen for a command
        if command != "None":  # Check if a command was recognized
            greet(command)  # Respond to greetings
            tell_time(command)  # Tell the time
            tell_date(command)  # Tell the date
            web_search(command)  # Perform a web search
        if 'exit' in command:  # Check if the user wants to exit
            speak("Goodbye!")  # Say goodbye
            break  # Break the loop to exit the program

# Check if the script is the main program and run it
if __name__ == "__main__":
    main()  # Call the main function
