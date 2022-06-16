from django.shortcuts import render
from receipts.models import Account, ExpenseCategory, Receipt
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
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
