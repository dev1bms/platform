# DevBMS Platform - Development Guide

This is the personal Django platform for devbms.com.

## Project goal

Convert the current static portfolio website into a dynamic Django-based platform.

Main features:
- Personal homepage
- Dynamic CV management from Django admin
- Blog
- Portfolio / projects section
- SEO-friendly public pages
- Admin-managed content
- Future support for media-related personal platforms under separate subdomains

## Tech stack

- Python
- Django
- Django Admin
- PostgreSQL later
- Docker later for deployment
- Gunicorn / Nginx later for production

## Development rules

- Keep changes focused and minimal.
- Do not rewrite unrelated files.
- Prefer clean Django architecture.
- Use Django Admin for content management.
- Add models carefully with readable field names.
- Always create migrations after model changes.
- Do not hardcode secrets.
- Use environment variables for sensitive settings.
- Keep public pages SEO-friendly.
- Do not add Docker unless explicitly requested.

## Apps

- core: homepage, shared pages, layout, navigation.
- blog: posts, categories, tags, publishing workflow.
- cv: dynamic CV, experience, education, skills, languages.
- portfolio: projects, case studies, technologies.

## Expected response style

For every implementation, provide:

1. Implementation Summary
2. Files Changed
3. Commands to Run
4. Validation Steps
5. Expected Result After Implementation
6. Risks or Notes
