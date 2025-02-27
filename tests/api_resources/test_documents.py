# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import Document
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestDocuments:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        document = client.documents.create(
            documentable_id="string",
            documentable_type="cases",
            file=b"raw file contents",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        document = client.documents.create(
            documentable_id="string",
            documentable_type="cases",
            file=b"raw file contents",
            document_type="string",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        document = client.documents.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        document = client.documents.list()
        assert_matches_type(SyncPage[Document], document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        document = client.documents.list(
            after_cursor="string",
            documentable_id="string",
            documentable_type="cases",
            per_page=0,
        )
        assert_matches_type(SyncPage[Document], document, path=["response"])


class TestAsyncDocuments:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        document = await client.documents.create(
            documentable_id="string",
            documentable_type="cases",
            file=b"raw file contents",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        document = await client.documents.create(
            documentable_id="string",
            documentable_type="cases",
            file=b"raw file contents",
            document_type="string",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        document = await client.documents.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        document = await client.documents.list()
        assert_matches_type(AsyncPage[Document], document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        document = await client.documents.list(
            after_cursor="string",
            documentable_id="string",
            documentable_type="cases",
            per_page=0,
        )
        assert_matches_type(AsyncPage[Document], document, path=["response"])
