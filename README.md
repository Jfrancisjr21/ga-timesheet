# GA Timesheet

A geofenced time clock for graduate assistants. GAs sign in with their Microsoft
school account and clock in on campus. Approvers review the hours and pull
pay-period reports. The reports are a guide for payroll, which runs in its own system.

## Run it locally

1. cp .env.example .env, then fill in the school values
2. docker compose up -d db
3. uv sync
4. uv run python manage.py migrate
5. uv run python manage.py runserver

## Docs

- docs/runbook.md: deploy, roll back, restore, rotate secrets, incidents
- docs/admin-guide.md: roster, buildings, courses, reports
- docs/user-guide-ga.md: for GAs
- docs/user-guide-approver.md: for approvers
- docs/decisions.md: why it works the way it does
