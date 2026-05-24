# DevBMS Platform - Project Knowledge

## 1. Project Identity

This project is the dynamic Django version of devbms.com.

The current public website presents Belal Alsweirki / DevBMS as:

- Odoo / ERP Technical Consultant
- Python Developer
- Business Systems Architect
- Based in Madrid, Spain
- Focused on Odoo, ERP modernization, Python, Django, Docker, PostgreSQL, Linux, AI-assisted development, and business process automation

The platform must represent Belal professionally and clearly, not as a generic blog or simple CV website.

## 2. Current Website Summary

The current devbms.com website is a bilingual professional portfolio/CV website.

Current public sections:

1. Hero / Identity
   - Name: Belal Alsweirki
   - Role: Odoo / ERP Technical Consultant
   - Subtitle: Python Developer | Business Systems Architect
   - Location: Madrid, Spain
   - Phone
   - Email
   - LinkedIn
   - Website

2. Languages
   - Arabic: Native
   - English: Professional working proficiency
   - Spanish: A2 — currently improving

3. Professional Summary
   - 9+ years of experience
   - Building business software, ERP systems, POS solutions, and web applications
   - Current work with Bidatia Sistemas SL in Spain
   - Focus on Odoo development, ERP modernization, automation, Docker-based deployments, integrations, and business requirements analysis
   - Strong background in Python, Django, PostgreSQL, Odoo, Docker, Linux, and technical leadership

4. Professional Experience
   - Odoo Developer / ERP Technical Consultant at Bidatia Sistemas SL, Madrid, Spain
   - Odoo Technical Consultant at Integration Point LLC, Muscat, Oman
   - Chief Technology Officer at Ghaith Technology, Muscat, Oman
   - Odoo Developer at Selsela Information Technology, Gaza, Palestine
   - Python Technical Trainer at VISIONPLUS, Gaza, Palestine

5. Selected Projects
   - Spanish Logistics Company — Odoo 19 ERP Modernization
   - Debt Collection Management System — Oman

6. Core Skills
   - Odoo
   - Backend
   - DevOps
   - Business
   - AI-Assisted Development
   - ERP Automation
   - Data & Reporting
   - System Integration

7. Education
   - Bachelor's Degree in Multimedia & Web Development
   - Diploma in Mechanical Engineering

8. Language switch
   - English version at /
   - Spanish version at /es/

## 3. Product Goal

Convert the static devbms.com website into a dynamic Django platform.

The new platform should allow managing most public content from Django Admin instead of editing static HTML.

The first goal is not to build a huge system. The first goal is to create a clean foundation that can grow.

## 4. Main Platform Modules

The Django project contains these apps:

### core

Responsible for:
- Homepage
- Global site settings
- Navigation
- Contact information
- SEO defaults
- Shared layout/templates
- Language switch
- Static public pages if needed

### cv

Responsible for:
- Personal profile
- Professional summary
- Work experience
- Education
- Languages
- Skills
- Certifications later
- Dynamic CV sections
- Admin-managed CV content

### portfolio

Responsible for:
- Projects
- Case studies
- Technologies used
- Problem / Solution / Result structure
- Featured projects on homepage
- Project detail pages

### blog

Responsible for:
- Technical articles
- Categories
- Tags
- Draft/published workflow
- SEO metadata
- Future content strategy around Odoo, Django, ERP, automation, and AI-assisted development

## 5. Site Vision

The platform should become a professional personal system, not only a public CV.

It should support:

- A strong homepage for recruiters, clients, and collaborators
- A dynamic CV that can be updated from Django Admin
- Case studies that explain real projects professionally
- Blog posts to build authority around Odoo, Python, Django, ERP, and AI-assisted development
- SEO-friendly structure
- Future expansion for tools, media systems, or subdomains

## 6. Public Pages Required

Initial public pages:

1. Home
   URL: /
   Purpose:
   - Introduce Belal / DevBMS
   - Show professional role
   - Show short summary
   - Highlight skills
   - Highlight selected projects
   - Link to CV, portfolio, blog, contact

