from config import CUTOFF_DATE

EXCLUDE_KEYWORDS = [
    "awesome",
    "template",
    "course",
    "tutorial",
    # "guide", try
    "workshop",
    "lecture",
    "homework",
    "assignment",
    "cheatsheet"
]

def is_active(repo):
    pushed_at = repo.get("pushed_at", "")
    if not pushed_at:
        return False
    return pushed_at >= CUTOFF_DATE

def has_excluded_keywords(repo):
    name = repo.get("name", "").lower()
    description = repo.get("description", "") or ""
    description = description.lower()
    return any(
        keyword in name or keyword in description
        for keyword in EXCLUDE_KEYWORDS
    )

def is_valid(repo):
    if repo.get("fork"):
        return False
    if repo.get("archived"):
        return False
    if not is_active(repo):
        return False
    if has_excluded_keywords(repo):
        return False
    return True