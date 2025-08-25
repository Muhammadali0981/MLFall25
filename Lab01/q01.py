import pandas as pd


data1 = [
    { 'test_score': 40 , 'writing skills': 52 , 'reading skill': 90, 'maths skill': 70, 'science skill': 80},
    { 'test_score': 60 , 'writing skills': 62 , 'reading skill': 80, 'maths skill': 60, 'science skill': 70},
    { 'test_score': 70 , 'writing skills': 72 , 'reading skill': 70, 'maths skill': 50, 'science skill': 60},
    { 'test_score': 80 , 'writing skills': 82 , 'reading skill': 60, 'maths skill': 40, 'science skill': 50},
    { 'test_score': 90 , 'writing skills': 92 , 'reading skill': 50, 'maths skill': 30, 'science skill': 40},
    { 'test_score': 100 , 'writing skills': 100 , 'reading skill': 40, 'maths skill': 20, 'science skill': 30},
    { 'test_score': 110 , 'writing skills': 110 , 'reading skill': 30, 'maths skill': 10, 'science skill': 20},
    { 'test_score': 120 , 'writing skills': 120 , 'reading skill': 20, 'maths skill': 0, 'science skill': 10},
    { 'test_score': 130 , 'writing skills': 130 , 'reading skill': 10, 'maths skill': 0, 'science skill': 10},
    { 'test_score': 140 , 'writing skills': 140 , 'reading skill': 0, 'maths skill': 0, 'science skill': 0}
]

df1 = pd.DataFrame(data1)
print(df1)

features = ['test_score', 'writing skills', 'reading skill', 'maths skill', 'science skill']
data2 = [
    [40, 52, 90, 70, 80],
    [50, 62, 80, 60, 70],
    [60, 72, 70, 50, 60],
    [70, 82, 60, 40, 50],
    [80, 92, 50, 30, 40],
    [90, 100, 40, 20, 30],
    [100, 110, 30, 10, 20],
    [110, 120, 20, 0, 10],
    [120, 130, 10, 0, 10],
    [130, 140, 0, 0, 0]
]

df2 = pd.DataFrame(data2, columns=features)
print(df2)

test_scores = pd.Series([40, 50, 60, 70, 80, 90, 100, 110, 120, 130])
writing_skills = pd.Series([52, 62, 72, 82, 92, 100, 110, 120, 130, 140])
reading_skills = pd.Series([90, 80, 70, 60, 50, 40, 30, 20, 10, 0])
maths_skills = pd.Series([70, 60, 50, 40, 30, 20, 10, 0, 0, 0])
science_skills = pd.Series([80, 70, 60, 50, 40, 30, 20, 10, 10, 0])
data3 = {
    'test_score': test_scores,
    'writing skills': writing_skills,
    'reading skill': reading_skills,
    'maths skill': maths_skills,
    'science skill': science_skills
}

df3 = pd.DataFrame(data3)
print(df3)