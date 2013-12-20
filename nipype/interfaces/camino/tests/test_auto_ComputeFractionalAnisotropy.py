# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.camino.dti import ComputeFractionalAnisotropy
def test_ComputeFractionalAnisotropy_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(position=-1,
    genfile=True,
    argstr='> %s',
    ),
    scheme_file=dict(position=2,
    argstr='%s',
    ),
    outputdatatype=dict(argstr='-outputdatatype %s',
    ),
    args=dict(argstr='%s',
    ),
    inputdatatype=dict(argstr='-inputdatatype %s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(position=1,
    mandatory=True,
    argstr='< %s',
    ),
    inputmodel=dict(argstr='-inputmodel %s',
    ),
    )
    inputs = ComputeFractionalAnisotropy.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_ComputeFractionalAnisotropy_outputs():
    output_map = dict(fa=dict(),
    )
    outputs = ComputeFractionalAnisotropy.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value