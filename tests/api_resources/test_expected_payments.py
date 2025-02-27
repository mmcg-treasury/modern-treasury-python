# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import ExpectedPayment
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestExpectedPayments:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.create(
            amount_lower_bound=0,
            amount_upper_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.create(
            amount_lower_bound=0,
            amount_upper_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="AED",
            date_lower_bound=parse_date("2019-12-27"),
            date_upper_bound=parse_date("2019-12-27"),
            description="string",
            line_items=[
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "string",
                    "accounting_category_id": "string",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "string",
                    "accounting_category_id": "string",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "string",
                    "accounting_category_id": "string",
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            reconciliation_filters={},
            reconciliation_groups={},
            remittance_information="string",
            statement_descriptor="string",
            type="ach",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.retrieve(
            "string",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.update(
            "string",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.update(
            "string",
            amount_lower_bound=0,
            amount_upper_bound=0,
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="AED",
            date_lower_bound=parse_date("2019-12-27"),
            date_upper_bound=parse_date("2019-12-27"),
            description="string",
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            reconciliation_filters={},
            reconciliation_groups={},
            remittance_information="string",
            statement_descriptor="string",
            type="ach",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.list()
        assert_matches_type(SyncPage[ExpectedPayment], expected_payment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.list(
            after_cursor="string",
            counterparty_id="string",
            created_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="credit",
            internal_account_id="string",
            metadata={"foo": "string"},
            per_page=0,
            status="archived",
            type="ach",
        )
        assert_matches_type(SyncPage[ExpectedPayment], expected_payment, path=["response"])

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        expected_payment = client.expected_payments.delete(
            "string",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])


class TestAsyncExpectedPayments:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        expected_payment = await client.expected_payments.create(
            amount_lower_bound=0,
            amount_upper_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        expected_payment = await client.expected_payments.create(
            amount_lower_bound=0,
            amount_upper_bound=0,
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="AED",
            date_lower_bound=parse_date("2019-12-27"),
            date_upper_bound=parse_date("2019-12-27"),
            description="string",
            line_items=[
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "string",
                    "accounting_category_id": "string",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "string",
                    "accounting_category_id": "string",
                },
                {
                    "amount": 0,
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "description": "string",
                    "accounting_category_id": "string",
                },
            ],
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            reconciliation_filters={},
            reconciliation_groups={},
            remittance_information="string",
            statement_descriptor="string",
            type="ach",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        expected_payment = await client.expected_payments.retrieve(
            "string",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        expected_payment = await client.expected_payments.update(
            "string",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        expected_payment = await client.expected_payments.update(
            "string",
            amount_lower_bound=0,
            amount_upper_bound=0,
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            currency="AED",
            date_lower_bound=parse_date("2019-12-27"),
            date_upper_bound=parse_date("2019-12-27"),
            description="string",
            direction="credit",
            internal_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            reconciliation_filters={},
            reconciliation_groups={},
            remittance_information="string",
            statement_descriptor="string",
            type="ach",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        expected_payment = await client.expected_payments.list()
        assert_matches_type(AsyncPage[ExpectedPayment], expected_payment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        expected_payment = await client.expected_payments.list(
            after_cursor="string",
            counterparty_id="string",
            created_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="credit",
            internal_account_id="string",
            metadata={"foo": "string"},
            per_page=0,
            status="archived",
            type="ach",
        )
        assert_matches_type(AsyncPage[ExpectedPayment], expected_payment, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        expected_payment = await client.expected_payments.delete(
            "string",
        )
        assert_matches_type(ExpectedPayment, expected_payment, path=["response"])
