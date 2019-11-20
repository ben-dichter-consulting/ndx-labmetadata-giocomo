from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec
from export_spec import export_spec
from pynwb.file import LabMetaData


def main():
    ns_builder = NWBNamespaceBuilder(doc='type for storing lab metadata',
                                     name='ndx-labmetadata-giocomo',
                                     version='0.0.1',
                                     author='Luiz Tauffer and Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    LabMetaData_ext = NWBGroupSpec(
        doc='type for storing lab metadata',
        neurodata_type_def='LabMetaData_ext',
        neurodata_type_inc='LabMetaData',
        )

    LabMetaData_ext.add_attribute(
        name='acquisition_sampling_rate',
        doc='acquisition sampling rate in Hz',
        dtype='float',
        shape=None,
    )

    LabMetaData_ext.add_attribute(
        name='number_of_electrodes',
        doc='number of electrodes on the probe',
        dtype='int',
        shape=None,
    )

    LabMetaData_ext.add_attribute(
        name='file_path',
        doc='filepath for where the raw data is saved',
        dtype='text',
        shape=None,
    )

    LabMetaData_ext.add_attribute(
        name='bytes_to_skip',
        doc='the number of bytes at the beginning of the file to skip',
        dtype='int',
        shape=None,
    )

    LabMetaData_ext.add_attribute(
        name='raw_data_dtype',
        doc='data type (dtype) of raw voltage data',
        dtype='text',
        shape=None,
    )

    LabMetaData_ext.add_attribute(
        name='high_pass_filtered',
        doc='binary variable as to whether raw data was high-pass filtered or not',
        dtype='bool',
        shape=None,
    )

    LabMetaData_ext.add_attribute(
        name='movie_start_time',
        doc='the time the mouse visualization movie started playing',
        dtype='float',
        shape=None,
    )
    LabMetaData_ext.add_attribute(
        name='subject_brain_region',
        doc='the name of the brain region where the electrode probe is recording from',
        dtype='text',
        shape=None,
    )

    new_data_types = [LabMetaData_ext]

    ns_builder.include_type('LabMetaData', namespace='core')

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
