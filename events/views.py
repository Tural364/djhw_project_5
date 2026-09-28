from django.http import Http404
from django.shortcuts import redirect, render

from .data import CATEGORIES, EVENTS, get_event, get_next_id
from .forms import EventForm


def event_list(request):
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "")
    status = request.GET.get("status", "")

    events = EVENTS.copy()

    if query:
        query_lower = query.lower()
        events = [
            event for event in events
            if query_lower in event["title"].lower()
            or query_lower in event["location"].lower()
        ]

    if category in CATEGORIES:
        events = [event for event in events if event["category"] == category]

    if status in ("active", "closed"):
        events = [event for event in events if event["status"] == status]

    context = {
        "events": events,
        "categories": CATEGORIES,
        "selected_category": category,
        "selected_status": status,
        "query": query,
        "total": len(EVENTS),
        "active_count": sum(event["status"] == "active" for event in EVENTS),
        "closed_count": sum(event["status"] == "closed" for event in EVENTS),
    }

    return render(request, "events/event_list.html", context)


def event_detail(request, event_id):
    event = get_event(event_id)

    if event is None:
        raise Http404("Event not found.")

    return render(request, "events/event_detail.html", {"event": event})


def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)

        if form.is_valid():
            EVENTS.append(
                {
                    "id": get_next_id(),
                    "title": form.cleaned_data["title"],
                    "description": form.cleaned_data["description"],
                    "category": form.cleaned_data["category"],
                    "location": form.cleaned_data["location"],
                    "status": "active",
                }
            )
            return redirect("event_list")
    else:
        form = EventForm()

    return render(request, "events/event_create.html", {"form": form})


def event_close(request, event_id):
    event = get_event(event_id)

    if event is None:
        raise Http404("Event not found.")

    if request.method == "POST" and event["status"] == "active":
        event["status"] = "closed"

    return redirect("event_detail", event_id=event_id)


def event_delete(request, event_id):
    event = get_event(event_id)

    if event is None:
        raise Http404("Event not found.")

    if request.method == "POST":
        EVENTS.remove(event)
        return redirect("event_list")

    return render(request, "events/event_delete.html", {"event": event})
