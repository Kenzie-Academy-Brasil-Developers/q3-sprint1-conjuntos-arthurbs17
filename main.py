from snippets import spanish_fruits, brazilian_fruits, japanese_fruits, popular_fruits, emails

def spanish_and_brazilian_fruits(spanish_fruits, brazilian_fruits):
    return list(spanish_fruits & brazilian_fruits)

def spanish_and_japan_fruits(spanish_fruits, japanese_fruits):
    return list(spanish_fruits & japanese_fruits)

def brazilian_and_japan_fruits(brazilian_fruits, japanese_fruits):
    return list(brazilian_fruits & japanese_fruits)

def popular_spanish_or_brazilian_fruits(popular_fruits, spanish_fruits, brazilian_fruits):
    brazilian_spanish = spanish_fruits | brazilian_fruits
    return list(brazilian_spanish & popular_fruits)

def popular_only_spanish_fruits(popular_fruits, spanish_fruits, japanese_fruits, brazilian_fruits):
    difference_set = spanish_fruits - (japanese_fruits|brazilian_fruits)
    return list(difference_set & popular_fruits)

def only_yahoo_emails(emails_list):
    return set([email for email in emails_list if email.lower().count('yahoo') > 0])

def only_hotmail_emails(emails_list):
    return set([email for email in emails_list if email.lower().count('hotmail') > 0])

def only_br_emails(emails_list):
    return set([email for email in emails_list if email.lower().endswith('br')])

result = popular_only_spanish_fruits(popular_fruits, spanish_fruits, japanese_fruits, brazilian_fruits)
result_email = only_br_emails(emails)