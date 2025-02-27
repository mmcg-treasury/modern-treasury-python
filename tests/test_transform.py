from __future__ import annotations

from typing import List, Union, Optional
from datetime import date, datetime
from typing_extensions import Required, Annotated, TypedDict

from modern_treasury._utils import PropertyInfo, transform, parse_datetime


class Foo1(TypedDict):
    foo_bar: Annotated[str, PropertyInfo(alias="fooBar")]


def test_top_level_alias() -> None:
    assert transform({"foo_bar": "hello"}, expected_type=Foo1) == {"fooBar": "hello"}


class Foo2(TypedDict):
    bar: Bar2


class Bar2(TypedDict):
    this_thing: Annotated[int, PropertyInfo(alias="this__thing")]
    baz: Annotated[Baz2, PropertyInfo(alias="Baz")]


class Baz2(TypedDict):
    my_baz: Annotated[str, PropertyInfo(alias="myBaz")]


def test_recursive_typeddict() -> None:
    assert transform({"bar": {"this_thing": 1}}, Foo2) == {"bar": {"this__thing": 1}}
    assert transform({"bar": {"baz": {"my_baz": "foo"}}}, Foo2) == {"bar": {"Baz": {"myBaz": "foo"}}}


class Foo3(TypedDict):
    things: List[Bar3]


class Bar3(TypedDict):
    my_field: Annotated[str, PropertyInfo(alias="myField")]


def test_list_of_typeddict() -> None:
    result = transform({"things": [{"my_field": "foo"}, {"my_field": "foo2"}]}, expected_type=Foo3)
    assert result == {"things": [{"myField": "foo"}, {"myField": "foo2"}]}


class Foo4(TypedDict):
    foo: Union[Bar4, Baz4]


class Bar4(TypedDict):
    foo_bar: Annotated[str, PropertyInfo(alias="fooBar")]


class Baz4(TypedDict):
    foo_baz: Annotated[str, PropertyInfo(alias="fooBaz")]


def test_union_of_typeddict() -> None:
    assert transform({"foo": {"foo_bar": "bar"}}, Foo4) == {"foo": {"fooBar": "bar"}}
    assert transform({"foo": {"foo_baz": "baz"}}, Foo4) == {"foo": {"fooBaz": "baz"}}
    assert transform({"foo": {"foo_baz": "baz", "foo_bar": "bar"}}, Foo4) == {"foo": {"fooBaz": "baz", "fooBar": "bar"}}


class Foo5(TypedDict):
    foo: Annotated[Union[Bar4, List[Baz4]], PropertyInfo(alias="FOO")]


class Bar5(TypedDict):
    foo_bar: Annotated[str, PropertyInfo(alias="fooBar")]


class Baz5(TypedDict):
    foo_baz: Annotated[str, PropertyInfo(alias="fooBaz")]


def test_union_of_list() -> None:
    assert transform({"foo": {"foo_bar": "bar"}}, Foo5) == {"FOO": {"fooBar": "bar"}}
    assert transform(
        {
            "foo": [
                {"foo_baz": "baz"},
                {"foo_baz": "baz"},
            ]
        },
        Foo5,
    ) == {"FOO": [{"fooBaz": "baz"}, {"fooBaz": "baz"}]}


class Foo6(TypedDict):
    bar: Annotated[str, PropertyInfo(alias="Bar")]


def test_includes_unknown_keys() -> None:
    assert transform({"bar": "bar", "baz_": {"FOO": 1}}, Foo6) == {
        "Bar": "bar",
        "baz_": {"FOO": 1},
    }


class Foo7(TypedDict):
    bar: Annotated[List[Bar7], PropertyInfo(alias="bAr")]
    foo: Bar7


class Bar7(TypedDict):
    foo: str


def test_ignores_invalid_input() -> None:
    assert transform({"bar": "<foo>"}, Foo7) == {"bAr": "<foo>"}
    assert transform({"foo": "<foo>"}, Foo7) == {"foo": "<foo>"}


