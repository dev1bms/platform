# DevBMS Platform - Development Guide

This is the personal Django platform for devbms.com.

## Project goal

Convert the current static portfolio website into a dynamic Django-based platform that represents Belal Alswerki / DevBMS professionally.

The platform should support:
- Personal homepage
- Dynamic CV management from Django Admin
- Blog
- Portfolio / projects section
- Case studies
- SEO-friendly public pages
- Admin-managed content
- Future expansion to additional personal platforms under separate subdomains

## Product vision

This is not only a simple portfolio website. It should become a professional personal platform for:
- Showcasing Python, Django, Odoo, ERP, automation, and AI-assisted development work
- Publishing technical articles
- Maintaining a dynamic CV
- Presenting real-world projects and case studies
- Supporting future personal tools and media-management systems

## Tech stack

- Python
- Django
- Django Admin
- Django REST Framework when needed
- SQLite for early local development
- PostgreSQL later
- Docker later for deployment
- Gunicorn / Nginx later for production
- Whitenoise for static files when appropriate

## Development rules

- Keep changes focused and minimal.
- Do not rewrite unrelated files.
- Do not introduce complex architecture too early.
- Prefer clean Django architecture.
- Prefer readable, explicit code over clever abstractions.
- Use Django Admin for content management whenever possible.
- Keep business logic out of templates when possible.
- Add models carefully with readable field names.
- Always create migrations after model changes.
- Do not hardcode secrets, passwords, tokens, domains, or API keys.
- Use environment variables for sensitive settings.
- Keep public pages SEO-friendly.
- Do not add Docker unless explicitly requested.
- Do not add Celery, Redis, APIs, or background workers unless explicitly requested.
- Do not mix the future media platform into this project unless explicitly requested.
- Preserve a clean structure that can later support multilingual content.

## Apps

- core: homepage, shared pages, layout, navigation, site-wide settings.
- blog: posts, categories, tags, publishing workflow, SEO metadata.
- cv: dynamic CV, personal info, experience, education, skills, languages, certifications.
- portfolio: projects, case studies, technologies, screenshots, problem/solution/result structure.

## Admin-first approach

When adding content models, make sure they can be managed comfortably from Django Admin.

Admin screens should be practical and clean:
- list_display where useful
- search_fields where useful
- list_filter where useful
- prepopulated_fields for slugs where useful
- fieldsets when the model grows

## SEO requirements

For public content models, consider SEO fields such as:
- slug
- meta_title
- meta_description
- canonical URL later if needed
- published status
- created_at
- updated_at

Do not over-engineer SEO in the first implementation, but keep the structure ready.

## Design and UI direction

The public website should feel:
- professional
- clean
- modern
- fast
- credible
- developer-focused

Avoid flashy or overly complicated UI. The site should prioritize clarity, trust, and useful content.

## Current development stage

The project is in its initial foundation stage.

Do not jump directly to advanced deployment, Docker, media platform, authentication systems, or complex APIs unless explicitly requested.

## Expected response style

For every implementation, provide:

1. Implementation Summary
2. Files Changed
3. Commands to Run
4. Validation Steps
5. Expected Result After Implementation
6. Risks or Notes

## Validation expectations

After code changes, suggest the relevant commands, for example:

- python manage.py check
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver 0.0.0.0:8000

When changing models, always mention whether migrations are needed.
