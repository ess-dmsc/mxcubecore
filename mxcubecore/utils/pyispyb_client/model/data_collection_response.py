"""
    py-ISPyB

    FastAPI Prototype  # noqa: E501

    The version of the OpenAPI document: 0.1alpha
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from mxcubecore.utils.pyispyb_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from mxcubecore.utils.pyispyb_client.exceptions import ApiAttributeError


def lazy_import():
    from mxcubecore.utils.pyispyb_client.model.detector import Detector
    from mxcubecore.utils.pyispyb_client.model.pydantic_main_data_collection_group import PydanticMainDataCollectionGroup
    globals()['Detector'] = Detector
    globals()['PydanticMainDataCollectionGroup'] = PydanticMainDataCollectionGroup


class DataCollectionResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'data_collection_id': (int,),  # noqa: E501
            'data_collection_group_id': (int,),  # noqa: E501
            'data_collection_group': (PydanticMainDataCollectionGroup,),  # noqa: E501
            'strategy_sub_wedge_orig_id': (int,),  # noqa: E501
            'detector_id': (int,),  # noqa: E501
            'bl_sub_sample_id': (int,),  # noqa: E501
            'start_position_id': (int,),  # noqa: E501
            'end_position_id': (int,),  # noqa: E501
            'data_collection_number': (int,),  # noqa: E501
            'start_time': (datetime,),  # noqa: E501
            'end_time': (datetime,),  # noqa: E501
            'run_status': (str,),  # noqa: E501
            'axis_start': (float,),  # noqa: E501
            'axis_end': (float,),  # noqa: E501
            'axis_range': (float,),  # noqa: E501
            'overlap': (float,),  # noqa: E501
            'number_of_images': (int,),  # noqa: E501
            'start_image_number': (int,),  # noqa: E501
            'number_of_passes': (int,),  # noqa: E501
            'exposure_time': (float,),  # noqa: E501
            'image_directory': (str,),  # noqa: E501
            'image_prefix': (str,),  # noqa: E501
            'image_suffix': (str,),  # noqa: E501
            'image_container_sub_path': (str,),  # noqa: E501
            'file_template': (str,),  # noqa: E501
            'wavelength': (float,),  # noqa: E501
            'resolution': (float,),  # noqa: E501
            'detector_distance': (float,),  # noqa: E501
            'x_beam': (float,),  # noqa: E501
            'y_beam': (float,),  # noqa: E501
            'x_beam_pix': (float,),  # noqa: E501
            'y_beam_pix': (float,),  # noqa: E501
            'comments': (str,),  # noqa: E501
            'printable_for_report': (int,),  # noqa: E501
            'slit_gap_vertical': (float,),  # noqa: E501
            'slit_gap_horizontal': (float,),  # noqa: E501
            'transmission': (float,),  # noqa: E501
            'synchrotron_mode': (str,),  # noqa: E501
            'xtal_snapshot_full_path1': (str,),  # noqa: E501
            'xtal_snapshot_full_path2': (str,),  # noqa: E501
            'xtal_snapshot_full_path3': (str,),  # noqa: E501
            'xtal_snapshot_full_path4': (str,),  # noqa: E501
            'rotation_axis': (str,),  # noqa: E501
            'phi_start': (float,),  # noqa: E501
            'kappa_start': (float,),  # noqa: E501
            'omega_start': (float,),  # noqa: E501
            'resolution_at_corner': (float,),  # noqa: E501
            'detector2_theta': (float,),  # noqa: E501
            'undulator_gap1': (float,),  # noqa: E501
            'undulator_gap2': (float,),  # noqa: E501
            'undulator_gap3': (float,),  # noqa: E501
            'beam_size_at_sample_x': (float,),  # noqa: E501
            'beam_size_at_sample_y': (float,),  # noqa: E501
            'centering_method': (str,),  # noqa: E501
            'average_temperature': (float,),  # noqa: E501
            'actual_centering_position': (str,),  # noqa: E501
            'beam_shape': (str,),  # noqa: E501
            'flux': (float,),  # noqa: E501
            'flux_end': (float,),  # noqa: E501
            'total_absorbed_dose': (float,),  # noqa: E501
            'best_wilson_plot_path': (str,),  # noqa: E501
            'image_quality_indicators_plot_path': (str,),  # noqa: E501
            'image_quality_indicators_csv_path': (str,),  # noqa: E501
            'bl_sample_id': (int,),  # noqa: E501
            'session_id': (int,),  # noqa: E501
            'experiment_type': (str,),  # noqa: E501
            'crystal_class': (str,),  # noqa: E501
            'chi_start': (float,),  # noqa: E501
            'detector_mode': (str,),  # noqa: E501
            'actual_sample_barcode': (str,),  # noqa: E501
            'actual_sample_slot_in_container': (int,),  # noqa: E501
            'actual_container_barcode': (str,),  # noqa: E501
            'actual_container_slot_in_sc': (int,),  # noqa: E501
            'position_id': (int,),  # noqa: E501
            'focal_spot_size_at_sample_x': (float,),  # noqa: E501
            'polarisation': (float,),  # noqa: E501
            'focal_spot_size_at_sample_y': (float,),  # noqa: E501
            'aperture_id': (int,),  # noqa: E501
            'screening_orig_id': (int,),  # noqa: E501
            'processed_data_file': (str,),  # noqa: E501
            'dat_full_path': (str,),  # noqa: E501
            'magnification': (int,),  # noqa: E501
            'binning': (int,),  # noqa: E501
            'particle_diameter': (float,),  # noqa: E501
            'box_size_ctf': (float,),  # noqa: E501
            'min_resolution': (float,),  # noqa: E501
            'min_defocus': (float,),  # noqa: E501
            'max_defocus': (float,),  # noqa: E501
            'defocus_step_size': (float,),  # noqa: E501
            'amount_astigmatism': (float,),  # noqa: E501
            'extract_size': (float,),  # noqa: E501
            'bg_radius': (float,),  # noqa: E501
            'voltage': (float,),  # noqa: E501
            'obj_aperture': (float,),  # noqa: E501
            'c1aperture': (float,),  # noqa: E501
            'c2aperture': (float,),  # noqa: E501
            'c3aperture': (float,),  # noqa: E501
            'c1lens': (float,),  # noqa: E501
            'c2lens': (float,),  # noqa: E501
            'c3lens': (float,),  # noqa: E501
            'detector': (Detector,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'data_collection_id': 'dataCollectionId',  # noqa: E501
        'data_collection_group_id': 'dataCollectionGroupId',  # noqa: E501
        'data_collection_group': 'DataCollectionGroup',  # noqa: E501
        'strategy_sub_wedge_orig_id': 'strategySubWedgeOrigId',  # noqa: E501
        'detector_id': 'detectorId',  # noqa: E501
        'bl_sub_sample_id': 'blSubSampleId',  # noqa: E501
        'start_position_id': 'startPositionId',  # noqa: E501
        'end_position_id': 'endPositionId',  # noqa: E501
        'data_collection_number': 'dataCollectionNumber',  # noqa: E501
        'start_time': 'startTime',  # noqa: E501
        'end_time': 'endTime',  # noqa: E501
        'run_status': 'runStatus',  # noqa: E501
        'axis_start': 'axisStart',  # noqa: E501
        'axis_end': 'axisEnd',  # noqa: E501
        'axis_range': 'axisRange',  # noqa: E501
        'overlap': 'overlap',  # noqa: E501
        'number_of_images': 'numberOfImages',  # noqa: E501
        'start_image_number': 'startImageNumber',  # noqa: E501
        'number_of_passes': 'numberOfPasses',  # noqa: E501
        'exposure_time': 'exposureTime',  # noqa: E501
        'image_directory': 'imageDirectory',  # noqa: E501
        'image_prefix': 'imagePrefix',  # noqa: E501
        'image_suffix': 'imageSuffix',  # noqa: E501
        'image_container_sub_path': 'imageContainerSubPath',  # noqa: E501
        'file_template': 'fileTemplate',  # noqa: E501
        'wavelength': 'wavelength',  # noqa: E501
        'resolution': 'resolution',  # noqa: E501
        'detector_distance': 'detectorDistance',  # noqa: E501
        'x_beam': 'xBeam',  # noqa: E501
        'y_beam': 'yBeam',  # noqa: E501
        'x_beam_pix': 'xBeamPix',  # noqa: E501
        'y_beam_pix': 'yBeamPix',  # noqa: E501
        'comments': 'comments',  # noqa: E501
        'printable_for_report': 'printableForReport',  # noqa: E501
        'slit_gap_vertical': 'slitGapVertical',  # noqa: E501
        'slit_gap_horizontal': 'slitGapHorizontal',  # noqa: E501
        'transmission': 'transmission',  # noqa: E501
        'synchrotron_mode': 'synchrotronMode',  # noqa: E501
        'xtal_snapshot_full_path1': 'xtalSnapshotFullPath1',  # noqa: E501
        'xtal_snapshot_full_path2': 'xtalSnapshotFullPath2',  # noqa: E501
        'xtal_snapshot_full_path3': 'xtalSnapshotFullPath3',  # noqa: E501
        'xtal_snapshot_full_path4': 'xtalSnapshotFullPath4',  # noqa: E501
        'rotation_axis': 'rotationAxis',  # noqa: E501
        'phi_start': 'phiStart',  # noqa: E501
        'kappa_start': 'kappaStart',  # noqa: E501
        'omega_start': 'omegaStart',  # noqa: E501
        'resolution_at_corner': 'resolutionAtCorner',  # noqa: E501
        'detector2_theta': 'detector2Theta',  # noqa: E501
        'undulator_gap1': 'undulatorGap1',  # noqa: E501
        'undulator_gap2': 'undulatorGap2',  # noqa: E501
        'undulator_gap3': 'undulatorGap3',  # noqa: E501
        'beam_size_at_sample_x': 'beamSizeAtSampleX',  # noqa: E501
        'beam_size_at_sample_y': 'beamSizeAtSampleY',  # noqa: E501
        'centering_method': 'centeringMethod',  # noqa: E501
        'average_temperature': 'averageTemperature',  # noqa: E501
        'actual_centering_position': 'actualCenteringPosition',  # noqa: E501
        'beam_shape': 'beamShape',  # noqa: E501
        'flux': 'flux',  # noqa: E501
        'flux_end': 'flux_end',  # noqa: E501
        'total_absorbed_dose': 'totalAbsorbedDose',  # noqa: E501
        'best_wilson_plot_path': 'bestWilsonPlotPath',  # noqa: E501
        'image_quality_indicators_plot_path': 'imageQualityIndicatorsPlotPath',  # noqa: E501
        'image_quality_indicators_csv_path': 'imageQualityIndicatorsCSVPath',  # noqa: E501
        'bl_sample_id': 'blSampleId',  # noqa: E501
        'session_id': 'sessionId',  # noqa: E501
        'experiment_type': 'experimentType',  # noqa: E501
        'crystal_class': 'crystalClass',  # noqa: E501
        'chi_start': 'chiStart',  # noqa: E501
        'detector_mode': 'detectorMode',  # noqa: E501
        'actual_sample_barcode': 'actualSampleBarcode',  # noqa: E501
        'actual_sample_slot_in_container': 'actualSampleSlotInContainer',  # noqa: E501
        'actual_container_barcode': 'actualContainerBarcode',  # noqa: E501
        'actual_container_slot_in_sc': 'actualContainerSlotInSC',  # noqa: E501
        'position_id': 'positionId',  # noqa: E501
        'focal_spot_size_at_sample_x': 'focalSpotSizeAtSampleX',  # noqa: E501
        'polarisation': 'polarisation',  # noqa: E501
        'focal_spot_size_at_sample_y': 'focalSpotSizeAtSampleY',  # noqa: E501
        'aperture_id': 'apertureId',  # noqa: E501
        'screening_orig_id': 'screeningOrigId',  # noqa: E501
        'processed_data_file': 'processedDataFile',  # noqa: E501
        'dat_full_path': 'datFullPath',  # noqa: E501
        'magnification': 'magnification',  # noqa: E501
        'binning': 'binning',  # noqa: E501
        'particle_diameter': 'particleDiameter',  # noqa: E501
        'box_size_ctf': 'boxSize_CTF',  # noqa: E501
        'min_resolution': 'minResolution',  # noqa: E501
        'min_defocus': 'minDefocus',  # noqa: E501
        'max_defocus': 'maxDefocus',  # noqa: E501
        'defocus_step_size': 'defocusStepSize',  # noqa: E501
        'amount_astigmatism': 'amountAstigmatism',  # noqa: E501
        'extract_size': 'extractSize',  # noqa: E501
        'bg_radius': 'bgRadius',  # noqa: E501
        'voltage': 'voltage',  # noqa: E501
        'obj_aperture': 'objAperture',  # noqa: E501
        'c1aperture': 'c1aperture',  # noqa: E501
        'c2aperture': 'c2aperture',  # noqa: E501
        'c3aperture': 'c3aperture',  # noqa: E501
        'c1lens': 'c1lens',  # noqa: E501
        'c2lens': 'c2lens',  # noqa: E501
        'c3lens': 'c3lens',  # noqa: E501
        'detector': 'Detector',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, data_collection_id, data_collection_group_id, data_collection_group, *args, **kwargs):  # noqa: E501
        """DataCollectionResponse - a model defined in OpenAPI

        Args:
            data_collection_id (int):
            data_collection_group_id (int):
            data_collection_group (PydanticMainDataCollectionGroup):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            strategy_sub_wedge_orig_id (int): [optional]  # noqa: E501
            detector_id (int): [optional]  # noqa: E501
            bl_sub_sample_id (int): [optional]  # noqa: E501
            start_position_id (int): [optional]  # noqa: E501
            end_position_id (int): [optional]  # noqa: E501
            data_collection_number (int): [optional]  # noqa: E501
            start_time (datetime): [optional]  # noqa: E501
            end_time (datetime): [optional]  # noqa: E501
            run_status (str): [optional]  # noqa: E501
            axis_start (float): [optional]  # noqa: E501
            axis_end (float): [optional]  # noqa: E501
            axis_range (float): [optional]  # noqa: E501
            overlap (float): [optional]  # noqa: E501
            number_of_images (int): [optional]  # noqa: E501
            start_image_number (int): [optional]  # noqa: E501
            number_of_passes (int): [optional]  # noqa: E501
            exposure_time (float): [optional]  # noqa: E501
            image_directory (str): [optional]  # noqa: E501
            image_prefix (str): [optional]  # noqa: E501
            image_suffix (str): [optional]  # noqa: E501
            image_container_sub_path (str): [optional]  # noqa: E501
            file_template (str): [optional]  # noqa: E501
            wavelength (float): [optional]  # noqa: E501
            resolution (float): [optional]  # noqa: E501
            detector_distance (float): [optional]  # noqa: E501
            x_beam (float): [optional]  # noqa: E501
            y_beam (float): [optional]  # noqa: E501
            x_beam_pix (float): [optional]  # noqa: E501
            y_beam_pix (float): [optional]  # noqa: E501
            comments (str): [optional]  # noqa: E501
            printable_for_report (int): [optional]  # noqa: E501
            slit_gap_vertical (float): [optional]  # noqa: E501
            slit_gap_horizontal (float): [optional]  # noqa: E501
            transmission (float): [optional]  # noqa: E501
            synchrotron_mode (str): [optional]  # noqa: E501
            xtal_snapshot_full_path1 (str): [optional]  # noqa: E501
            xtal_snapshot_full_path2 (str): [optional]  # noqa: E501
            xtal_snapshot_full_path3 (str): [optional]  # noqa: E501
            xtal_snapshot_full_path4 (str): [optional]  # noqa: E501
            rotation_axis (str): [optional]  # noqa: E501
            phi_start (float): [optional]  # noqa: E501
            kappa_start (float): [optional]  # noqa: E501
            omega_start (float): [optional]  # noqa: E501
            resolution_at_corner (float): [optional]  # noqa: E501
            detector2_theta (float): [optional]  # noqa: E501
            undulator_gap1 (float): [optional]  # noqa: E501
            undulator_gap2 (float): [optional]  # noqa: E501
            undulator_gap3 (float): [optional]  # noqa: E501
            beam_size_at_sample_x (float): [optional]  # noqa: E501
            beam_size_at_sample_y (float): [optional]  # noqa: E501
            centering_method (str): [optional]  # noqa: E501
            average_temperature (float): [optional]  # noqa: E501
            actual_centering_position (str): [optional]  # noqa: E501
            beam_shape (str): [optional]  # noqa: E501
            flux (float): [optional]  # noqa: E501
            flux_end (float): [optional]  # noqa: E501
            total_absorbed_dose (float): [optional]  # noqa: E501
            best_wilson_plot_path (str): [optional]  # noqa: E501
            image_quality_indicators_plot_path (str): [optional]  # noqa: E501
            image_quality_indicators_csv_path (str): [optional]  # noqa: E501
            bl_sample_id (int): [optional]  # noqa: E501
            session_id (int): [optional]  # noqa: E501
            experiment_type (str): [optional]  # noqa: E501
            crystal_class (str): [optional]  # noqa: E501
            chi_start (float): [optional]  # noqa: E501
            detector_mode (str): [optional]  # noqa: E501
            actual_sample_barcode (str): [optional]  # noqa: E501
            actual_sample_slot_in_container (int): [optional]  # noqa: E501
            actual_container_barcode (str): [optional]  # noqa: E501
            actual_container_slot_in_sc (int): [optional]  # noqa: E501
            position_id (int): [optional]  # noqa: E501
            focal_spot_size_at_sample_x (float): [optional]  # noqa: E501
            polarisation (float): [optional]  # noqa: E501
            focal_spot_size_at_sample_y (float): [optional]  # noqa: E501
            aperture_id (int): [optional]  # noqa: E501
            screening_orig_id (int): [optional]  # noqa: E501
            processed_data_file (str): [optional]  # noqa: E501
            dat_full_path (str): [optional]  # noqa: E501
            magnification (int): [optional]  # noqa: E501
            binning (int): [optional]  # noqa: E501
            particle_diameter (float): [optional]  # noqa: E501
            box_size_ctf (float): [optional]  # noqa: E501
            min_resolution (float): [optional]  # noqa: E501
            min_defocus (float): [optional]  # noqa: E501
            max_defocus (float): [optional]  # noqa: E501
            defocus_step_size (float): [optional]  # noqa: E501
            amount_astigmatism (float): [optional]  # noqa: E501
            extract_size (float): [optional]  # noqa: E501
            bg_radius (float): [optional]  # noqa: E501
            voltage (float): [optional]  # noqa: E501
            obj_aperture (float): [optional]  # noqa: E501
            c1aperture (float): [optional]  # noqa: E501
            c2aperture (float): [optional]  # noqa: E501
            c3aperture (float): [optional]  # noqa: E501
            c1lens (float): [optional]  # noqa: E501
            c2lens (float): [optional]  # noqa: E501
            c3lens (float): [optional]  # noqa: E501
            detector (Detector): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.data_collection_id = data_collection_id
        self.data_collection_group_id = data_collection_group_id
        self.data_collection_group = data_collection_group
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, data_collection_id, data_collection_group_id, data_collection_group, *args, **kwargs):  # noqa: E501
        """DataCollectionResponse - a model defined in OpenAPI

        Args:
            data_collection_id (int):
            data_collection_group_id (int):
            data_collection_group (PydanticMainDataCollectionGroup):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            strategy_sub_wedge_orig_id (int): [optional]  # noqa: E501
            detector_id (int): [optional]  # noqa: E501
            bl_sub_sample_id (int): [optional]  # noqa: E501
            start_position_id (int): [optional]  # noqa: E501
            end_position_id (int): [optional]  # noqa: E501
            data_collection_number (int): [optional]  # noqa: E501
            start_time (datetime): [optional]  # noqa: E501
            end_time (datetime): [optional]  # noqa: E501
            run_status (str): [optional]  # noqa: E501
            axis_start (float): [optional]  # noqa: E501
            axis_end (float): [optional]  # noqa: E501
            axis_range (float): [optional]  # noqa: E501
            overlap (float): [optional]  # noqa: E501
            number_of_images (int): [optional]  # noqa: E501
            start_image_number (int): [optional]  # noqa: E501
            number_of_passes (int): [optional]  # noqa: E501
            exposure_time (float): [optional]  # noqa: E501
            image_directory (str): [optional]  # noqa: E501
            image_prefix (str): [optional]  # noqa: E501
            image_suffix (str): [optional]  # noqa: E501
            image_container_sub_path (str): [optional]  # noqa: E501
            file_template (str): [optional]  # noqa: E501
            wavelength (float): [optional]  # noqa: E501
            resolution (float): [optional]  # noqa: E501
            detector_distance (float): [optional]  # noqa: E501
            x_beam (float): [optional]  # noqa: E501
            y_beam (float): [optional]  # noqa: E501
            x_beam_pix (float): [optional]  # noqa: E501
            y_beam_pix (float): [optional]  # noqa: E501
            comments (str): [optional]  # noqa: E501
            printable_for_report (int): [optional]  # noqa: E501
            slit_gap_vertical (float): [optional]  # noqa: E501
            slit_gap_horizontal (float): [optional]  # noqa: E501
            transmission (float): [optional]  # noqa: E501
            synchrotron_mode (str): [optional]  # noqa: E501
            xtal_snapshot_full_path1 (str): [optional]  # noqa: E501
            xtal_snapshot_full_path2 (str): [optional]  # noqa: E501
            xtal_snapshot_full_path3 (str): [optional]  # noqa: E501
            xtal_snapshot_full_path4 (str): [optional]  # noqa: E501
            rotation_axis (str): [optional]  # noqa: E501
            phi_start (float): [optional]  # noqa: E501
            kappa_start (float): [optional]  # noqa: E501
            omega_start (float): [optional]  # noqa: E501
            resolution_at_corner (float): [optional]  # noqa: E501
            detector2_theta (float): [optional]  # noqa: E501
            undulator_gap1 (float): [optional]  # noqa: E501
            undulator_gap2 (float): [optional]  # noqa: E501
            undulator_gap3 (float): [optional]  # noqa: E501
            beam_size_at_sample_x (float): [optional]  # noqa: E501
            beam_size_at_sample_y (float): [optional]  # noqa: E501
            centering_method (str): [optional]  # noqa: E501
            average_temperature (float): [optional]  # noqa: E501
            actual_centering_position (str): [optional]  # noqa: E501
            beam_shape (str): [optional]  # noqa: E501
            flux (float): [optional]  # noqa: E501
            flux_end (float): [optional]  # noqa: E501
            total_absorbed_dose (float): [optional]  # noqa: E501
            best_wilson_plot_path (str): [optional]  # noqa: E501
            image_quality_indicators_plot_path (str): [optional]  # noqa: E501
            image_quality_indicators_csv_path (str): [optional]  # noqa: E501
            bl_sample_id (int): [optional]  # noqa: E501
            session_id (int): [optional]  # noqa: E501
            experiment_type (str): [optional]  # noqa: E501
            crystal_class (str): [optional]  # noqa: E501
            chi_start (float): [optional]  # noqa: E501
            detector_mode (str): [optional]  # noqa: E501
            actual_sample_barcode (str): [optional]  # noqa: E501
            actual_sample_slot_in_container (int): [optional]  # noqa: E501
            actual_container_barcode (str): [optional]  # noqa: E501
            actual_container_slot_in_sc (int): [optional]  # noqa: E501
            position_id (int): [optional]  # noqa: E501
            focal_spot_size_at_sample_x (float): [optional]  # noqa: E501
            polarisation (float): [optional]  # noqa: E501
            focal_spot_size_at_sample_y (float): [optional]  # noqa: E501
            aperture_id (int): [optional]  # noqa: E501
            screening_orig_id (int): [optional]  # noqa: E501
            processed_data_file (str): [optional]  # noqa: E501
            dat_full_path (str): [optional]  # noqa: E501
            magnification (int): [optional]  # noqa: E501
            binning (int): [optional]  # noqa: E501
            particle_diameter (float): [optional]  # noqa: E501
            box_size_ctf (float): [optional]  # noqa: E501
            min_resolution (float): [optional]  # noqa: E501
            min_defocus (float): [optional]  # noqa: E501
            max_defocus (float): [optional]  # noqa: E501
            defocus_step_size (float): [optional]  # noqa: E501
            amount_astigmatism (float): [optional]  # noqa: E501
            extract_size (float): [optional]  # noqa: E501
            bg_radius (float): [optional]  # noqa: E501
            voltage (float): [optional]  # noqa: E501
            obj_aperture (float): [optional]  # noqa: E501
            c1aperture (float): [optional]  # noqa: E501
            c2aperture (float): [optional]  # noqa: E501
            c3aperture (float): [optional]  # noqa: E501
            c1lens (float): [optional]  # noqa: E501
            c2lens (float): [optional]  # noqa: E501
            c3lens (float): [optional]  # noqa: E501
            detector (Detector): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.data_collection_id = data_collection_id
        self.data_collection_group_id = data_collection_group_id
        self.data_collection_group = data_collection_group
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
