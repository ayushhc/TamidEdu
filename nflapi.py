import requests
import tkinter as tk

# Define the NBA API endpoint
nba_api_endpoint = "https://www.balldontlie.io/api/v1/players"

def get_stats():
    # Get the input values from the user
    player_name = player_name_entry.get()

    # Define the parameters for the API call
    params = {
        "search": player_name,
        "per_page": 100,
    }

    # Make the API call
    response = requests.get(nba_api_endpoint, params=params)

    # Check if the API call was successful
    if response.status_code != 200:
        result_label.config(text="Error: Failed to retrieve data from NBA API.")
        return

    # Extract the player ID from the API response
    try:
        player_id = response.json()["data"][0]["id"]
    except (KeyError, IndexError):
        result_label.config(text="No results found.")
        return

    # Make the API call to get the player information
    response = requests.get(nba_api_endpoint + f"/{player_id}")

    # Check if the API call was successful
    if response.status_code != 200:
        result_label.config(text="Error: Failed to retrieve data from NBA API.")
        return

    # Extract the data from the API response
    try:
        data = response.json()
    except KeyError:
        result_label.config(text="No results found.")
        return

    # Display the data in the result label
    result_label.config(text=f"Name: {data['first_name']} {data['last_name']}\n")
    if "height_feet" in data and "height_inches" in data:
        total_inches = int(data["height_feet"]) * 12 + int(data["height_inches"])
        result_label.config(text=result_label.cget("text") + f"Height: {total_inches} in\n")
    else:
        result_label.config(text=result_label.cget("text") + "Height: Unknown\n")
    result_label.config(text=result_label.cget("text") + f"Weight: {data['weight_pounds']} lbs\n")
    result_label.config(text=result_label.cget("text") + f"Current Team: {data['team']['full_name']}\n")

# Create the GUI
window = tk.Tk()
window.title("NBA Player Information")

# Create the player name input field
player_name_label = tk.Label(window, text="Enter Player Name:")
player_name_label.pack()
player_name_entry = tk.Entry(window)
player_name_entry.pack()

# Create the button to get the stats
get_stats_button = tk.Button(window, text="Get Information", command=get_stats)
get_stats_button.pack()

# Create the label to display the results
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()