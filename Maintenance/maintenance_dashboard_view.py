from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def maintenance_dashboard_view(request):
    # This view simply renders a template that includes links to the other pages
    return render(request, 'pages/maintenance_dashboard.html')