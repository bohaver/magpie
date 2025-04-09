""" Interview coding challenge for Magpie Literacy

Written with Python 3.13.3

"""

import json
from pathlib import Path

import pandas as pd
import plotly.express as px


def read_json_file(path):
    with Path(path).open() as fp:
        return json.load(fp)

def process_score_data(scores, skill_opts, score_opts):
    valid_scores = []
    invalid_scores = []
    for score in scores:
        if score.get('skill') not in skill_opts:
            invalid_scores.append(score)
            continue
        if score.get('score') not in score_opts:
            invalid_scores.append(score)
            continue
        valid_scores.append(score)
    return valid_scores, invalid_scores
        

data_json = read_json_file('datasets/data.json')
proficiency_json = read_json_file('datasets/proficiency.json')
skills_json = read_json_file('datasets/skills.json')

skill_options = set([skill['skill'] for skill in skills_json['skills']])
proficiency_options = set(proficiency_json['proficiency'])

all_scores = data_json['scores']
scores, invalid = process_score_data(all_scores, skill_options, proficiency_options)

score_df = pd.DataFrame(scores)
score_df.sort_values(by=['skill', 'score'], axis=0, inplace=True)
score_df.to_csv('output/scores_cleansed.csv', index=False)

skill_aggs = score_df.groupby('skill', as_index=False).agg(
    count=pd.NamedAgg(column='score', aggfunc='count'),
    avg_score=pd.NamedAgg(column='score', aggfunc='mean'),
)
skill_aggs.to_csv('output/skill_aggs.csv', index=False)

fig = px.bar(
    skill_aggs,
    x='skill',
    y='avg_score',
    title='Average score per skill',
    hover_data=['count'],
)
fig.write_html('output/skills.html')
