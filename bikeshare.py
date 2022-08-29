import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new York City': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWould you like to see data for New York City, Chicago or Washington?\n"').lower()
        if city.lower() not in ('new York City', 'chicago', 'washington'):
            print("wrong choice,Please enter the name of the city again ")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWhich month would you like to filter by? January, February, March, April, May, June or type 'all' for all days?\n").lower()
        if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("wrong choice,Please enter the month again.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nWhich day would you like to filter by? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' for all days.\n").lower()
      if day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("wrong choice,Please enter the day again.")
        continue
      else:
        break

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Commonly start station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost Commonly end station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combnation= df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', popular_start_station, " and ",
          popular_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time:', total_travel_time,"Seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('average travel time:', mean_travel_time , "Seconds")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('\ncounts of each user type:\n',counts_of_user_types)
    # TO DO: Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print('\ncounts of each gender:\n',counts_of_gender)
    except :
        print("\ncounts of gender only available for New York City and Chicago.")
        # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        print('\nearliest year:', earliest)
    except:
        print("\nealiest year of birth only available for New York City and Chicago.")
    try:
        most_recent = df['Birth Year'].max()
        print('\nmost recent year:', most_recent)
    except:
        print("\nmost recent year of birth only available for New York City and Chicago.")
    try:
        common_year = df['Birth Year'].mode()[0]
        print('\nmost common year:', common_year)
    except:
        print("\nmost common year of birth only available for New York City and Chicago.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    data_row= 0 
    while True:
        raw = input('\nWould you like to see some raw data? yes or no.\n')
        if raw.lower() not in ('yes','no'):
            print('\nwrong choice,Please enter choice again.\n')
            continue
        else:
            if raw.lower() == 'yes':
                print(df[data_row:data_row+5])
                data_row+=5
            else:
                break 
         
            
        
    
  
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
