class BaseReport:
    name = None
    group_field = None
    value_field = None

    def generate(self, data):
        grouped_data = self.group_data(data)

        metrics_by_group = {}

        for key, values in grouped_data.items():
            prepared_values = self.prepare_values(values)
            metrics_by_group[key] = self.calculate_metric(prepared_values)

        return self.sort_result(metrics_by_group)

    def group_data(self, data):
        grouped_data = {}

        for row in data:
            key = row[self.group_field]
            value = row[self.value_field]
            grouped_data.setdefault(key, []).append(value)

        return grouped_data

    def prepare_values(self, values):
        """
        Подготовка значений перед расчетом.
        Например: приведение к int, сортировка и т.д.
        По умолчанию ничего не делает.
        """
        return values

    def sort_result(self, metrics_by_group):
        """
        Сортировка результата (по убыванию метрики).
        Можно переопределить при необходимости.
        """
        return dict(
            sorted(metrics_by_group.items(), key=lambda item: item[1], reverse=True)
        )

    def calculate_metric(self, values):
        raise NotImplementedError("Subclasses must implement calculate_metric")