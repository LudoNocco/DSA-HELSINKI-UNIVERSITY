#The participants of a contest send in their solutions for tasks. The tasks are numbered 1,2,3,\dots, and a solution for each task is worth 0–100 points.
#If a contestant submits multiple solutions to the same task, the score for the task is the maximum score of a single solution. The total score of a contestant is the sum of scores over all tasks.
#Your task is to compile the score board of the contest containing the name and the total score of each contestant. The contestants are sorted by their score from the highest to the lowest. If two contestants have the same score, the one that achieved this score first is listed higher. If two or more participants have a score 0, they are listed in alphabetical order.
#In a file contest.py, implement a class Contest with the following methods:

#__init__: constructs an object of the class
#add_submission: processes the submission of a contestant
#create_scoreboard: creates the score board of the contest

#The following example illustrates the use of the class in detail.

class Participant:
    def __init__(self, name, task_count):
        self.name = name
        self.best_scores = [0]*task_count
        self.total = 0
        self.first_achieved = None

    def update_score(self, task_index, score, submission_index):
        if score > self.best_scores[task_index]:
            old_best = self.best_scores[task_index]
            self.best_scores[task_index] = score
            self.total += (score - old_best)
            if self.total > 0:
                self.first_achieved = submission_index

class Contest:
    def __init__(self, names, task_count):
        self.task_count = task_count
        self.participants = {}
        for name in names:
            self.participants[name] = Participant(name, task_count)

        self.names = names
        self.submission_number = 0

    def add_submission(self, name, task, score):
        self.submission_number += 1
        participant = self.participants[name]
        participant.update_score(task-1, score, self.submission_number)

    def create_scoreboard(self):
        def sort_key(p):
            if p.total == 0:
                return (0, 9999999999999, p.name)
            else:
                return (-p.total, p.first_achieved, "")

        sorted_participants = sorted(self.participants.values(), key=sort_key)
        return [(p.name, p.total) for p in sorted_participants]

if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]