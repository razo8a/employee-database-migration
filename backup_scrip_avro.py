from avro.schema import parse
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

class avro_writer:
    def __init__(self, avro_schema_file, avro_data_file):
        self.avro_data_file = avro_data_file
        self.schema = parse(open(avro_schema_file, "rb") .read())

    def write_sample(self):
        with DataFileWriter(open(self.avro_data_file , "wb"), DatumWriter(), self.schema) as writer:

            writer.append(({
                'name': 'value_name',
                'year': 'data',
                'area': 'department'
            }))

            writer.append(({
                'name': 'value_name_2',
                'year': 'data_2',
                'area': 'department_2'
            }))

            writer.append(({
                'name': 'value_name_3',
                'year': 'data_3',
                'area': 'department_3'
            }))



