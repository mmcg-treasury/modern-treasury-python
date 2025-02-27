# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import RoutingDetail
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestRoutingDetails:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        routing_detail = client.routing_details.create(
            "string",
            accounts_type="external_accounts",
            routing_number="string",
            routing_number_type="aba",
        )
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        routing_detail = client.routing_details.create(
            "string",
            accounts_type="external_accounts",
            routing_number="string",
            routing_number_type="aba",
            payment_type="ach",
        )
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        routing_detail = client.routing_details.retrieve(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        routing_detail = client.routing_details.list(
            "string",
            accounts_type="external_accounts",
        )
        assert_matches_type(SyncPage[RoutingDetail], routing_detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        routing_detail = client.routing_details.list(
            "string",
            accounts_type="external_accounts",
            after_cursor="string",
            per_page=0,
        )
        assert_matches_type(SyncPage[RoutingDetail], routing_detail, path=["response"])

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        routing_detail = client.routing_details.delete(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )
        assert routing_detail is None


class TestAsyncRoutingDetails:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        routing_detail = await client.routing_details.create(
            "string",
            accounts_type="external_accounts",
            routing_number="string",
            routing_number_type="aba",
        )
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        routing_detail = await client.routing_details.create(
            "string",
            accounts_type="external_accounts",
            routing_number="string",
            routing_number_type="aba",
            payment_type="ach",
        )
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        routing_detail = await client.routing_details.retrieve(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )
        assert_matches_type(RoutingDetail, routing_detail, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        routing_detail = await client.routing_details.list(
            "string",
            accounts_type="external_accounts",
        )
        assert_matches_type(AsyncPage[RoutingDetail], routing_detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        routing_detail = await client.routing_details.list(
            "string",
            accounts_type="external_accounts",
            after_cursor="string",
            per_page=0,
        )
        assert_matches_type(AsyncPage[RoutingDetail], routing_detail, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncModernTreasury) -> None:
        routing_detail = await client.routing_details.delete(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )
        assert routing_detail is None
