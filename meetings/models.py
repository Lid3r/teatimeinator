from django.db import models
from teas.models import Tea


class Meeting(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=50)

    def __str__(self):
        return '{ date: ' + str(self.date) + ', title: ' + str(self.title) + '}'

    def serialize(self):
        return {
            "id": self.pk,
            "date": self.date,
            "title": self.title
        }


class TeaChoices(models.Model):
    meeting_ref = models.ForeignKey(
        Meeting, on_delete=models.CASCADE)
    person = models.CharField(max_length=15)
    tea_ref = models.ForeignKey(Tea, on_delete=models.CASCADE)

    def __str__(self):
        return '{ meeting: ' + str(self.meeting_ref.serialize()) + ', person: ' + str(self.person) + ', tea: ' + str(self.tea_ref.serialize()) + '}'


class SerializedSelections():
    selections = []

    def __init__(self):
        self._clear()

    def _add_to_selections(self, element):
        self.selections.append(element)

    def merge_choices(self, person: str, choices):
        self._add_to_selections({'person': person, 'teas': choices})

    def get_selections(self):
        return self.selections

    def _clear(self):
        self.selections = []
