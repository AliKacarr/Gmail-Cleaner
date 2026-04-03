# GMailCleaner

Python script to move matching Gmail messages to Trash.

## What it does

The script:

- authenticates with the Gmail API using OAuth
- reads email addresses from `filterFrom.txt`
- searches messages where those addresses appear in either `from:` or `to:`
- moves all matches to Gmail Trash
- prints how many emails were found and how many were moved

## Requirements

- Python 3
- `credentials.json` from Google Cloud OAuth Desktop App credentials
- Gmail API enabled in your Google Cloud project

Install dependencies:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## How to use

1. Enable the Gmail API in Google Cloud.
2. Create an OAuth `Desktop app` credential.
3. Download the JSON file and place it in the project root as `credentials.json`.
4. Create `filterFrom.txt` from `filterFrom.example.txt`, then add one email address per line.
5. Run the script:

```bash
python mail_deleter.py
```

On first run, a browser window opens for Google authorization. After approval, a token file is saved in the `token files` folder.

## Filter behavior

Each line in `filterFrom.txt` is used to build a Gmail query like this:

```text
(from:example@gmail.com OR to:example@gmail.com)
```

This means the script can match:

- emails received from that address
- emails sent to that address

Multiple lines are combined with `OR`.

## Custom queries

If you want to use your own Gmail search query, check the [Gmail search operators documentation](https://support.google.com/mail/answer/7190?hl=en) and replace the generated query in `mail_deleter.py`.

## Warning

Matching emails are moved to Trash automatically. Test with a small filter first.
