import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

CHOICES = ['month', 'day', 'both', 'none']

def get_df():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input('Would you like to see data for Chicago, New York or Washington?\n')).lower().replace(' ', '_')
    try:
        city in CITY_DATA.keys()
    except ValueError:
        print('Please make a choice among Chicago, New York City or Washington.\n')
        get_filters()
    finally:
        filename = CITY_DATA[city]
        df = pd.read_csv(filename)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['Start hour'] = df['Start Time'].dt.hour
        df['Start month'] = df['Start Time'].dt.month
        df['Start day of week'] = df['Start Time'].dt.weekday_name

        return df, city


# TO DO: get user input for month (all, january, february, ... , june)
def get_month(df):
    month = str(input('Which month are you going to look at?\n')).lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if month != 'all':
        if month in months:
            month = months.index(month) + 1
            df = df[df['Start month'] == month]
        else:
            print('The input is not valid.')
            get_month(df)
    return df


# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
def get_day_of_week(df):
    day = str(input('Which day are you going to look at? (e.g., Monday)\n'))
    if day != 'all':
        df = df[df['Start day of week'] == day.title()]
    return df


def filter_with_month_or_day(df):
    choice = str(input('Would you like to filter the data by month, day, ' +
                       'both, or not at all? Type "none" for no time filter.\n')).lower()

    try:
        choice in CHOICES
    except ValueError:
        print('Please choose a word among month, day, both and none.')
    finally:
        if not choice == 'none':
            return choice





def time_stats(df, choice):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if choice != 'none':
        if choice == 'month':
            res, count = most_common_month(df)
            execution_time = time.time() - start_time
            print(res + ', Count: ' + str(count) + ', Filter: month')
            print('That took ' + str(execution_time) + ' seconds.')
        elif choice == 'day':
            res, count = most_common_day_of_week(df)
            execution_time = time.time() - start_time
            print(res + ', Count: ' + str(count) + ', Filter: day')
            print('That took ' + str(execution_time) + ' seconds.')
        elif choice == 'both':
            res, count = most_common_start_hour(df)
            execution_time = time.time() - start_time
            print(res + ', Count: ' + str(count) + ', Filter: month & day')
            print('That took ' + str(execution_time) + ' seconds.')


# TO DO: display the most common month
def most_common_month(df):
    common_month = str(df['Start month'].mode()[0])
    res = 'The most common month for selected city is: '
    res += common_month
    count = df['Start month'].value_counts(ascending=False).max()
    return res, count


# TO DO: display the most common day of week
def most_common_day_of_week(df):
    common_day_of_week = str(df['Start day of week'].mode()[0])
    res = 'The most common day of week for selected city is: '
    res += common_day_of_week
    count = df['Start day of week'].value_counts(ascending=False).max()
    return res, count

    # TO DO: display the most common start hour


def most_common_start_hour(df):
    common_start_hour = str(df['Start hour'].mode()[0])
    res = 'The most common start hour for selected city is: '
    res += common_start_hour
    count = df['Start hour'].value_counts(ascending=False).max()
    return res, count


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...')
    print('\nCalculating The Most Popular Stations...')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    count1 = df['Start Station'].value_counts(ascending=False).max()
    end_station = df['End Station'].mode()[0]
    count2 = df['End Station'].value_counts(ascending=False).max()
    print('Start station: ' + start_station + ', Count:' + str(count1) + ' - ' +
          'End station: ' + end_station + ', Count:' + str(count2))

    print("This took %s seconds." % (time.time() - start_time))
    print('\nCalculating The Most Popular Trip...')
    start_time = time.time()
    df['trip'] = df[['Start Station', 'End Station']].apply(lambda x: ' - '.join(x), axis=1)
    trip = df['trip'].mode()[0]
    count3 = df['trip'].value_counts(ascending=False).max()
    print('Trip: ' + trip + ', Count:' + str(count3))
    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('Calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Duration: ' + str(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Mean Duration: ' + str(df['Trip Duration'].mean()))

    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('Calculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df['User Type'].fillna('Unknown')
    for val, cnt in df['User Type'].value_counts().iteritems():
        print('There are {} {}s'.format(cnt, val))
    interval = time.time() - start_time
    print("This took {}s seconds." .format(interval))
    print()
    # TO DO: Display counts of gender
    if city == 'chicago' or city == 'new york city':
        start_time = time.time()
        for val, cnt in df['Gender'].value_counts().iteritems():
            print('There are {} {}s'.format(cnt, val))
        interval = time.time() - start_time
        print("This took {}s seconds.".format(interval))
        print()
        # TO DO: Display earliest, most recent, and most common year of birth
        start_time = time.time()
        print('The earliest year of birth: ' + str(int(df['Birth Year'].min())))
        print('The most recent year of birth: ' + str(int(df['Birth Year'].max())))
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('The most common year of birth: ' + str(int(most_common_birth_year)))
        interval = time.time() - start_time
        print("This took {}s seconds.".format(interval))
    else:
        print('The file does not contain gender and birth year information.')
    print('-' * 40)

def execution_code(df, choice, city_name):
    if choice == 'month':
        df = get_month(df)
    elif choice == 'day':
        df = get_day_of_week(df)
    elif choice == 'both':
        df = get_month(df)
        df = get_day_of_week(df)
    time_stats(df, choice)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df, city_name)


def main():
    while True:
        city_df, city_name = get_df()
        filter_method = filter_with_month_or_day(city_df)
        execution_code(city_df, filter_method, city_name)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
