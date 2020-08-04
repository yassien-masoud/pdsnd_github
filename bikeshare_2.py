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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago','new york city','washington']
    city=input("please enter the city").lower()
    while city not in cities:
         city=input("please enter the city").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months={'january':1, 'february':2,'march':3,'april':4,'may':5,'june':6}
    month=input("please enter which month").lower()
    month = months[month]
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days={'monday': 1,'tusday': 2,'wensday':3,'thursday':4,'friday':5,'saturday':6,'sunday':7}
    day=input("please enter the day").lower()
    day =days[day]
    
        
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
    
    df=pd.read_csv(CITY_DATA[city])
    
    # convert Start Time to datetime value
    df['Start Time']= pd.to_datetime(df['Start Time'])
    
    # filter by month
    df['month']=df['Start Time'].dt.month
    df = df[df['month'] == month]
    #filter by day
    df['day']=df['Start Time'].dt.day
    df = df[df['day'] == day]
    print(df)
    

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    month_frequent= df['month'].mode()[0]
    print("The most common month is {}".format(month_frequent))

    # TO DO: display the most common day of week
    day_frequent= df['day'].mode()[0]
    print("The most common day is {}".format(day_frequent))

    # TO DO: display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    hour_frequent= df['hour'].mode()[0]
    print("The most common hour is {}".format(hour_frequent))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].value_counts()
    print("most_common_start_station is: \n{}".format(most_common_start_station))
    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].value_counts()
    print("\nmost_common_end_station is: \n{}".format(most_common_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station=df[['Start Station','End Station']].mode().loc[0]
    print("\nmost_common_start_end_station is: \n{}".format(most_common_start_end_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_ttavel=df['Trip Duration'].sum()
    print(total_ttavel)

    # TO DO: display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print(mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("These are the counts of each user type:\n{}".format(df['User Type'].value_counts()))

    # Display counts of gender
    try:
        print("\nThese are the counts of each user's gender:\n{}".format(df['Gender'].value_counts()))
    except:
        print("\nThe data set for the city you have selected does not have Gender data.")

    # Display earliest, most recent, and most common year of birth
    try:
        year = df['Birth Year']
        print("\nThe earliest birth year is: {}".format(year.min()))
        print("\nThe most recent birth year is: {}".format(year.max()))
        print("\nThe most common birth year is: {}".format(year.value_counts().idxmax()))
    except:
        print("\nThe data set for the city you have selected does not have Birth Year data.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
main()
