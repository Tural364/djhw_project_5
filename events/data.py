EVENTS = [
    {
        "id": 1,
        "title": "Python Workshop",
        "description": "Practical workshop about Python programming and useful development techniques.",
        "category": "Education",
        "location": "Baku",
        "status": "active",
    },
    {
        "id": 2,
        "title": "Tech Conference",
        "description": "A technology event about modern web development and software engineering.",
        "category": "Technology",
        "location": "Baku Expo Center",
        "status": "active",
    },
    {
        "id": 3,
        "title": "Football Tournament",
        "description": "Local football tournament for amateur teams.",
        "category": "Sport",
        "location": "Baku Sports Palace",
        "status": "closed",
    },
]

CATEGORIES = ["Education", "Technology", "Sport", "Entertainment", "Other"]
STATUSES = ["active", "closed"]


def get_event(event_id):
    return next((event for event in EVENTS if event["id"] == event_id), None)


def get_next_id():
    return max((event["id"] for event in EVENTS), default=0) + 1
