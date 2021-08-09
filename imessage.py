import sqlite3
import pandas as pd

# find your chat.db and establish a connection
# Insert path where chat db is located ie. ../chat.db
path = ''
conn = sqlite3.connect(path)
cur = conn.cursor()

# Fetching all messages
messages_df = pd.read_sql_query('SELECT * FROM message WHERE handle_id = 1', conn)
processed_df = messages_df[['is_from_me', 'text']]

file = open('texts.txt', 'w')

# Looping through and dropping reaction messages and labeling messages
for i in range(0, 2933):
    if not(' “' in str(processed_df['text'][i]) and ('Emphasized' in str(processed_df['text'][i]) or \
           'Loved' in str(processed_df['text'][i]) or 'Laughed' in str(processed_df['text'][i]) or \
           'Liked' in str(processed_df['text'][i]) or 'Disliked' in str(processed_df['text'][i]))):
        if str(processed_df['is_from_me'][i]) == '1':
            name = 'Me'
        elif str(processed_df['is_from_me'][i]) == '0':
            name = 'You'
        else:
            name = processed_df['is_from_me'][i]
        # Saving message in a file
        file.write(str(name) + ': ' + str(processed_df['text'][i]) + '\n')

# Closing file
file.close()
