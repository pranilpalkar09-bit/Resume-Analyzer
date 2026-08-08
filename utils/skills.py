def extract_skills(text):
    skills = [
        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Data Science",
        "TensorFlow",
        "Scikit-learn",
        "Pandas",
        "NumPy",
        "Streamlit",
        "Git",
        "GitHub",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Flask",
        "Django",
        "Docker",
        "AWS"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills