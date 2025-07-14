import re
import pandas as pd

def preprocess(data):
    # Regex pattern to extract datetime entries like "29/06/25, 08:58 -"
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    # Extract messages and corresponding dates
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    # Create a DataFrame with extracted messages and dates
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Remove trailing ' - ' and convert to datetime (with 2-digit year support)
    df['message_date'] = pd.to_datetime(df['message_date'].str.strip().str.replace(' -', '', regex=False), format='%d/%m/%y, %H:%M')

    # Rename column
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Separate user and message
    users = []
    cleaned_messages = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if len(entry) > 2:
            users.append(entry[1])
            cleaned_messages.append("".join(entry[2:]))
        else:
            users.append('group_notification')
            cleaned_messages.append(entry[0])

    # Add to DataFrame
    df['user'] = users
    df['message'] = cleaned_messages
    df.drop(columns=['user_message'], inplace=True)

    # Date and time features
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # Time period bucket (e.g. 23-00, 0-1)
    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append('23-00')
        elif hour == 0:
            period.append('00-1')
        else:
            period.append(f'{hour}-{hour+1}')
    df['period'] = period

    return df
