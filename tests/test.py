import os
from datetime import datetime
from pynwb import NWBFile, NWBHDF5IO
import unittest

from ndx_labmetadata_giocomo import LabMetaData_ext


class LabMetaDataExtensionTest(unittest.TestCase):

    def setUp(self):
        self.nwbfile = NWBFile('description', 'id', datetime.now().astimezone())
        self.filename = 'test_labmetadata.nwb'

    def tearDown(self):
        os.remove(self.filename)

    def test_add_lab_metadata(self):
        # Creates LabMetaData container
        lab_metadata = dict(
            name='LabMetaData',
            acquisition_sampling_rate=1000.,
            number_of_electrodes=10,
            file_path='',
            bytes_to_skip=2,
            raw_data_dtype='int16',
            high_pass_filtered=False,
            movie_start_time=13.6,
            subject_brain_region='Medial Entorhinal Cortex'
        )

        lab_metadata_extension = LabMetaData_ext(**lab_metadata)

        # Add to file
        self.nwbfile.add_lab_meta_data(lab_metadata_extension)

        filename = 'test_labmetadata.nwb'

        with NWBHDF5IO(filename, 'w') as io:
            io.write(self.nwbfile)

        with NWBHDF5IO(filename, mode='r', load_namespaces=True) as io:
            nwbfile = io.read()

        for metadata_key, metadata_value in lab_metadata.items():
            self.assertEqual(metadata_value,
                             getattr(nwbfile.lab_meta_data['LabMetaData'], metadata_key, None))
