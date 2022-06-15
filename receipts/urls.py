from django.urls import path
from receipts.views import (
    show_accounts,
    show_expensecategory,
    show_receipts
)

urlpatterns = [
    path("", show_receipts, name="home"),
    path("", show_accounts, name="arbitrary"),
    path("", show_expensecategory, name="arbitrary"),
]