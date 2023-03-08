from datetime import datetime, timedelta


class FactorHandler:
    def __init__(self):
        self.__factors = {}

    def time_formatter(self, time_format, time):
        if time_format == 'dd/mm/yyyy':
            d = f'{time[:2]}/{time[3:5]}/{time[6:]}'
        elif time_format == 'dd/yyyy/mm':
            d = f'{time[:2]}/{time[8:]}/{time[3:7]}'
        elif time_format == 'yyyy/mm/dd':
            d = f'{time[8:]}/{time[5:7]}/{time[:4]}'
        elif time_format == 'yyyy/dd/mm':
            d = f'{time[5:7]}/{time[8:]}/{time[:4]}'
        elif time_format == 'mm/yyyy/dd':
            d = f'{time[8:]}/{time[:2]}/{time[3:7]}'
        else:
            d = f'{time[3:5]}/{time[:2]}/{time[6:]}'
        return datetime.strptime(d, '%d/%m/%Y').date()

    def add_factor(self, time_format, time, value):
        d = self.time_formatter(time_format, time)
        if d in self.__factors:
            self.__factors[d].append(value)
        else:
            self.__factors[d] = [value]

    def remove_all_factors(self, time_format, time):
        d = self.time_formatter(time_format, time)
        del self.__factors[d]

    def get_sum(self, time_format, start_time, finish_time):
        summary = 0
        start = self.time_formatter(time_format, start_time)
        end = self.time_formatter(time_format, finish_time)
        delta = timedelta(days=1)
        while start <= end:
            if start in self.__factors:
                summary += sum(self.__factors[start])
            start += delta
        return summary
