from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="Schema1752844140AttrDictString1752844160")


@_attrs_define
class Schema1752844140AttrDictString1752844160:
    """ 
     """

    additional_properties: Dict[str, str] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        schema_1752844140_attr_dict_string_1752844160 = cls(
        )


        schema_1752844140_attr_dict_string_1752844160.additional_properties = d
        return schema_1752844140_attr_dict_string_1752844160

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
