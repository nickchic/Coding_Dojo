from django.shortcuts import render, redirect
from django.db.models import Count
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
		"atlantic_soccer_conference_teams": Team.objects.filter(league_id=5),
		"boston_penguin_players_curr": Player.objects.filter(curr_team_id=28),
		"ICBC_players_curr": Player.objects.filter(curr_team_id__league_id=2),
		"ACAF_players_lopez_curr": Player.objects.filter(curr_team_id__league_id=7, last_name='Lopez'),
		"all_football_players": Player.objects.filter(curr_team_id__league_id__sport='Football'),
		"teams_with_sophia": Team.objects.filter(curr_players__first_name="Sophia"),
		"leagues_with_sophia": League.objects.filter(teams__curr_players__first_name="Sophia"),
		"flores_not_roughriders": Player.objects.filter(last_name="Flores").exclude(curr_team_id__id=10),
		"samuel_evans_teams": Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
		"all_tigercats_players": Player.objects.filter(all_teams__id=37),
		"former_vikings_players": Player.objects.filter(all_teams__id=40).exclude(curr_team__id=40),
		"jacob_grey_teams_before_colts": Team.objects.filter(all_players__id=151).exclude(curr_players__id=151),
		"all_joshuas_AFABP": Player.objects.filter(first_name='Joshua', all_teams__league_id=3),
		"teams_with_tweleve": Team.objects.annotate(all_players_count=Count("all_players")).filter(all_players_count__gt=12).order_by("-all_players_count"),
		"all_players_with_amount_of_teams": Player.objects.annotate(all_teams_count=Count("all_teams")).order_by("-all_teams_count")
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
