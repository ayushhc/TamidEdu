# Advik Nakirikanti
# Ayush Chintalapani

# NBA Statistics App

import pandas as pd
import requests
import tkinter as tk
pd.set_option('display.max_columns', None)
import time
import numpy as np




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NBA Statistics")
        self.geometry("400x300")

        # create widgets for main window
        self.label = tk.Label(self, text="NBA Information", font=("Arial", 24))
        self.nbaButton = tk.Button(self, text="NBA Stats", command=self.show_nba_screen, height=2, width=10, font=("Arial", 18))
        self.playerInfo = tk.Button(self, text="Player Info", command=self.show_player_info, height=2, width=10, font=("Arial", 18))

        # pack widgets for main window
        self.label.pack(side="top", pady=20, anchor="center")
        self.nbaButton.pack(side="top", pady=10, anchor="center")
        self.playerInfo.pack(side="top", pady=10, anchor="center")


    def nba_show_player(self, entry, result, num, title):

        nba_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2021-22&SeasonType=Regular%20Season&StatCategory=PTS"

        r = requests.get(url=nba_url).json()

        names = []
        points = []

        for player in r["resultSet"]["rowSet"]:
            names.append(player[2])
            points.append(player[num])

        player_name = entry.get()
        i = 0
        is_there = True
        for name in names:
            if (player_name == name):
                result.config(text=name + ": " + str(points[i]) + " " + title)
                is_there = False
            i = i + 1
        if(is_there):
            result.config(text="That player is not part of the top 50.")



    def show_nba_screen(self):
        # create new window for NBA screen
        nba_window = tk.Toplevel(self)
        nba_window.title("NBA Statistics")
        nba_window.geometry("400x370")
        
        label = tk.Label(nba_window, text="Enter Top 50 NBA Player Name:")
        entry = tk.Entry(nba_window)

        label.pack()
        entry.pack()


        # create widgets for NBA screen
        label = tk.Label(nba_window, text="Select A Statistic:")
        pts_button = tk.Button(nba_window, text="PTS", command=lambda: self.nba_show_player(entry, result, 23, "Points Per Game"))
        fgm_button = tk.Button(nba_window, text="FGM", command=lambda: self.nba_show_player(entry, result, 7, "Field Goals Made"))
        fga_button = tk.Button(nba_window, text="FGA", command=lambda: self.nba_show_player(entry, result, 8, "Field Goals Attempted"))
        fg_percentage_button = tk.Button(nba_window, text="MIN", command=lambda: self.nba_show_player(entry, result, 6, "Minutes"))
        three_pm_button = tk.Button(nba_window, text="3PM", command=lambda: self.nba_show_player(entry, result, 10, "Three Pointers Made"))

        # set font size for buttons
        button_font = ("TkDefaultFont", 14)

        # configure buttons
        pts_button.config(font=button_font)
        fgm_button.config(font=button_font)
        fga_button.config(font=button_font)
        fg_percentage_button.config(font=button_font)
        three_pm_button.config(font=button_font)

        # pack widgets for NBA screen
        label.pack(pady=10)
        pts_button.pack(pady=5)
        fgm_button.pack(pady=5)
        fga_button.pack(pady=5)
        fg_percentage_button.pack(pady=5)
        three_pm_button.pack(pady=5)


        result = tk.Label(nba_window, text="")
        result.config(font=("TkDefaultFont", 20))
        # pack widgets for NBA screen
        
        result.pack(pady = 20)

    def show_player_info(self):
        # create new window for NBA screen
        player_window = tk.Toplevel(self)
        player_window.title("Player Info")
        player_window.geometry("400x170")

        # Create the player name input field
        player_name_label = tk.Label(player_window, text="Enter NBA Player Name:")
        player_name_label.pack()
        player_name_entry = tk.Entry(player_window)
        player_name_entry.pack()

        # Create the label to display the results
        result_label = tk.Label(player_window, text="")
        

        # Create the button to get the stats
        get_stats_button = tk.Button(player_window, text="Get Information", command=lambda: self.get_stats(player_name_entry, result_label))
        get_stats_button.pack()

        result_label.pack()

        

    def get_stats(self, player_name_entry, result_label):
        
        # Define the NBA API endpoint
        nba_api_endpoint = "https://www.balldontlie.io/api/v1/players"
        
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
            result_label.config(text="No results found")
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

if __name__ == "__main__":
    app = App()
    app.mainloop()