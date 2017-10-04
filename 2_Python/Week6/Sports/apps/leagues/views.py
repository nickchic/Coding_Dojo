from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_leagues": League.objects.filter(sport='Baseball'),
		"women_leagues": League.objects.filter(name__contains="Women"),
		"hockey_leauges": League.objects.filter(sport__contains="Hockey"),
		"non_football_leagues": League.objects.exclude(sport="Football"),
		"conferences": League.objects.filter(name__contains="Conference"),
		"atlantic_region_teams": Team.objects.filter(league_id=3)|Team.objects.filter(league_id=4)|Team.objects.filter(league_id=5)|Team.objects.filter(league_id=8),
		"dallas_teams": Team.objects.filter(location='Dallas'),
		"raptor_teams": Team.objects.filter(team_name__contains="Raptor"),
		"city_location": Team.objects.filter(location__contains="City"),
		"t_teams": Team.objects.filter(team_name__startswith="T"),
		"location_alphabet": Team.objects.all().order_by('location'),
		"last_name_cooper": Player.objects.filter(last_name="Cooper"),
		"first_name_joshua": Player.objects.filter(first_name="Joshua"),
		"cooper_no_joshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"alexander_or_wyatt": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
