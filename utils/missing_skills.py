from utils.skills import extract_skills

def find_missing_skills(resume_text, job_description):
    resume_skills = set(skill.lower() for skill in extract_skills(resume_text))
    jd_skills = set(skill.lower() for skill in extract_skills(job_description))

    missing = jd_skills - resume_skills

    return sorted([skill.title() for skill in missing])