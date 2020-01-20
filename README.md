# simpleweather
Python script to return only the current outside temperature from the OpenWeatherMap API.

Created for use with things like <a href="https://goodies.xfce.org/projects/panel-plugins/xfce4-genmon-plugin">Genmon</a> in XFCE to display the temperature in your taskbar.

# Getting Started
1. To get started, you'll need your own OpenWeatherMap API key. To obtain an OpenWeatherMap API key, see this page: https://openweathermap.org/appid
2. Once you have an API key, edit simpleweather.py and insert your API key between the single quotation marks on the 8th line.
3. Change the zipcode on line 9 to your location.
4. OPTIONAL: By default, the script returns the temperature in fahrenheit. If you'd like the temperature in celsius, change 'imperial' on line 12 of simpleweather.py to 'metric'.

To test the script from a Linux terminal:

```
chmod +x simpleweather.py
./simpleweather.py
```
(The chmod step only needs to be done once to make the file executable.)


Or by calling Python directly:
```
python simpleweather.py
```

If everything worked, the script should just return the current temperature on a single line.

To avoid Python errors showing up on your taskbar when you don't have an internet connection, the script simply returns "--°" if it is unable to retrieve the temperature for whatever reason. If you get this when your internet connection is working, double check that your API key is formatted properly (it should be 32 characters long), and be aware that it may take OpenWeatherMap several hours to activate your API key after first signing up.

# Setting up with Genmon on XFCE
1. Add a new item to your XFCE panel and select "Generic Monitor".
2. Right click the new item on the panel and go to Properties.
3. Enter the full path of the script in the "Command" field, and change the update period to at least 600 seconds (10 minutes).
..*This is due to the fact that OpenWeatherMap only updates their weather data once every 10 minutes at the absolute minimum. I personally set mine to 1800 seconds. (30 minutes)

![screenshot](https://user-images.githubusercontent.com/59930698/72713964-ee93e300-3b3b-11ea-8221-d908fc748e27.png)
