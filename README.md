# puzzleWebsite

Puzzle hints website rebuilt with Django for Vercel hosting.

## Local Run

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start dev server:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Vercel Deploy

- Django entrypoint: `puzzle_project/wsgi.py`
- Static files served from: `static/`
- Configured in: `vercel.json`
