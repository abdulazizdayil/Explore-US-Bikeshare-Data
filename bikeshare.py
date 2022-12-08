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
    
    
    city = input('\nWhich city would you like to filter by? New York City, Chicago or Washington?\n').lower()
    cities = ['chicago','new york city','washington']
    while city not in cities:     
        city = input('Please , Enter Valid City\n').lower()
        
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nWhich month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n").lower()
    months = ['january','february','march','april','may','june','all']
    while month not in months:     
        month = input('Please , Enter Valid Month\n').lower()
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day - monday, tuesday, wednesday, thursday, friday, all , saturday, or sunday?\n').lower()
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while day not in days:     
        day = input('Please , Enter Valid Day\n').lower()
        
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    dc = df  
    dc['month'] = dc['Start Time'].dt.month
    common_month = dc['month'].value_counts().idxmax()
    print('Most Frequent Month:', common_month)
          
    
    

    
    # TO DO: display the most common day of week

    dc['day_of_week'] = dc['Start Time'].dt.day_name()  
    common_day = dc['day_of_week'].value_counts().idxmax()
    print('Most Frequent Day:', common_day)
    # TO DO: display the most common start hour
   
    dc['hour'] = dc['Start Time'].dt.hour
    common_hour = dc['hour'].value_counts().idxmax()  
    print('Most Frequent Start Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    dc = df
    common_start_station = dc['Start Station'].value_counts().idxmax() 
    print('Most Frequent Start Station:', common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = dc['End Station'].value_counts().idxmax() 
    print('Most Frequent End Station:', common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip

    common_start_end_stations = dc['Start Station'].str.cat(dc['End Station'], sep=' to ')
    print('Most Frequent Start and End Stations:', common_start_end_stations.value_counts().idxmax())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    dc = df
    total_travel_time= dc['Trip Duration'].sum()
    print('Total Travel Time :', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time= dc['Trip Duration'].mean()
    print('Mean Travel Time :', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    dc = df
    user_type=dc['User Type'].value_counts()
    print('Counts Of User Types', user_type)
    # TO DO: Display counts of gender
    
    if 'Gender' and 'Birth Year' in dc.columns:
        gender=dc['Gender'].value_counts()
        print('Counts Of Gender', gender)
        # TO DO: Display earliest, most recent, and most common year of birth
        birth_year=dc['Birth Year'].value_counts().idxmax()
    
        print('Earliest Year Of Birth :', dc['Birth Year'].min())
        print('Most Recent Year Of Birth :', dc['Birth Year'].max())
        print('Most Common Year Of Birth',birth_year)
     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n").lower()
    start_loc = 0
    end_loc = 5
    while (view_data=='yes'):
        print(df.iloc[start_loc:end_loc])
        start_loc += 5
        end_loc += 5
        view_data = input("Do you wish to continue?: \n").lower()
    
    
    
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()