"""
    Radix Core API

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import re  # noqa: F401
import sys  # noqa: F401

from core_client.model_utils import (  # noqa: F401
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
)
from ..model_utils import OpenApiModel
from core_client.exceptions import ApiAttributeError


def lazy_import():
    from core_client.model.above_maximum_validator_fee_increase_error import AboveMaximumValidatorFeeIncreaseError
    from core_client.model.below_minimum_stake_error import BelowMinimumStakeError
    from core_client.model.core_error import CoreError
    from core_client.model.data_object_not_supported_by_entity_error import DataObjectNotSupportedByEntityError
    from core_client.model.fee_construction_error import FeeConstructionError
    from core_client.model.internal_server_error import InternalServerError
    from core_client.model.invalid_address_error import InvalidAddressError
    from core_client.model.invalid_data_object_error import InvalidDataObjectError
    from core_client.model.invalid_fee_payer_entity_error import InvalidFeePayerEntityError
    from core_client.model.invalid_hex_error import InvalidHexError
    from core_client.model.invalid_json_error import InvalidJsonError
    from core_client.model.invalid_partial_state_identifier_error import InvalidPartialStateIdentifierError
    from core_client.model.invalid_public_key_error import InvalidPublicKeyError
    from core_client.model.invalid_signature_error import InvalidSignatureError
    from core_client.model.invalid_sub_entity_error import InvalidSubEntityError
    from core_client.model.invalid_transaction_error import InvalidTransactionError
    from core_client.model.invalid_transaction_hash_error import InvalidTransactionHashError
    from core_client.model.mempool_full_error import MempoolFullError
    from core_client.model.message_too_long_error import MessageTooLongError
    from core_client.model.network_not_supported_error import NetworkNotSupportedError
    from core_client.model.not_enough_native_tokens_for_fees_error import NotEnoughNativeTokensForFeesError
    from core_client.model.not_enough_resources_error import NotEnoughResourcesError
    from core_client.model.not_validator_entity_error import NotValidatorEntityError
    from core_client.model.not_validator_owner_error import NotValidatorOwnerError
    from core_client.model.public_key_not_supported_error import PublicKeyNotSupportedError
    from core_client.model.resource_deposit_operation_not_supported_by_entity_error import ResourceDepositOperationNotSupportedByEntityError
    from core_client.model.resource_withdraw_operation_not_supported_by_entity_error import ResourceWithdrawOperationNotSupportedByEntityError
    from core_client.model.state_identifier_not_found_error import StateIdentifierNotFoundError
    from core_client.model.substate_dependency_not_found_error import SubstateDependencyNotFoundError
    from core_client.model.transaction_identifier import TransactionIdentifier
    from core_client.model.transaction_not_found_error import TransactionNotFoundError
    from core_client.model.transaction_not_found_error_all_of import TransactionNotFoundErrorAllOf
    globals()['AboveMaximumValidatorFeeIncreaseError'] = AboveMaximumValidatorFeeIncreaseError
    globals()['BelowMinimumStakeError'] = BelowMinimumStakeError
    globals()['CoreError'] = CoreError
    globals()['DataObjectNotSupportedByEntityError'] = DataObjectNotSupportedByEntityError
    globals()['FeeConstructionError'] = FeeConstructionError
    globals()['InternalServerError'] = InternalServerError
    globals()['InvalidAddressError'] = InvalidAddressError
    globals()['InvalidDataObjectError'] = InvalidDataObjectError
    globals()['InvalidFeePayerEntityError'] = InvalidFeePayerEntityError
    globals()['InvalidHexError'] = InvalidHexError
    globals()['InvalidJsonError'] = InvalidJsonError
    globals()['InvalidPartialStateIdentifierError'] = InvalidPartialStateIdentifierError
    globals()['InvalidPublicKeyError'] = InvalidPublicKeyError
    globals()['InvalidSignatureError'] = InvalidSignatureError
    globals()['InvalidSubEntityError'] = InvalidSubEntityError
    globals()['InvalidTransactionError'] = InvalidTransactionError
    globals()['InvalidTransactionHashError'] = InvalidTransactionHashError
    globals()['MempoolFullError'] = MempoolFullError
    globals()['MessageTooLongError'] = MessageTooLongError
    globals()['NetworkNotSupportedError'] = NetworkNotSupportedError
    globals()['NotEnoughNativeTokensForFeesError'] = NotEnoughNativeTokensForFeesError
    globals()['NotEnoughResourcesError'] = NotEnoughResourcesError
    globals()['NotValidatorEntityError'] = NotValidatorEntityError
    globals()['NotValidatorOwnerError'] = NotValidatorOwnerError
    globals()['PublicKeyNotSupportedError'] = PublicKeyNotSupportedError
    globals()['ResourceDepositOperationNotSupportedByEntityError'] = ResourceDepositOperationNotSupportedByEntityError
    globals()['ResourceWithdrawOperationNotSupportedByEntityError'] = ResourceWithdrawOperationNotSupportedByEntityError
    globals()['StateIdentifierNotFoundError'] = StateIdentifierNotFoundError
    globals()['SubstateDependencyNotFoundError'] = SubstateDependencyNotFoundError
    globals()['TransactionIdentifier'] = TransactionIdentifier
    globals()['TransactionNotFoundError'] = TransactionNotFoundError
    globals()['TransactionNotFoundErrorAllOf'] = TransactionNotFoundErrorAllOf


class TransactionNotFoundError(ModelNormal):
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
            'transaction_identifier': (TransactionIdentifier,),  # noqa: E501
            'type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        lazy_import()
        val = {
            'AboveMaximumValidatorFeeIncreaseError': AboveMaximumValidatorFeeIncreaseError,
            'BelowMinimumStakeError': BelowMinimumStakeError,
            'DataObjectNotSupportedByEntityError': DataObjectNotSupportedByEntityError,
            'FeeConstructionError': FeeConstructionError,
            'InternalServerError': InternalServerError,
            'InvalidAddressError': InvalidAddressError,
            'InvalidDataObjectError': InvalidDataObjectError,
            'InvalidFeePayerEntityError': InvalidFeePayerEntityError,
            'InvalidHexError': InvalidHexError,
            'InvalidJsonError': InvalidJsonError,
            'InvalidPartialStateIdentifierError': InvalidPartialStateIdentifierError,
            'InvalidPublicKeyError': InvalidPublicKeyError,
            'InvalidSignatureError': InvalidSignatureError,
            'InvalidSubEntityError': InvalidSubEntityError,
            'InvalidTransactionError': InvalidTransactionError,
            'InvalidTransactionHashError': InvalidTransactionHashError,
            'MempoolFullError': MempoolFullError,
            'MessageTooLongError': MessageTooLongError,
            'NetworkNotSupportedError': NetworkNotSupportedError,
            'NotEnoughNativeTokensForFeesError': NotEnoughNativeTokensForFeesError,
            'NotEnoughResourcesError': NotEnoughResourcesError,
            'NotValidatorEntityError': NotValidatorEntityError,
            'NotValidatorOwnerError': NotValidatorOwnerError,
            'PublicKeyNotSupportedError': PublicKeyNotSupportedError,
            'ResourceDepositOperationNotSupportedByEntityError': ResourceDepositOperationNotSupportedByEntityError,
            'ResourceWithdrawOperationNotSupportedByEntityError': ResourceWithdrawOperationNotSupportedByEntityError,
            'StateIdentifierNotFoundError': StateIdentifierNotFoundError,
            'SubstateDependencyNotFoundError': SubstateDependencyNotFoundError,
            'TransactionNotFoundError': TransactionNotFoundError,
        }
        if not val:
            return None
        return {'type': val}

    attribute_map = {
        'transaction_identifier': 'transaction_identifier',  # noqa: E501
        'type': 'type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, transaction_identifier, type, *args, **kwargs):  # noqa: E501
        """TransactionNotFoundError - a model defined in OpenAPI

        Args:
            transaction_identifier (TransactionIdentifier):
            type (str):

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
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
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

        self.transaction_identifier = transaction_identifier
        self.type = type
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
    def __init__(self, transaction_identifier, type, *args, **kwargs):  # noqa: E501
        """TransactionNotFoundError - a model defined in OpenAPI

        Args:
            transaction_identifier (TransactionIdentifier):
            type (str):

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
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
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

        self.transaction_identifier = transaction_identifier
        self.type = type
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
