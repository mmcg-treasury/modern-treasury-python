# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LedgerAccount
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLedgerAccounts:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
            currency_exponent=0,
            description="string",
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="external_account",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.retrieve(
            "string",
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_lower_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_upper_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "as_of_lock_version": 0,
            },
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.update(
            "string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.update(
            "string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.list()
        assert_matches_type(SyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.list(
            id=["string", "string", "string"],
            after_cursor="string",
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_lower_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_upper_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            currency="string",
            ledger_account_category_id="string",
            ledger_id="string",
            metadata={"foo": "string"},
            name="string",
            per_page=0,
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(SyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        ledger_account = client.ledger_accounts.delete(
            "string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])


class TestAsyncLedgerAccounts:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.create(
            currency="string",
            ledger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            normal_balance="credit",
            currency_exponent=0,
            description="string",
            ledgerable_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ledgerable_type="external_account",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.retrieve(
            "string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.retrieve(
            "string",
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_lower_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_upper_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "as_of_lock_version": 0,
            },
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.update(
            "string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.update(
            "string",
            description="string",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.list()
        assert_matches_type(AsyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.list(
            id=["string", "string", "string"],
            after_cursor="string",
            balances={
                "as_of_date": parse_date("2019-12-27"),
                "effective_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_lower_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
                "effective_at_upper_bound": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            created_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
            currency="string",
            ledger_account_category_id="string",
            ledger_id="string",
            metadata={"foo": "string"},
            name="string",
            per_page=0,
            updated_at={"foo": parse_datetime("2019-12-27T18:11:19.117Z")},
        )
        assert_matches_type(AsyncPage[LedgerAccount], ledger_account, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        ledger_account = await client.ledger_accounts.delete(
            "string",
        )
        assert_matches_type(LedgerAccount, ledger_account, path=["response"])
