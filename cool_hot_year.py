from mrjob.job import MRJob
from mrjob.step import MRStep
import csv
from datetime import datetime


class CalculateGrades(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        if line.startswith('date'):
            return
          
        temp = {}

        reader = csv.reader([line])
        for row in reader:
            date, tmx, tmn = str(row[0]), float(row[2]), float(row[3])
            temp[date] = tmx
        yield _, temp

    def reducer(self, key, value):
      t = list(value)
      max_pair = max(t, key=lambda x: list(x.values())[0])
      
      max_pair_key = list(max_pair.keys())[0]
      max_pair_value = max_pair[max_pair_key]

      yield max_pair_key, max_pair_value


if __name__ == "__main__":
    CalculateGrades.run()


"""
ren cool_hot_year.py.py cool_hot_year.py
python cool_hot_year.py weather.csv

"""