2. Spanish Home
   URL: /es/
   Purpose:
   - Spanish version of the homepage
   - Should mirror the English content where possible

3. CV Page
   URL: /cv/
   Purpose:
   - Full professional CV
   - Dynamic from Django Admin
   - Structured and readable

4. Spanish CV Page
   URL: /es/cv/
   Purpose:
   - Spanish version of CV

5. Portfolio List
   URL: /projects/
   Purpose:
   - List projects and case studies

6. Project Detail
   URL: /projects/<slug>/
   Purpose:
   - Show detailed case study

7. Blog List
   URL: /blog/
   Purpose:
   - List published posts

8. Blog Detail
   URL: /blog/<slug>/
   Purpose:
   - Show article detail

9. Contact Section or Page
   URL: /contact/ or homepage section
   Purpose:
   - Email, LinkedIn, website, WhatsApp if needed

## 7. Admin Requirements

The project must be admin-first.

When creating models, make them easy to manage from Django Admin.

Admin should use:
- list_display
- search_fields
- list_filter
- prepopulated_fields for slug fields
- ordering
- readonly_fields where useful
- fieldsets for larger models

The user should be able to update:
- Profile data
- Summary
- Contact information
- Skills
- Experience
- Education
- Languages
- Projects
- Blog posts
- SEO titles/descriptions

## 8. Content Model Direction

### SiteProfile

Suggested fields:
- full_name
- headline
- subheadline
- location
- phone
- email
- linkedin_url
- website_url
- whatsapp_url
- short_summary
- professional_summary
- profile_image
- is_active

Only one active profile should normally be used.

### SkillCategory

Suggested fields:
- name
- description
- order

Examples:
- Odoo
- Backend
- DevOps
- Business
- AI-Assisted Development
- ERP Automation
- Data & Reporting
- System Integration

### Skill

Suggested fields:
- category
- name
- description
- order
- is_featured

### Experience

Suggested fields:
- title
- company
- location
- start_date
- end_date
- is_current
- summary
- order

Need support for bullet points.

### Education

Suggested fields:
- degree
- institution
- location
- start_year
- end_year
- description
- order

### Language

Suggested fields:
- name
- level
- order

### Project / CaseStudy

Suggested fields:
- title
- slug
- client_or_context
- short_description
- long_description
- problem
- solution
- result
- technologies
- is_featured
- status
- published_at
- meta_title
- meta_description

### BlogPost

Suggested fields:
- title
- slug
- excerpt
- content
- status: draft/published
- category
- tags
- published_at
- meta_title
- meta_description
- created_at
- updated_at

## 9. Multilingual Direction

The current site has English and Spanish versions.

Initial implementation can be simple and pragmatic.

Do not over-engineer full i18n too early.

Acceptable early approach:
- Keep English as default.
- Prepare structure for Spanish pages.
- Use language-specific fields only where necessary, for example:
  - title_en
  - title_es
  - summary_en
  - summary_es
  - content_en
  - content_es

Avoid implementing complex translation frameworks unless explicitly requested.

## 10. SEO Requirements

Every public page should be SEO-friendly.

Important SEO concepts:
- Unique title
- Meta description
- Clean slug
- Semantic HTML
- Fast loading
- Open Graph metadata later
- Sitemap later
- robots.txt later

For content models, include:
- slug
- meta_title
- meta_description
- published status where relevant
- created_at
- updated_at

Do not over-engineer SEO in the first step, but keep the structure ready.

## 11. UI Direction

The design should feel:

- Professional
- Modern
- Clean
- Fast
- Credible
- Developer-focused
- Business-oriented

Avoid:
- Flashy animations
- Over-complicated UI
- Heavy frontend frameworks at the beginning
- Random design experiments
- Generic portfolio templates that do not reflect Odoo/ERP/Python expertise

Initial templates can be simple Django templates with clean HTML/CSS.

