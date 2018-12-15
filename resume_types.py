
from __future__ import annotations

import dataclasses
from typing import List, Optional


@dataclasses.dataclass
class Resume(object):
    personal_info: PersonalInfo
    jobs: List[Job]
    educations: List[Education]


@dataclasses.dataclass
class PersonalInfo(object):
    first_name: str
    middle_name: str
    last_name: str
    phone_number: str
    email: str
    linkedin: str
    github: str


@dataclasses.dataclass
class Job(object):
    company: str
    title: str
    start_date: Date
    end_date: Date
    location: str
    bullets: List[str]


@dataclasses.dataclass
class Education(object):
    institution: str
    start_date: Date
    end_date: Date
    location: str
    bullets: List[str]


@dataclasses.dataclass
class Date(object):
    year: int
    month: Optional[int] = None


def make_date_from_str(date: Optional[str]) -> Optional[Date]:
    """
    Expected: "2018-12", for example.
    """
    if date is None:
        return None

    year_str, month_str = date.split('-')
    return Date(int(year_str), int(month_str))


def make_resume_model(my_resume) -> Resume:
    personal_info = my_resume.personal_info
    personal_info = PersonalInfo(
        first_name=personal_info.first_name,
        middle_name=personal_info.middle_name,
        last_name=personal_info.last_name,
        phone_number=personal_info.phone_number,
        email=personal_info.email,
        linkedin=personal_info.linkedin,
        github=personal_info.github,
    )

    jobs = my_resume.jobs
    jobs = [
        Job(
            company=job_module.company,
            title=job_module.title,
            start_date=make_date_from_str(job_module.start_date),
            end_date=make_date_from_str(job_module.end_date),
            location=job_module.location,
            bullets=job_module.bullets
        )
        for job_module in jobs
    ]

    educations = my_resume.educations
    educations = [
        Education(
            institution=education_module.institution,
            start_date=Date(education_module.start_year),
            end_date=Date(education_module.end_year),
            location=education_module.location,
            bullets=education_module.bullets
        )
        for education_module in educations
    ]

    return Resume(
        personal_info=personal_info,
        jobs=jobs,
        educations=educations,
    )
