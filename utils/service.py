import datetime


class ScoreJournalMixin:
    def create_date_period_list(self):
        """Створює список дат, які знаходяться між початковою і кінцевою."""
        day_delta = datetime.timedelta(days=1)
        try:
            start_date = datetime.datetime.strptime(self.request.GET.get('start-date'), '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(self.request.GET.get('end-date'), '%Y-%m-%d').date()
        except (ValueError, TypeError):
            end_date = datetime.date.today()
            start_date = end_date - datetime.timedelta(days=15)
        return [start_date + i * day_delta for i in range((end_date - start_date).days + 1)]

    @staticmethod
    def create_scores_dict(date_period, scores, grouping_object, grouping_object_name):
        """
        Формує словник необхідний для створення таблиці з оцінками. Яка включає:
        1. Дату
        2. Назва об'єктів по яким формуються таблиця (дисципліни, студенти)
        3. Кортеж: оцінка, id оцінки
        """
        scores_dict = {}
        for date in date_period:
            scores_dict[date] = {}
            for obj in grouping_object:
                scores_dict[date][obj.id] = (0, 0)
                if scores:
                    for score in scores:
                        if obj.id == score[grouping_object_name] and date == score['created']:
                            scores_dict[date][obj.id] = (score['score'], score['id'])
                            break
        return scores_dict
