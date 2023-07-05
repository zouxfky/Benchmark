import csv
import uuid
import random
import numpy as np
import util.dataDictionary as dataDictionary

COMMENT_HEADER = ['comment_id', 'text', 'create_time']
CONCEPT_HEADER = ['concept_id', 'concept_name', 'context']
COURSE_HEADER = ['course_id', 'course_name', 'prerequisites', 'about', 'resource']
OTHER_HEADER = ['other_id', 'type', 'content']
OTHER_TYPE = ['zhihu', 'baike', 'wiki']
PAPER_HEADER = ['paper_id', 'title', 'abstract', 'doi', 'lang', 'num_citation', 'pages', 'score', 'sourcetype', 'urls',
                'year']
PROBLEM_HEADER = ['problem_id', 'content', 'option', 'answer', 'score', 'type', 'typetext', 'location', 'context_id',
                  'language']
REPLY_HEADER = ['reply_id', 'text', 'create_time']
TEACHER_HEADER = ['teacher_id', 'name', 'about', 'job_title', 'org_name']
USER_HEADER = ['user_id', 'name', 'gender', 'school', 'year_of_birth']
VIDEO_HEADER = ['video_id', 'name', 'start', 'end', 'text']
GRAPH_HEADER = ['start_id', 'end_id']
USER_COURSE_HEADER = ['user_id', 'course']
USER_PROBLEM_HEADER = ['user_id', 'problem']
USER_VIDEO_HEADER = ['user_id', 'seq']


def commentGen(dir, row_data, scale):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        total = 0
        writer = csv.writer(a)
        writer.writerow(COMMENT_HEADER)
        while total <= scale:
            writer.writerow([uuid.uuid1(), dataDictionary.getRandomData(row_data)[0], dataDictionary.getRandomTime()])
            total = total + 1


def conceptGen(dir, row_data, scale):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        total = 0
        writer = csv.writer(a)
        writer.writerow(CONCEPT_HEADER)
        while total <= scale:
            data = dataDictionary.getRandomData(row_data)
            writer.writerow([uuid.uuid1(), data[0], data[2]])
            total = total + 1


def courseGen(dir, row_data, scale):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        total = 0
        writer = csv.writer(a)
        writer.writerow(COURSE_HEADER)
        while total <= scale:
            data = dataDictionary.getRandomData(row_data)
            writer.writerow([uuid.uuid1(), data[1], data[2], data[3], data[4]])
            total = total + 1


def problemGen(dir, row_data, scale):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        total = 0
        writer = csv.writer(a)
        writer.writerow(PROBLEM_HEADER)
        while total <= scale:
            data = dataDictionary.getRandomData(row_data)
            data[0] = uuid.uuid1()
            writer.writerow(data)
            total = total + 1


def replyGen(dir, row_data, scale):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        total = 0
        writer = csv.writer(a)
        writer.writerow(REPLY_HEADER)
        while total <= scale:
            writer.writerow([uuid.uuid1(), dataDictionary.getRandomData(row_data)[0], dataDictionary.getRandomTime()])
            total = total + 1


def teacherGen(dir, row_data, scale):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        total = 0
        writer = csv.writer(a)
        writer.writerow(TEACHER_HEADER)
        while total <= scale:
            data = dataDictionary.getRandomData(row_data)
            writer.writerow([uuid.uuid1(), dataDictionary.getRandomName(), data[3], data[4], data[5]])
            total = total + 1


def userGen(dir, row_data, scale):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        total = 0
        writer = csv.writer(a)
        writer.writerow(USER_HEADER)
        while total <= scale:
            school = dataDictionary.getRandomData(row_data)
            writer.writerow([uuid.uuid1(), dataDictionary.getRandomName(), random.choice([0.0, 1.0]), school[1],
                             random.randint(1960, 2010)])
            total = total + 1


def videoGen(dir, row_data, scale):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        total = 0
        writer = csv.writer(a)
        writer.writerow(VIDEO_HEADER)
        while total <= scale:
            data = dataDictionary.getRandomData(row_data)
            writer.writerow([uuid.uuid1(), data[1], data[2], data[3], data[4]])
            total = total + 1


def courseTeacherGen(dir, course, teacher):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(GRAPH_HEADER)
        for row in course.iterrows():
            data = dataDictionary.getRandomData(teacher)
            writer.writerow([row[1]["course_id"], data[0]])


def courseFiledGen(dir, course, field):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(["course_id", "filed_list"])
        for row in course.iterrows():
            count = random.randint(1, 3)
            data = []
            if count == 1:
                writer.writerow([row[1]["course_id"], dataDictionary.getRandomData(field)[1]])
            else:
                for i in range(count):
                    data.append(dataDictionary.getRandomData(field)[1])
                writer.writerow([row[1]["course_id"], data])


def courseCommentGen(dir, course, comment):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(GRAPH_HEADER)
        for row in comment.iterrows():
            data = dataDictionary.getRandomData(course)
            writer.writerow([data[0], row[1]["comment_id"]])


