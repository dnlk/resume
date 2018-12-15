
from resume_types import Resume, PersonalInfo, Job, Education, Date


RENDERED_BEFORE_BODY = r"""
\starttext
\section[reference={resume}]
"""

RENDERED_AFTER_BODY = r"""
\stoptext
"""


def render_personal_info(personal_info: PersonalInfo) -> str:
    lines = [
        personal_info.first_name + ' ' + personal_info.middle_name + ' ' + personal_info.last_name,
        '',
        personal_info.phone_number,
        '',
        personal_info.email,
        '',
        personal_info.github,
        '',
        personal_info.linkedin
    ]
    return '\n'.join(lines)


def render_time_range(start_date: Date, end_date: Date) -> str:
    if end_date is not None:
        return '{start_year} - {end_year}'.format(start_year=start_date.year, end_year=end_date.year)
    else:
        return str(start_date.year)


def render_jobs(jobs: [Job]) -> str:
    lines = [r'\subsection[title={Contact Details},reference={career}]']

    for job in jobs:
        lines.extend([
            render_time_range(job.start_date, job.end_date),
            '\n',
            job.location,
            '\n',
            job.company,
            '\n',
            job.title,
        ])
        lines.append(r'\startitemize')
        for bullet in job.bullets:
            lines.append(r'\item')
            lines.append(bullet)
        lines.append(r'\stopitemize')

    return '\n'.join(lines)


def render_educations(educations: [Education]) -> str:
    lines = [r'\subsection[title={Contact Details},reference={education}]']

    for education in educations:
        lines.extend([
            render_time_range(education.start_date, education.end_date),
            '\n',
            education.location,
            '\n',
            education.institution
        ])
        lines.append(r'\startitemize')
        for bullet in education.bullets:
            lines.append(r'\item')
            lines.append(bullet)
        lines.append(r'\stopitemize')

    return '\n'.join(lines)


def render(resume: Resume) -> str:
    personal_info_str = render_personal_info(resume.personal_info)
    jobs_str = render_jobs(resume.jobs)
    educations_str = render_educations(resume.educations)

    return '\n'.join([
        RENDERED_BEFORE_BODY,
        personal_info_str,
        jobs_str,
        educations_str,
        RENDERED_AFTER_BODY
    ])
