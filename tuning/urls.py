from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^v1/competitions$", views.v1_competitions, name="v1_competitions"),
    url(r"^v1/competitions/(?P<competition_id>[\w.-]+)$",
        views.v1_competition,
        name="v1_competition"),
    url(r"^v1/participations$",
        views.v1_participations,
        name="v1_participations"),
    url(r"^v1/participations/(?P<participation_id>[\w.-]+)$",
        views.v1_participation,
        name="v1_participation"),
    url(r"^v1/trials$", views.v1_trials, name="v1_trials"),
    url(r"^v1/trials/(?P<trial_id>[\w.-]+)$", views.v1_trial, name="v1_trial"),
    url(r"^v1/trials/(?P<trial_id>[\w.-]+)/execute$",
        views.v1_trial_execute,
        name="v1_trial_execute"),
]