## 12. Technical Direction

Current stack:
- Python
- Django
- Django Admin
- Django REST Framework if needed
- SQLite for early development
- PostgreSQL later
- Gunicorn / Nginx later
- Docker later
- Whitenoise later/when appropriate

Development rules:
- Keep changes focused.
- Do not add Docker until requested.
- Do not add Celery/Redis/background workers until requested.
- Do not add APIs unless needed.
- Do not add authentication beyond Django Admin unless requested.
- Do not hardcode secrets.
- Keep code readable.
- Prefer simple, maintainable Django patterns.

## 13. First Development Milestones

### Milestone 1: Project foundation

Expected result:
- Apps registered
- Static/media/templates configured
- Homepage route works
- Admin works
- Project passes python manage.py check

### Milestone 2: Dynamic CV foundation

Expected result:
- Models for profile, experience, education, skills, languages
- Admin management for CV data
- CV page renders dynamic data

### Milestone 3: Portfolio foundation

Expected result:
- Project/case study model
- Admin management
- Projects list page
- Project detail page
- Featured projects on homepage

### Milestone 4: Blog foundation

Expected result:
- Blog post model
- Category/tag support
- Draft/published workflow
- Blog list and detail pages
- SEO fields

### Milestone 5: Content migration

Expected result:
- Current devbms.com content added as initial database seed or admin data
- English content available
- Spanish content prepared where possible

### Milestone 6: Visual improvement

Expected result:
- Clean layout
- Navigation
- Homepage sections
- CV page
- Portfolio pages
- Blog pages
- Responsive design

### Milestone 7: Deployment preparation

Expected result:
- Production settings plan
- PostgreSQL plan
- Static files plan
- Gunicorn/Nginx or Cloudflare Tunnel plan
- Backups plan

## 14. Initial Current Content to Preserve

The platform must preserve the core public identity:

Name:
Belal Alsweirki

Main headline:
Odoo / ERP Technical Consultant

Subheadline:
Python Developer | Business Systems Architect

Location:
Madrid, Spain

Languages:
- Arabic: Native
- English: Professional working proficiency
- Spanish: A2 — currently improving

Professional positioning:
- Odoo / ERP Technical Consultant
- Python Developer
- Business Systems Architect
- 9+ years of experience
- Business software
- Custom ERP systems
- POS solutions
- Web applications
- Odoo customization
- Odoo module development
- System migration
- Docker-based deployments
- Integrations
- Business requirements analysis

Current role:
Odoo Developer / ERP Technical Consultant
Bidatia Sistemas SL — Madrid, Spain
Mar 2026 – Present

Selected project:
Spanish Logistics Company — Odoo 19 ERP Modernization

Selected project:
Debt Collection Management System — Oman

Core skills:
- Odoo
- Python
- Django
- PostgreSQL
- Docker
- Linux
- Nginx
- Git
- REST APIs
- ERP implementation
- Process analysis
- Technical consulting
- AI-assisted development
- Workflow automation
- Data migration
- Reporting
- System integration

## 15. Important Working Style for Aider

When using Aider:

- Do not implement all milestones in one response.
- Work milestone by milestone.
- Keep changes small and testable.
- Always explain files changed.
- Always provide commands to validate.
- Always mention expected result after implementation.
- Always mention whether migrations are needed.
- Avoid large rewrites.
- If a file does not exist, create it only when required.
- Do not invent unnecessary complexity.

## 16. Expected Response Format

Every implementation should include:

1. Implementation Summary
2. Files Changed
3. Commands to Run
4. Validation Steps
5. Expected Result After Implementation
6. Risks or Notes

## 17. Immediate Next Task

The immediate next task is Milestone 1:

Prepare the initial Django structure:
- Register apps
- Register rest_framework
- Configure templates directory
- Configure static/media settings
- Create core URLs
- Create homepage view
- Include core URLs from project URLs
- Keep admin available
- Keep project simple
