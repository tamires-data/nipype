# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from .....testing import assert_equal
from ..utilities import GeneratePurePlugMask


def test_GeneratePurePlugMask_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputImageModalities=dict(argstr='--inputImageModalities %s...',
    ),
    numberOfSubSamples=dict(argstr='--numberOfSubSamples %s',
    sep=',',
    ),
    outputMaskFile=dict(argstr='--outputMaskFile %s',
    hash_files=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    threshold=dict(argstr='--threshold %f',
    ),
    )
    inputs = GeneratePurePlugMask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_GeneratePurePlugMask_outputs():
    output_map = dict(outputMaskFile=dict(),
    )
    outputs = GeneratePurePlugMask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value