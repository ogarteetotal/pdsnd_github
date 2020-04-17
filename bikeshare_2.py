import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! I am OGAR JOSEPH  ODAMA. Let\'s explore some US bikeshare data!')
    print()
    
    #enter your name to start
    user_name = input('Please enter your name: ')
    print('Welcome {} to US bikeshare data analysis!'.format(user_name.title()))
    print()

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please, enter any of the 3 cities (Chicago, New York or Washington) you want to analyze: ').lower()
    while city not in cities:
        print('Please, enter a valid city')
        city = input('Please, enter the correct input: ').lower()
        print()

    # get user input for month (all, january, february, ... , june)
    month = input('Enter any of the following month (all, january, february, ... , june): ').lower()
    while month not in months:
        print('Please,enter the a valid month')
        month = input('Please, enter the correct input: ').lower()
        print()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day of week (all, monday, tuesday, ... sunday): ').lower()
    while day not in days:
        print('Please, enter a vaild day')
        day = input('Please, enter the correct input: ').lower()
        print()
    
        return city, month, day

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
    # Loading US bikeshare data into a pandas DataFrame

    df = pd.read_csv(CITY_DATA[city])

    # Converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month,:]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print()
    
    # display the most common month
    print('The most common month is: {}'.format(df['month'].mode().values[0]))
       
    print()
    
    # display the most common day of week
    print('The most common day of the week: {}'.format(
        str(df['day_of_week'].mode().values[0]))
    )
    print()

    # display the most common start hour
    df['common_start_hour'] = df['Start Time'].dt.hour
    print('The most common start hour: {}'.format(
        str(df['common_start_hour'].mode().values[0]))
    )
    print()
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common start station is: {}'.format(df['Start Station'].mode().values[0]))

    # display most commonly used end station
    print('The most common end station is: {}'.format(df['End Station'].mode().values[0]))

    # display most frequent combination of start station and end station trip
    df['most frequent combined trip'] = df['Start Station']+ " " + df['End Station']
    print("The most frequent combined start and end station trip is: {}".format(df['most frequent combined trip'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['total travel time'] = df['End Time'] - df['Start Time']
    print('The Total Travel Time is: {}'.format(str(df['total travel time'].sum())))

    # display mean travel time
    print('The Mean Travel Time is: {}'.format(str(df['total travel time'].mean())))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print(' The counts of user types is: ', counts_user_types)
    print()
    # Display counts of gender
    counts_gender = df['Gender'].value_counts()
    print('The counts of gender is: ', counts_gender)
    print()

    # Display earliest, most recent, and most common year of birth
    print("The earliest birth year is: {}".format(str(int(df['Birth Year'].min()))))
    print("The most recent year of birth is: {}".format(str(int(df['Birth Year'].max()))))
    print("The most common year of birth is: {}".format(str(int(df['Birth Year'].mode().values[0]))))
        
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_raw_data(df):
    '''
    Show csv file by prompting users 
    whether they would like want to see the raw data    
    '''
    # Display raw data to users that would like to see it
    start_raw_data = 0
    end_raw_data = 5

    raw_data = input('Do you like  to see the raw data? Enter yes or no. \n').lower()
    if raw_data.lower() == 'yes':
        while end_raw_data <= df.shape[0] - 1:

            print(df.iloc[start_raw_data:end_raw_data,:])
            start_raw_data += 5
            end_raw_data += 5

            continue_prompting_user = input('Would you like to see 5 more rows of raw data? Enter yes or no.\n ').lower()
            if continue_prompting_user.lower() == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
