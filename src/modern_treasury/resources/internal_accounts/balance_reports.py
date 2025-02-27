# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.internal_accounts import BalanceReport, balance_report_list_params

__all__ = ["BalanceReports", "AsyncBalanceReports"]


class BalanceReports(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        internal_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> BalanceReport:
        """
        Get a single balance report for a given internal account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/internal_accounts/{internal_account_id}/balance_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceReport,
        )

    def list(
        self,
        internal_account_id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_date: Union[str, date] | NotGiven = NOT_GIVEN,
        balance_report_type: Literal["intraday", "other", "previous_day", "real_time"] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[BalanceReport]:
        """
        Get all balance reports for a given internal account.

        Args:
          as_of_date: The date of the balance report in local time.

          balance_report_type: The specific type of balance report. One of `intraday`, `previous_day`,
              `real_time`, or `other`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/api/internal_accounts/{internal_account_id}/balance_reports",
            page=SyncPage[BalanceReport],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "as_of_date": as_of_date,
                        "balance_report_type": balance_report_type,
                        "per_page": per_page,
                    },
                    balance_report_list_params.BalanceReportListParams,
                ),
            ),
            model=BalanceReport,
        )


class AsyncBalanceReports(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        internal_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> BalanceReport:
        """
        Get a single balance report for a given internal account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/internal_accounts/{internal_account_id}/balance_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceReport,
        )

    def list(
        self,
        internal_account_id: str,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        as_of_date: Union[str, date] | NotGiven = NOT_GIVEN,
        balance_report_type: Literal["intraday", "other", "previous_day", "real_time"] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BalanceReport, AsyncPage[BalanceReport]]:
        """
        Get all balance reports for a given internal account.

        Args:
          as_of_date: The date of the balance report in local time.

          balance_report_type: The specific type of balance report. One of `intraday`, `previous_day`,
              `real_time`, or `other`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/api/internal_accounts/{internal_account_id}/balance_reports",
            page=AsyncPage[BalanceReport],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "as_of_date": as_of_date,
                        "balance_report_type": balance_report_type,
                        "per_page": per_page,
                    },
                    balance_report_list_params.BalanceReportListParams,
                ),
            ),
            model=BalanceReport,
        )
