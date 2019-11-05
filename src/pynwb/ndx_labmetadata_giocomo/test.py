from datetime import datetime
from dateutil.tz import tzlocal
from pynwb import NWBFile, NWBHDF5IO
from ndx_labmetadata_giocomo import LabMetaData_ext

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

# Creates LabMetaData container
lab_metadata = LabMetaData_ext(
    name='LabMetaData',
    acquisition_sampling_rate=1000.,
    number_of_electrodes=10,
    file_path='',
    bytes_to_skip=2,
    raw_data_dtype='int16',
    high_pass_filtered=False,
    movie_start_time=datetime(2019, 11, 5, tzinfo=tzlocal()),
)

# Add to file
nwb.add_lab_meta_data(lab_metadata)

# Write nwb file
with NWBHDF5IO('test_labmetadata.nwb', 'w') as io:
    io.write(nwb)

with NWBHDF5IO('test_labmetadata.nwb', 'r', load_namespaces=True) as io:
    nwb = io.read()
    print(nwb)
