from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from ..types import UNSET, Unset
from typing import Dict
from typing import Union

if TYPE_CHECKING:
  from ..models.schema_1752844140 import schema_1752844140





T = TypeVar("T", bound="test")


@_attrs_define
class test:
    """ 
        Attributes:
            atr (Union[Unset, schema_1752844140]): Описание схемы автотестом
     """

    atr: Union[Unset, 'schema_1752844140'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.schema_1752844140 import schema_1752844140
        atr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.atr, Unset):
            atr = self.atr.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if atr is not UNSET:
            field_dict["atr"] = atr

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schema_1752844140 import schema_1752844140
        d = src_dict.copy()
        _atr = d.pop("atr", UNSET)
        atr: Union[Unset, schema_1752844140]
        if isinstance(_atr,  Unset):
            atr = UNSET
        else:
            atr = schema_1752844140.from_dict(_atr)




        test = cls(
            atr=atr,
        )


        test.additional_properties = d
        return test

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
