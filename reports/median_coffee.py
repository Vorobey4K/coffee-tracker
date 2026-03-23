from .base import BaseReport
import statistics

class MedianCoffeeReport(BaseReport):
    name = 'median-coffee'
    group_field = 'student'
    value_field = 'coffee_spent'

    def prepare_values(self, values):
        return [int(v) for v in values]

    def calculate_metric(self, values):
        return statistics.median(values)