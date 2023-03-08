import csv

acceptable = {}
participants = []
answers_list = [[] for _ in range(6)]
scores_list = []


def ready_up():
    fields = []
    rows = []
    with open('esm_famil_data.csv', encoding='utf-8') as f:
        csvreader = csv.reader(f)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

    new_rows = [[] for _ in range(6)]

    for k in range(len(fields)):
        for i in range(len(rows)):
            if rows[i][k] != "":
                word = rows[i][k].split()
                new_word = "".join(word)
                new_rows[k].append(new_word)

    global acceptable
    acceptable = {k: v for (k, v) in zip(fields, new_rows)}


def add_participant(participant, answers):
    ans = ["esm", "famil", "keshvar", "rang", "ashia", "ghaza"]
    cor_ans = []
    global participants
    global answers_list
    answer_list = list(answers.values())
    for i in range(6):
        if answer_list[i] != "":
            word = answer_list[i].split()
            new_word = "".join(word)
            cor_ans.append(new_word)
            if new_word != "" and new_word :
                answers_list[i].append(new_word)
    answer_dict = dict(zip(ans, cor_ans))
    p_list =[participant, answer_dict]
    participants.append(p_list)


def calculate_all():
    scores_list = []
    par_list = [p[0] for p in participants]
    for participant in participants:
        ans = participant[1]
        score = 0
        i = 0
        for key, value in ans.items():
            if len(answers_list[i]) == len(participants):
                if value != "" and value in acceptable[key]:
                    if answers_list[i].count(value) == 1:
                        score += 10
                    else:
                        score += 5
                else:
                    score += 0
            else:
                if value != "" and value in acceptable[key]:
                    if answers_list[i].count(value) == 1:
                        score += 15
                    else:
                        score += 10
                else:
                    score += 0
            i += 1
        scores_list.append(score)
    return dict(zip(par_list, scores_list))


ready_up()
add_participant(participant='salib', answers={'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
add_participant(participant='kianoush', answers={'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
add_participant(participant = 'sajjad', answers = {'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
add_participant(participant = 'farhad', answers = {'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})
print(calculate_all())