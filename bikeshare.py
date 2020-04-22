import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july','all']
    valid_cities = ['washington', 'new york city', 'chicago']
    valid_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            while True:
                city = str(input('Please enter which city you are interested in: Chicago, New York City or Washington?\n')).lower()
                month = str(input('Please choose a month, if you want to see all months, insert "all"\n')).lower()
                day = str(input('Please choose a day, if you want to see all days, insert "all"\n')).lower()
                if city in valid_cities and month in valid_months and day in valid_days:
                    break
                else:
                    print('Unfortunately, your inputs were not valid, please try again')
                    continue
        except ValueError:
            print("Sorry, we did not understand your input. Please try again :)")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    popular_month = df['Start Time'].dt.month.mode()[0]
    print('Most frequent month:', popular_month)

    #TO DO: display the most common day of week
    popular_day = df['Start Time'].dt.day.mode()[0]
    print('Most frequent day:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most frequent hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_stat = df['Start Station'].mode()[0]
    print('The most popular Start Station is:\n ',start_stat)
    # TO DO: display most commonly used end station
    end_stat = df['End Station'].mode()[0]
    print('The most popular End Station is:\n ',end_stat)
    # TO DO: display most frequent combination of start station and end station trip
    trip_stat = df['Start Station']+df['End Station']
    pop_trip = trip_stat.mode()[0]
    print('The most popular trip is between:\n ', pop_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip = df['Trip Duration'].sum()
    print('The total time amount of trips in minutes is:\n ', total_trip)
    # TO DO: display mean travel time
    mean_trip = df['Trip Duration'].mean()
    print('The mean travel time of a trip in minutes is:\n ', mean_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Our customers are distributed among the following User Types: \n", user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(" The gender distribution is as follows:\n ", gender)
    else:
        print("Sorry, the Gender Data is missing.\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
        print("The most common Birth Year is:\n", int(birth_year.mode()[0]))
        print("The earliest Birth Year is\n", int(birth_year.min()))
        print("The most recent Birth Year is\n", int(birth_year.max()))
    else:
        print("Sorry, the Birth Date Data in is missing.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw(df):
    """Displays 5 lines of the raw data of the current dataframe upon user request"""
    index=0
    raw_check = input('\nWould you like to see the raw data? Enter yes or no.\n')
    while True:
        if raw_check.lower() != 'yes':
            break
        print(df.iloc[index:index+5])
        index +=5
        raw_check = input('\nWould you like to see more raw data? Enter yes or no.\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
