# iMessage Fetcher

This is a Python script which retrieves all message history between you and someone else on iMessage. I was inspired to make this script when a friend accidentally deleted message history on her iPhone but had important information she still needed. Running this script on my Mac, I was able to store all message history into a text file and send it over.

## Requirements

1. Mac Laptop
2. [Python](https://www.python.org/downloads/)
3. [Pandas](https://pypi.org/project/pandas/)

## Installation
1. Clone/Download repo onto laptop
```bash
git clone https://github.com/sumuksrao/iMessageFetcher.git
```

## Usage

1. Open imessage.py file and edit path variable on line 6. The path will be path of the imessage chat db.
```bash
path = ''
```
2. Run the Python File
```bash
python imessage.py
```
