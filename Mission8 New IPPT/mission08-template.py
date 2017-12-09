#
# CS1010S --- Programming Methodology
#
# Mission 8 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ippt import *
import csv

##########
# Task 1 #
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows


def read_data(filename):
    rows = read_csv(filename)
    rep_title = tuple(int(i) for i in rows[0][1:])
    data, age_title = (), ()
    for row in rows[1:]:
        data += ((tuple(int(i) for i in row[1:])),)
        title = int(row[0])
        age_title += (title,)
    return create_table(data, age_title, rep_title)

pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

# # print("## Q1 ##")
# # Sit-up score of a 24-year-old who did 10 sit-ups.
# print(access_cell(situp_table, 24, 10))    # 0

# # Push-up score of a 18-year-old who did 30 push-ups.
# print(access_cell(pushup_table, 18, 30))   # 16

# # Run score of a 30-year old-who ran 12 minutes (720 seconds)
# print(access_cell(run_table, 30, 720))     # 36

# # Since our run.csv file does not have data for 725 seconds, we should
# # get None if we try to access that cell.
# print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 #
##########

def pushup_score(pushup_table, age, pushup):
    if pushup > 60:
        return access_cell(pushup_table, age, 60)
    elif pushup <= 0:
        return access_cell(pushup_table, age, 1)
    return access_cell(pushup_table,age, pushup)


def situp_score(situp_table, age, situp):
    if situp > 60:
        return access_cell(situp_table, age, 60)
    elif situp <= 0:
        return access_cell(situp_table, age, 1)
    return access_cell(situp_table, age, situp)

def run_score(run_table, age, run):
    if run <= 510:
        return access_cell(run_table, age, 510)
    elif run >= 1100:
        return access_cell(run_table, age, 1100)
    elif 510<run<1100:
        score = access_cell(run_table, age, run)
        if not score:
            run = run + 10 - int(str(run)[-1])
            score = access_cell(run_table, age, run)
        return score

# print("## Q2 ##")
# print(pushup_score(pushup_table, 18, 61))   # 25
# print(pushup_score(pushup_table, 18, 70))   # 25
# print(situp_score(situp_table, 24, 0))      # 0

# print(run_score(run_table, 30, 720))        # 36
# print(run_score(run_table, 30, 725))        # 35
# print(run_score(run_table, 30, 735))        # 35
# print(run_score(run_table, 30, 500))        # 50
# print(run_score(run_table, 30, 1300))       # 0


##########
# Task 3 #
##########

def ippt_award(score):
    if score<51:
        return "F"
    elif score<61:
        return "P"
    elif score<75:
        return "P$"
    elif score<85:
        return "S"
    else:
        return "G"

# print("## Q3 ##")
# print(ippt_award(50))     # F
# print(ippt_award(51))     # P
# print(ippt_award(61))     # P$
# print(ippt_award(75))     # S
# print(ippt_award(85))     # G


##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    pushup_table, situp_table, run_table = get_pushup_table(ippt_table), get_situp_table(ippt_table), get_run_table(ippt_table)
    situp_s = situp_score(situp_table, age, situp)
    pushup_s = pushup_score(pushup_table, age, pushup)
    run_s = run_score(run_table, age, run)
    total_score = pushup_s + situp_s + run_s
    award = ippt_award(total_score)
    return(total_score, award)



# print("## Q4 ##")
# print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
# print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
# print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
# print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
# print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########
def make_training_program(rate_pushup, rate_situp, rate_run):
    def training_program(ippt_table, age, pushup, situp, run, days):
        new_pushup = pushup + days//rate_pushup
        new_situp = situp + days//rate_situp
        new_run = run - days//rate_run
        results = ippt_results(ippt_table, age, new_pushup, new_situp, new_run)
        return (new_pushup, new_situp, new_run, results)

    return training_program

# print("## Q5 ##")
tp = make_training_program(7, 3, 10)
# print(tp(ippt_table, 25, 30, 25, 820, 30))        # (34, 35, 817, (61, 'P$'))


##########
# Bonus  #
##########

def make_tp_bonus(rate_pushup, rate_situp, rate_run):
    def tp_bonus(ippt_table, age, pushup, situp, run, days):
        results = ippt_results(ippt_table, age, pushup, situp, run)
        max_score = results[0]
        run_table, pushup_table, situp_table = get_run_table(ippt_table), get_pushup_table(ippt_table), get_situp_table(ippt_table)
        max_pushup, max_situp, max_run = pushup, situp, run

        for s_days in range(days+1):
            for p_days in range(days+1-s_days):
                r_days = 11 - s_days - p_days
                new_pushup = pushup + p_days//rate_pushup
                new_situp = situp + s_days//rate_situp
                new_run = run - r_days//rate_run
                new_score = ippt_results(ippt_table, age, new_pushup, new_situp, new_run)[0]

                if new_score > max_score:
                    max_score = new_score
                    results = ippt_results(ippt_table, age, new_pushup, new_situp, new_run)
                    max_pushup, max_situp, max_run = new_pushup, new_situp, new_run
                    print(new_pushup, new_situp, new_run, results)

        return (new_pushup, new_situp, new_run, results)

    return tp_bonus

tp_bonus = make_tp_bonus(7, 3, 10)

# Note: Depending on your implementation, you might get a different number of
# sit-up, push-up, and 2.4km run timing. However, the IPPT score and grade
# should be the same as the sample output.

print(tp_bonus(ippt_table, 25, 20, 30, 800, 30))      # (20, 40, 800, (58, 'P'))
print(tp_bonus(ippt_table, 25, 20, 30, 800, 2))       # (20, 30, 800, (52, 'P'))
