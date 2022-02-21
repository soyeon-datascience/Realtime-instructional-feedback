# Project WISE
> Sentiment analysis of audio files for providing teacher feedback in the classroom

## Quick navigation
[Background](#background)  
[Data](#data)  
[Models](#models)  
[Timeline](#timeline)  
[Repo Structure](#repo-structure)  
[Logistics](#project-logistics)  
[Resources](#resources)  
[Contact](#contact-info)

# Goal

The objective of this project is to label sections of audio files with positive, negative, or neutral based on the statements made by the instructor.  This task fits into an overall objective of providing real-time feedback to teachers regarding their daily interactions with their students.

# Background  

It's Ms. Samuels first year teaching. She graduated from Vanderbilt with a degree in Elementary Education in May. With a degree from one of the best schools of education in the country, she was confident she would be ready to teach this fall. She landed a job as a 1st grade teacher at an elementary school in East Nashville and by the end of the third week of school she was already feeling burnt out and questioning her decision to become a teacher. While she feels like she knows how to provide effective instruction, she’s really struggling with classroom and behavior management. She feels like she spends her entire day redirecting students who are off-task and trying to stop students from misbehaving.

She reached out to her colleagues and principal for help, but no one seems to have time to observe her teaching and give her the coaching and support she needs to improve. While searching for resources online to help her with classroom and behavior management, she stumbles across a new smartwatch app, WISE, that uses machine learning to collect data about teachers’ classroom management practices and then uses that data to provide tailored, in the moment coaching and support to teachers to improve their classroom management. It’s like a Fitbit for classroom management! She downloads the app onto her Apple Watch and gives it a try in class the next day. When her students go to lunch, she takes a look at the data in her WISE app from her English Language Arts lesson that morning and realizes part of the problem—she’s been providing her students with nonstop negative feedback and almost no positive feedback. For every 1 piece of positive feedback she provides to her students, she’s delivering 5 pieces of negative feedback. She knows this is the opposite of what she’s supposed to be doing to improve her students’ behavior. No wonder her students are struggling to stay on task!

The WISE app recommends a simple intervention—regular reminders to provide positive feedback to her students. During her Math lesson that afternoon, she opens the WISE app and gives the intervention a try. Again, WISE uses machine learning to collect data on her classroom management practices, but this time, if she doesn’t provide positive feedback for more than 5 minutes her watch vibrates with a reminder to provide positive reinforcement to her students. At the end of the lesson, she takes a look at the data WISE collected during her math lesson. With frequent and personalized reminders, she managed to provide 6 pieces of positive feedback to her students for every 1 piece of negative feedback she provided. More importantly, she observed that her students were more on task and engaged in her lesson! Ms. Samuels finally feels like she has the coaching and support she needs to improve her classroom management practices and create the positive classroom community she dreamed about building for her students.  

# Data

The provided data are audio files.  There are accompanying transcripts with labels regarding the sentiment of statements made by teachers.

## Data security

The data should be kept in a secure location since it contains recordings of minors.

## Counts

TBD

# Models

Transformer models will be employed in order to perform this classification as provided through HuggingFace.  Initially, pretrained models will be explored for their capacity to provide the desired labels (if the set of labels exist), and will be fine-tuned if the performance is not sufficient or pretrained models for this task are not available.

# Timeline

The first phase of this project should be completed by October 16th.  This encompasses providing preliminary feedback on the performance of the models and generated classifications.

# Repo Structure 

The repo is structured as follows: Notebooks are grouped according to their series (e.g., 10, 20, 30, etc) which reflects the general task to be performed in those notebooks.  Start with the *0 notebook in the series and add other investigations relevant to the task in the series (e.g., `11-cleaned-scraped.ipynb`).  If your notebook is extremely long, make sure you've utilized nbdev reuse capabilities and consider whether you can divide the notebook into two notebooks.

All files which appear in the repo should be able to run, and not contain error or blank cell lines, even if they are relatively midway in development of the proposed task. All notebooks relating to the analysis should have a numerical prefix (e.g., 31-) followed by the exploration (e.g. 31-text-labeling). Any utility notebooks should not be numbered, but be named according to their purpose. All notebooks should have lowercase and hyphenated titles (e.g., 10-process-data not 10-Process-Data). All notebooks should adhere to literate programming practices (i.e., markdown writing to describe problems, assumptions, conclusions) and provide adequate although not superfluous code comments.

# Project logistics

* **Sprint planning**:  Tuesdays from 5:30pm to 6:30pm in the DSI Conference Room or virtually at: https://vanderbilt.zoom.us/j/93135458958?pwd=MzdobGtsemhUWVBOZ21yZXJGZGVKUT09  
* **Coder's Meeting**:  Fridays from 8-9am virtually at: https://vanderbilt.zoom.us/j/93135458958?pwd=MzdobGtsemhUWVBOZ21yZXJGZGVKUT09   
* **Demos**:  Fridays from 2-3pm in the DSI Conference room or virtually at: https://vanderbilt.zoom.us/j/96286586254?pwd=dTBuV1NXSkV0UmdWS005WlR0Qkg2Zz09&from=addon 

* **Data location**:  Box/DSI Documents  

* **Slack channel**:  https://datasciencetip.slack.com/archives/C02BS6MHW9Y   

# Resources 
* **Python usage**: Whirlwind Tour of Python, Jake VanderPlas ([Book](https://learning.oreilly.com/library/view/a-whirlwind-tour/9781492037859/), [Notebooks](https://github.com/jakevdp/WhirlwindTourOfPython))
* **Data science packages in Python**: [Python Data Science Handbook, Jake VanderPlas](https://jakevdp.github.io/PythonDataScienceHandbook/) 
* **HuggingFace**: [Website](https://huggingface.co/transformers/index.html), [Course/Training](https://huggingface.co/course/chapter1), [Inference using pipelines](https://huggingface.co/transformers/task_summary.html), [Fine tuning models](https://huggingface.co/transformers/training.html)
* **fast.ai**: [Course](https://course.fast.ai/), [Quick start](https://docs.fast.ai/quick_start.html)
* **h2o**: [Resources, documentation, and API links](https://docs.h2o.ai/#h2o)
* **nbdev**: [Overview](https://nbdev.fast.ai/), [Tutorial](https://nbdev.fast.ai/tutorial.html)
* **Git tutorials**: [Simple Guide](https://rogerdudler.github.io/git-guide/), [Learn Git Branching](https://learngitbranching.js.org/?locale=en_US)
* **ACCRE how-to guides**: [DSI How-tos](https://github.com/vanderbilt-data-science/how-tos)  

# Contact Info

Alyssa Van Camp, Ph.D., Founder and CEO  
The Behavior Company  
alyssa.m.van.camp@vanderbilt.edu  

Jesse Spencer-Smith, Ph.D. Chief Data Scientist  
Vanderbilt University Data Science Institute  
jesse.spencer-smith@vanderbilt.edu  

Charreau Bell, Ph.D. Senior Data Scientist  
Vanderbilt University Data Science Institute  
charreau.s.bell@vanderbilt.edu  

Soyeon Park, Graduate Student
Vanderbilt University Data Science Institute   
soyeon.park@vanderbilt.edu 

Li Yuan, Graduate Student
Vanderbilt University Data Science Institute   
li.yuan@vanderbilt.edu  
