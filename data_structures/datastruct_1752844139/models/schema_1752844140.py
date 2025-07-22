from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, List
from typing import cast
from typing import Union
import datetime
from typing import Dict
from dateutil.parser import isoparse

if TYPE_CHECKING:
  from ..models.schema_1752844140_attr_dict_string_1752844160 import Schema1752844140AttrDictString1752844160





T = TypeVar("T", bound="schema_1752844140")


@_attrs_define
class schema_1752844140:
    """ Описание схемы автотестом

        Attributes:
            attr_boolean_1752844144 (Union[Unset, bool]): Описание для boolean
            attr_date_1752844152 (Union[Unset, datetime.date]): Описание для date
            attr_datetime_1752844155 (Union[Unset, datetime.datetime]): Описание для datetime
            attr_dict_string_1752844160 (Union[Unset, Schema1752844140AttrDictString1752844160]):
            attr_float_1752844150 (Union[Unset, float]): Описание для float
            attr_integer_1752844147 (Union[Unset, int]): Описание для integer
            attr_list_string_1752844158 (Union[Unset, List[str]]):
            attr_string_1752844142 (Union[Unset, str]): Описание для string
     """

    attr_boolean_1752844144: Union[Unset, bool] = UNSET
    attr_date_1752844152: Union[Unset, datetime.date] = UNSET
    attr_datetime_1752844155: Union[Unset, datetime.datetime] = UNSET
    attr_dict_string_1752844160: Union[Unset, 'Schema1752844140AttrDictString1752844160'] = UNSET
    attr_float_1752844150: Union[Unset, float] = UNSET
    attr_integer_1752844147: Union[Unset, int] = UNSET
    attr_list_string_1752844158: Union[Unset, List[str]] = UNSET
    attr_string_1752844142: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.schema_1752844140_attr_dict_string_1752844160 import Schema1752844140AttrDictString1752844160
        attr_boolean_1752844144 = self.attr_boolean_1752844144

        attr_date_1752844152: Union[Unset, str] = UNSET
        if not isinstance(self.attr_date_1752844152, Unset):
            attr_date_1752844152 = self.attr_date_1752844152.isoformat()

        attr_datetime_1752844155: Union[Unset, str] = UNSET
        if not isinstance(self.attr_datetime_1752844155, Unset):
            attr_datetime_1752844155 = self.attr_datetime_1752844155.isoformat()

        attr_dict_string_1752844160: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attr_dict_string_1752844160, Unset):
            attr_dict_string_1752844160 = self.attr_dict_string_1752844160.to_dict()

        attr_float_1752844150 = self.attr_float_1752844150

        attr_integer_1752844147 = self.attr_integer_1752844147

        attr_list_string_1752844158: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attr_list_string_1752844158, Unset):
            attr_list_string_1752844158 = self.attr_list_string_1752844158



        attr_string_1752844142 = self.attr_string_1752844142


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attr_boolean_1752844144 is not UNSET:
            field_dict["attr_boolean_1752844144"] = attr_boolean_1752844144
        if attr_date_1752844152 is not UNSET:
            field_dict["attr_date_1752844152"] = attr_date_1752844152
        if attr_datetime_1752844155 is not UNSET:
            field_dict["attr_datetime_1752844155"] = attr_datetime_1752844155
        if attr_dict_string_1752844160 is not UNSET:
            field_dict["attr_dict_string_1752844160"] = attr_dict_string_1752844160
        if attr_float_1752844150 is not UNSET:
            field_dict["attr_float_1752844150"] = attr_float_1752844150
        if attr_integer_1752844147 is not UNSET:
            field_dict["attr_integer_1752844147"] = attr_integer_1752844147
        if attr_list_string_1752844158 is not UNSET:
            field_dict["attr_list_string_1752844158"] = attr_list_string_1752844158
        if attr_string_1752844142 is not UNSET:
            field_dict["attr_string_1752844142"] = attr_string_1752844142

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schema_1752844140_attr_dict_string_1752844160 import Schema1752844140AttrDictString1752844160
        d = src_dict.copy()
        attr_boolean_1752844144 = d.pop("attr_boolean_1752844144", UNSET)

        _attr_date_1752844152 = d.pop("attr_date_1752844152", UNSET)
        attr_date_1752844152: Union[Unset, datetime.date]
        if isinstance(_attr_date_1752844152,  Unset):
            attr_date_1752844152 = UNSET
        else:
            attr_date_1752844152 = isoparse(_attr_date_1752844152).date()




        _attr_datetime_1752844155 = d.pop("attr_datetime_1752844155", UNSET)
        attr_datetime_1752844155: Union[Unset, datetime.datetime]
        if isinstance(_attr_datetime_1752844155,  Unset):
            attr_datetime_1752844155 = UNSET
        else:
            attr_datetime_1752844155 = isoparse(_attr_datetime_1752844155)




        _attr_dict_string_1752844160 = d.pop("attr_dict_string_1752844160", UNSET)
        attr_dict_string_1752844160: Union[Unset, Schema1752844140AttrDictString1752844160]
        if isinstance(_attr_dict_string_1752844160,  Unset):
            attr_dict_string_1752844160 = UNSET
        else:
            attr_dict_string_1752844160 = Schema1752844140AttrDictString1752844160.from_dict(_attr_dict_string_1752844160)




        attr_float_1752844150 = d.pop("attr_float_1752844150", UNSET)

        attr_integer_1752844147 = d.pop("attr_integer_1752844147", UNSET)

        attr_list_string_1752844158 = cast(List[str], d.pop("attr_list_string_1752844158", UNSET))


        attr_string_1752844142 = d.pop("attr_string_1752844142", UNSET)

        schema_1752844140 = cls(
            attr_boolean_1752844144=attr_boolean_1752844144,
            attr_date_1752844152=attr_date_1752844152,
            attr_datetime_1752844155=attr_datetime_1752844155,
            attr_dict_string_1752844160=attr_dict_string_1752844160,
            attr_float_1752844150=attr_float_1752844150,
            attr_integer_1752844147=attr_integer_1752844147,
            attr_list_string_1752844158=attr_list_string_1752844158,
            attr_string_1752844142=attr_string_1752844142,
        )


        schema_1752844140.additional_properties = d
        return schema_1752844140

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
