def check_registration_rules(**kwargs):
    c = 0
    nums = "0123456789"
    list_of_usernames = []
    for key, val in kwargs.items():
        if (key != "quera" and key != "codecup") and len(key) >= 4:
            if len(val) >= 6:
                for i in val:
                    if i in nums:
                        c += 1
                if c != len(val):
                    list_of_usernames.append(key)
    return list_of_usernames


output = check_registration_rules(username='password', sadegh='He3@lsa', quera='kLS45@l$')
print(output)