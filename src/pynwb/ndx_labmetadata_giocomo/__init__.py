import os
from pynwb import load_namespaces, get_class

name = 'ndx-labmetadata-giocomo'

spec_path = os.path.abspath(os.path.dirname(__file__))
ns_path = os.path.join(spec_path, 'spec', f'{name}.namespace.yaml')

load_namespaces(ns_path)

LabMetaData_ext = get_class('LabMetaData_ext', name)
