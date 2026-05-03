# Project - Sell or Hold 

I created this project to learn how to integrate LLM with a frontend interface. The goal of this project is to allow users to interact with a wrapper of Gemini where the users can ask whether or not they should sell their stock on a particular date. 

It fetches information from online sources and then provides a summary of its recommendation.

I wanted to learn something new and venture into an interest of mine so I decided to build a different project than the previous 3 projects from this course.

## Architecture Overview

> The AI provides confidence scoring on how sure it is about each recommendation

## Setup Instructions 

1. Clone the repo 
2. Add SECRET_KEY and GEMINI_KEY to .env file
3. (First time only) `python manage.py migrate`
4. python manage.py runserver
   
## Sample Interactions
Include at least 2-3 examples of inputs and the resulting AI outputs to demonstrate the system is functional.

## Design Decisions: 
Why you built it this way, and what trade-offs you made.

## Testing Summary: What worked, what didn't, and what you learned.

## Reflection: What this project taught you about AI and problem-solving.

## Additional notes - What to do when: 

1. runserver or the project is not starting
- check if your postgres server is running or not. Postgres is a dependency so make sure it works properly before running your code 
