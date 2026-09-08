survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["C++", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"],
]

survey_set = [set(language) for language in survey_results]
print(survey_set)

present_all_days = set.intersection(*survey_set)
print("Languages known by all participants:", present_all_days)

