# Magpie skill parser
This tool parses json data sets, cleanses the data, and then generates data sets for downstream usage.
It also includes some visualization of the data.

- /datasets/data.json is the main score data being processed.
- /proficiency.json contains a list of acceptable scores
- /skills.json contains a list of acceptable skills

When cleansing the dataset, any skill not present in skills.json is skipped, as is any score not
present in proficiency.json.

It may be useful to investigate the records that are rejected by this data cleansing. Currently
they are not output in any way, but are available in the module for future use ("invalid" variable).

# Installation
Install Python 3.13.3 (although this should work with earlier versions, I have not tested them)

Clone repository and change working directory to it.

Set up virtual environment for this project
python -m venv venv

Install dependencies
pip install -r requirements.txt

# Execution & Output
Run the skill_parser.py module directly. It will generate three outputs in the /outputs folder:
- scores_cleansed.csv - This is the contents of /datasets/data.json parsed, cleansed, sorted, and exported as CSV
	- Data cleansing approach is outlined in the top section of this readme.
	- Sorting is done by skill ascending alphabetically and then score ascending numerically.
- skill_aggs.csv - This is aggregates of the scores data by skill.
- skills.html - This is a html page that contains a Plotly chart of skill aggregations

# Visualization Discussion
The goal of this analysis is primarily to see how scores differ across skills. This is shown using a bar chart,
with the x axis as the skill and the y axis as the average score.

When computing averages, it's important to be mindful of how the size of the dataset impacts the average.
An average of 5 over 2 records is very different statistically than an average of 5 over 200 records.
In the visualization, the tooltip on the bar chart includes the number of records that are being analyzed.