def userCourseGen(dir, user, course):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(USER_COURSE_HEADER)
        for row in user.iterrows():
            count = random.randint(1, 8)
            data = []
            if count == 1:
                time = dataDictionary.getRandomTime()
                writer.writerow([row[1]["user_id"], {"course_id": dataDictionary.getRandomData(course)[0],
                                                     "enroll_time": str(time)}])
            else:
                for i in range(count):
                    time = dataDictionary.getRandomTime()
                    data.append({"course_id": dataDictionary.getRandomData(course)[0],
                                 "enroll_time": str(time)})
                writer.writerow([row[1]["user_id"], data])


def userProblemGen(dir, user, problem):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(USER_PROBLEM_HEADER)
        for row in user.iterrows():
            count = random.randint(0, 60)
            problem_list = []
            if count == 1:
                data = dataDictionary.getRandomData(problem)
                writer.writerow([row[1]["user_id"], {"problem_id": data[0],
                                                     "is_correct": random.randint(0, 1),
                                                     "attempts": random.randint(1, 50),
                                                     "score": random.randint(0, 100),
                                                     "submit_time": str(dataDictionary.getRandomTime())}])
            elif count > 1:
                for i in range(count):
                    data = dataDictionary.getRandomData(problem)
                    problem_list.append({"problem_id": data[0],
                                         "is_correct": random.randint(0, 1),
                                         "attempts": random.randint(1, 50),
                                         "score": random.randint(0, 100),
                                         "submit_time": str(dataDictionary.getRandomTime())})
                writer.writerow([row[1]["user_id"], problem_list])


def userVideoGen(dir, user, video):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(USER_VIDEO_HEADER)
        for row in user.iterrows():
            video_count = random.randint(0, 7)
            segment_count = random.randint(1, 5)
            segment_list = []
            video_list = []
            if video_count == 0:
                continue
            for x in range(video_count):
                data = dataDictionary.getRandomData(video)
                start_time = dataDictionary.getRandomTime()
                time = start_time
                if segment_count == 1:
                    start_point = round(random.uniform(0, 2000), 1)
                    end_point = round(start_point + random.uniform(0, 200))
                    segment_list = {"start_point": start_point,
                                    "end_point": end_point,
                                    "speed": random.choice([0.5, 1.0, 1.5, 2.0]),
                                    "local_start_time": time.timestamp()}
                else:
                    for y in range(segment_count):
                        start_point = round(random.uniform(0, 2000), 1)
                        end_point = round(start_point + random.uniform(0, 200))
                        if y != 0:
                            time = dataDictionary.getNextTime(time)
                        segment_list.append({"start_point": start_point,
                                             "end_point": end_point,
                                             "speed": random.choice([0.5, 1.0, 1.5, 2.0]),
                                             "local_start_time": time.timestamp()})
                if video_count == 1:
                    video_list = {"video_id": data[0], "seq": segment_list}
                else:
                    video_list.append({"video_id": data[0],
                                       "seq": segment_list})
            writer.writerow([row[1]["user_id"], video_list])


def userCommentGen(dir, user, comment):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(GRAPH_HEADER)
        for row in comment.iterrows():
            data = dataDictionary.getRandomData(user)
            writer.writerow([data[0], row[1]["comment_id"]])


def userReplyGen(dir, user, reply):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(GRAPH_HEADER)
        for row in reply.iterrows():
            data = dataDictionary.getRandomData(user)
            writer.writerow([data[0], row[1]["reply_id"]])


def commentReplyGen(dir, comment, reply):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(GRAPH_HEADER)
        for row in reply.iterrows():
            data = dataDictionary.getRandomData(comment)
            writer.writerow([data[0], row[1]["reply_id"]])


def conceptCommentGen(dir, concept, comment):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(GRAPH_HEADER)
        for row in comment.iterrows():
            data = dataDictionary.getRandomData(concept)
            writer.writerow([data[0], row[1]["comment_id"]])


def conceptCourseGen(dir, concept, course):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(GRAPH_HEADER)
        for row in course.iterrows():
            for i in range(random.randint(1, 8)):
                data = dataDictionary.getRandomData(concept)
                writer.writerow([data[0], row[1]["course_id"]])


def conceptProblemGen(dir, concept, problem):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(GRAPH_HEADER)
        for row in concept.iterrows():
            for i in range(random.randint(0, 8)):
                data = dataDictionary.getRandomData(problem)
                writer.writerow([row[1]["concept_id"], data[0]])


def conceptVideoGen(dir, concept, video):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(GRAPH_HEADER)
        for row in concept.iterrows():
            for i in range(random.randint(1, 3)):
                data = dataDictionary.getRandomData(video)
                writer.writerow([row[1]["concept_id"], data[0]])


def conceptPrerequisiteGen(dir, concept):
    with open(dir, 'w', encoding='UTF8', newline='') as a:
        writer = csv.writer(a)
        writer.writerow(GRAPH_HEADER)
        for row in concept.iterrows():
            for i in range(random.randint(1, 7)):
                data = dataDictionary.getRandomData(concept)
                writer.writerow([row[1]["concept_id"], data[0]])
