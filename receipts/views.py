from django.shortcuts import render

from receipts.models import Account, ExpenseCategory, Receipt

# Create your views here.


def show_receipts(request):
    model = Receipt.objects.all()
    return render(
        request,
        template_name="receipts/list.html",
        context={"receipts": model},
    )


def show_accounts(request):
    model = Account.objects.all()
    return render(
        request,
        template_name="receipts/list.html",
        context={"receipts": model},
    )


def show_expensecategory(request):
    model = ExpenseCategory.objects.all()
    return render(
        request,
        template_name="receipts/list.html",
        context={"receipts": model},
    )