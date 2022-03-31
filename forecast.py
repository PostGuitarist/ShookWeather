import requests
import calendar
import time

api_key = 'FORECAST_API_KEY'
api_call = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key + '&zip=ZIP_KEY'

running = True

print('-------------------------------------------------------------------')
print('| Shook\'s Weather Forecast Application Using OpenWeatherMap\'s API |')
print('-------------------------------------------------------------------')

time.sleep(3)

# Program loop
while running:

    # Asks the user for the city or zip code to be queried
    while True:
      api_call += '&zip=' 
      break

    # Stores the Json response
    json_data = requests.get(api_call).json()

    location_data = {
        'city': json_data['city']['name'],
        'country': json_data['city']['country']
    }

    print('\n{city}, {country}'.format(**location_data))

    # The current date we are iterating through
    current_date = ''

    # Iterates through the array of dictionaries named list in json_data
    for item in json_data['list']:

        # Time of the weather data received, partitioned into 3 hour blocks
        time = item['dt_txt']

        # Split the time into date and hour [2018-04-15 06:00:00]
        next_date, hour = time.split(' ')

        # Stores the current date and prints it once
        if current_date != next_date:
            current_date = next_date
            year, month, day = current_date.split('-')
            date = {'y': year, 'm': month, 'd': day}
            print('\n{m}/{d}/{y}'.format(**date))
        
        # Grabs the first 2 integers from our HH:MM:SS string to get the hours
        hour = int(hour[:2])

        # Sets the AM (ante meridiem) or PM (post meridiem) period
        if hour < 12:
            if hour == 0:
                hour = 12
            meridiem = 'AM'
        else:
            if hour > 12:
                hour -= 12
            meridiem = 'PM'

        # Prints the hours [HH:MM AM/PM]
        print('\n%i:00 %s' % (hour, meridiem))

        # Temperature is measured in Kelvin
        temperature = item['main']['temp']

        # Weather condition
        description = item['weather'][0]['description'],

        # Prints the description as well as the temperature in Celcius and Farenheit
        print('Weather condition: %s' % description)
        print('Farenheit: %.2f' % (temperature * 9/5 - 459.67))

    # Prints a calendar of the current month
    calendar = calendar.month(int(year), int(month))
    print('\n'+ calendar)

    # Asks the user if he/she wants to exit
    while True:
        print('-------------------------------------------------------------------')
        print('| Shook\'s Current Weather Application Using OpenWeatherMap\'s API  |')
        print('-------------------------------------------------------------------')
        running = False
        break

