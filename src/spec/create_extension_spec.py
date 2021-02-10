import os
from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec, export_spec


def main():
    ns_builder = NWBNamespaceBuilder(doc='type for storing lab metadata for Giocomo lab',
                                     name='ndx-labmetadata-giocomo',
                                     version='0.1.0',
                                     author=['Luiz Tauffer', 'Szonja Weigl', 'Ben Dichter'],
                                     contact=['ben.dichter@gmail.com'])

    ns_builder.include_type('LabMetaData', namespace='core')

    LabMetaData_ext = NWBGroupSpec(
        doc='type for storing lab metadata',
        neurodata_type_def='LabMetaData_ext',
        neurodata_type_inc='LabMetaData',
        )

    LabMetaData_ext.add_attribute(
        name='acquisition_sampling_rate',
        doc='acquisition sampling rate in Hz',
        dtype='float',
    )

    LabMetaData_ext.add_attribute(
        name='number_of_electrodes',
        doc='number of electrodes on the probe',
        dtype='int',
    )

    LabMetaData_ext.add_attribute(
        name='file_path',
        doc='filepath for where the raw data is saved',
        dtype='text',
    )

    LabMetaData_ext.add_attribute(
        name='bytes_to_skip',
        doc='the number of bytes at the beginning of the file to skip',
        dtype='int',
    )

    LabMetaData_ext.add_attribute(
        name='raw_data_dtype',
        doc='data type (dtype) of raw voltage data',
        dtype='text',
    )

    LabMetaData_ext.add_attribute(
        name='high_pass_filtered',
        doc='binary variable as to whether raw data was high-pass filtered or not',
        dtype='bool',
    )

    LabMetaData_ext.add_attribute(
        name='movie_start_time',
        doc='the time the mouse visualization movie started playing',
        dtype='float',
    )

    LabMetaData_ext.add_attribute(
        name='subject_brain_region',
        doc='the name of the brain region where the electrode probe is recording from',
        dtype='text',
    )

    # export the extension to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, [LabMetaData_ext], output_dir)


if __name__ == "__main__":
    main()