class DatetimeDict(TypedDict, total=False):
    foo: Annotated[datetime, PropertyInfo(format="iso8601")]

    bar: Annotated[Optional[datetime], PropertyInfo(format="iso8601")]

    required: Required[Annotated[Optional[datetime], PropertyInfo(format="iso8601")]]

    list_: Required[Annotated[Optional[List[datetime]], PropertyInfo(format="iso8601")]]

    union: Annotated[Union[int, datetime], PropertyInfo(format="iso8601")]


class DateDict(TypedDict, total=False):
    foo: Annotated[date, PropertyInfo(format="iso8601")]


def test_iso8601_format() -> None:
    dt = datetime.fromisoformat("2023-02-23T14:16:36.337692+00:00")
    assert transform({"foo": dt}, DatetimeDict) == {"foo": "2023-02-23T14:16:36.337692+00:00"}  # type: ignore[comparison-overlap]

    dt = dt.replace(tzinfo=None)
    assert transform({"foo": dt}, DatetimeDict) == {"foo": "2023-02-23T14:16:36.337692"}  # type: ignore[comparison-overlap]

    assert transform({"foo": None}, DateDict) == {"foo": None}  # type: ignore[comparison-overlap]
    assert transform({"foo": date.fromisoformat("2023-02-23")}, DateDict) == {"foo": "2023-02-23"}  # type: ignore[comparison-overlap]


def test_optional_iso8601_format() -> None:
    dt = datetime.fromisoformat("2023-02-23T14:16:36.337692+00:00")
    assert transform({"bar": dt}, DatetimeDict) == {"bar": "2023-02-23T14:16:36.337692+00:00"}  # type: ignore[comparison-overlap]

    assert transform({"bar": None}, DatetimeDict) == {"bar": None}


def test_required_iso8601_format() -> None:
    dt = datetime.fromisoformat("2023-02-23T14:16:36.337692+00:00")
    assert transform({"required": dt}, DatetimeDict) == {"required": "2023-02-23T14:16:36.337692+00:00"}  # type: ignore[comparison-overlap]

    assert transform({"required": None}, DatetimeDict) == {"required": None}


def test_union_datetime() -> None:
    dt = datetime.fromisoformat("2023-02-23T14:16:36.337692+00:00")
    assert transform({"union": dt}, DatetimeDict) == {  # type: ignore[comparison-overlap]
        "union": "2023-02-23T14:16:36.337692+00:00"
    }

    assert transform({"union": "foo"}, DatetimeDict) == {"union": "foo"}


def test_nested_list_iso6801_format() -> None:
    dt1 = datetime.fromisoformat("2023-02-23T14:16:36.337692+00:00")
    dt2 = parse_datetime("2022-01-15T06:34:23Z")
    assert transform({"list_": [dt1, dt2]}, DatetimeDict) == {  # type: ignore[comparison-overlap]
        "list_": ["2023-02-23T14:16:36.337692+00:00", "2022-01-15T06:34:23+00:00"]
    }


def test_datetime_custom_format() -> None:
    dt = parse_datetime("2022-01-15T06:34:23Z")

    result = transform(dt, Annotated[datetime, PropertyInfo(format="custom", format_template="%H")])
    assert result == "06"  # type: ignore[comparison-overlap]


class DateDictWithRequiredAlias(TypedDict, total=False):
    required_prop: Required[Annotated[date, PropertyInfo(format="iso8601", alias="prop")]]


def test_datetime_with_alias() -> None:
    assert transform({"required_prop": None}, DateDictWithRequiredAlias) == {"prop": None}  # type: ignore[comparison-overlap]
    assert transform({"required_prop": date.fromisoformat("2023-02-23")}, DateDictWithRequiredAlias) == {"prop": "2023-02-23"}  # type: ignore[comparison-overlap]
