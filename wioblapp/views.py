from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Role, UserAccount, Team, Player, RegistrationType, Registration, Park, Game, Comment, Announcement, Flag, LikedComment, FavoriteTeam
from .forms import SignUpForm, RegistrationForm, ModifyAccountForm, LoginForm, FilterTeamsForm, CreateCommentForm, TeamScheduleForm

from django.db.models import F

# --------------------------------------------------------------
def index(request):
    announcements = Announcement.objects.order_by("-date")[:4]

    context = {
        "announcements": announcements,
    }
    return render(request, "index.html", context)
# --------------------------------------------------------------

# --------------------------------------------------------------
def sign_up(request):
    signup_form = SignUpForm()

    if request.method == "POST":
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            firstname = signup_form.cleaned_data.get("firstname").strip()
            lastname = signup_form.cleaned_data.get("lastname").strip()
            username = f"{firstname}{lastname}"
            email = signup_form.cleaned_data.get("email")
            password = signup_form.cleaned_data.get("password1")

            if UserAccount.objects.filter(username=username).exists():
                messages.error(request, f"Username {username} is already exist!")
                return render (request, "sign-up.html", {"signup_form": signup_form,})
            
            if UserAccount.objects.filter(email=email).exists():
                messages.error(request, f"Email {email} is already exist")
                return render (request, "sign-up.html", {"signup_form": signup_form,})

            member = UserAccount.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=username,
                email=email,
                password=password,
                role=Role.objects.get(name="Parent")
            )

            messages.success(request, "You signed-up successfully")
            auth_member = authenticate(request, username=username, password=password)
            if auth_member:
                login(request, auth_member)
                return redirect("index")
            else:
                 messages.error(request, "error logging in")

    context = {
        "signup_form": signup_form,
    }
    return render(request, "sign-up.html", context)
# --------------------------------------------------------------

# --------------------------------------------------------------
def member_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    login_form = LoginForm()

    if request.method == "POST":
        login_form = LoginForm(data=request.POST)

        if login_form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]

            try:
                user = UserAccount.objects.get(email=email)
                username = user.username
                member = authenticate(request, username=username, password=password)

                if member is not None:
                    login(request, member)
                    return redirect("index")
                else:
                    messages.error(request, "Email OR Password is incorrect!")
            except UserAccount.DoesNotExist:
                    messages.error(request, "Email OR Password is incorrect!")

    context = {
        "login_form": login_form,
    }
    return render(request, "login.html", context)
# --------------------------------------------------------------

# --------------------------------------------------------------
@login_required(login_url="login")
def member_account(request, account_id):
    member = get_object_or_404(UserAccount, pk=account_id)
    players = Player.objects.filter(related_account=account_id)
    favorite_teams = FavoriteTeam.objects.filter(user_account=account_id)
    registrations = Registration.objects.filter(player__in=players)
    password = member.password

    try:
        player = Player.objects.filter(related_account=account_id).first()
    except Player.DoesNotExist:
        pass

    try:
        registration = Registration.objects.get(player=player)
    except Registration.DoesNotExist:
        pass

    if request.method == "GET":
        account_form = ModifyAccountForm(instance=member)
    elif request.method == "POST":
        account_form = ModifyAccountForm(request.POST, instance=member)
        if account_form.is_valid():
            member.username = account_form.cleaned_data["username"]
            member.first_name = account_form.cleaned_data["first_name"]
            member.last_name = account_form.cleaned_data["last_name"]
            member.email = account_form.cleaned_data["email"]
            new_password = account_form.cleaned_data.get("password")
            member.set_password(new_password)
            member.phone = account_form.cleaned_data["phone"]
            member.save()
            messages.success(request, "Your account updated successfully")

            auth_member = authenticate(request, username=member.username, password=new_password)
            if auth_member is not None:
                login(request, auth_member)
                return redirect("member_account", account_id=request.user.id)
            else:
                messages.error(request, "error logging in")

    context = {
        "account_form": account_form,
        "member": member,
        "players": players,
        "favorite_teams": favorite_teams,
        "registrations": registrations,
    }
    return render(request, "member_account.html", context)
# --------------------------------------------------------------

# --------------------------------------------------------------
@login_required(login_url="login")
def register_player(request):
    register_form = RegistrationForm()

    if request.method == "POST":
        register_form = RegistrationForm(request.POST)

        if register_form.is_valid():
            firstname = register_form.cleaned_data["firstname"]
            lastname = register_form.cleaned_data["lastname"]
            playername = f"{firstname} {lastname}"
            dob = register_form.cleaned_data["dob"]
            gender = register_form.cleaned_data["gender"]
            group = register_form.cleaned_data["group"]
            street_line1 = register_form.cleaned_data["street_line1"]
            app_line2 = register_form.cleaned_data["app_line2"]
            city = register_form.cleaned_data["city"]
            province = register_form.cleaned_data["province"]
            postal_code = register_form.cleaned_data["postal_code"]
            country = register_form.cleaned_data["country"]
            email = register_form.cleaned_data["email"]
            phone = register_form.cleaned_data["phone"]
            uniform_size = register_form.cleaned_data["uniform_size"]
            consent = register_form.cleaned_data["consent"]
            volunteer = register_form.cleaned_data["volunteer"]
            message = register_form.cleaned_data["message"]

            member = UserAccount.objects.get(email=request.user.email)

            player, created = Player.objects.get_or_create(
                related_account=member,
                name=playername,
                dob=dob,
                gender=gender
            )

            registration = Registration.objects.create(
                player=player,
                reg_type=group,
                address=f"{street_line1}, {app_line2}, {city}, {province}, {postal_code}, {country}",
                email=email,
                phone=phone,
                uniform_size=uniform_size,
                consent=consent,
                volunteer=volunteer,
                message=message
            )

            messages.success(request, "Registration submitted successfully")
            return redirect('index') 

    context = {
        "register_form": register_form,
    }
    return render(request, "registration.html", context)
# --------------------------------------------------------------

# --------------------------------------------------------------
@login_required(login_url="login")
def member_logout(request):
    logout(request)
    return redirect("login")
# --------------------------------------------------------------

# --------------------------------------------------------------
def teams(request):
    filter_teams_form = FilterTeamsForm(request.GET)
    groups = RegistrationType.objects.all()
    teams = Team.objects.all()
    players = Player.objects.all()

    if filter_teams_form.is_valid():
        group = filter_teams_form.cleaned_data.get('group')
        coach = filter_teams_form.cleaned_data.get('coach')
        keyword = filter_teams_form.cleaned_data.get('search')

        if group: 
            teams = teams.filter(group=group)
            players = players.filter(team_name__in=teams)

        if coach:
            teams = teams.filter(coaches=coach)
            players = players.filter(team_name__in=teams)

        if keyword:
            keyword_teams = teams.filter(name__icontains=keyword)
            if keyword_teams:
                teams = keyword_teams
            
            keyword_players = players.filter(name__icontains=keyword)
            if keyword_players:
                players = keyword_players
                teams = Team.objects.filter(players__in=keyword_players)

            if not keyword_players and not keyword_teams:
                players = []
                teams = []

    context = {
        "filter_teams_form": filter_teams_form,
        "groups": groups,
        "teams": teams,
        "players": players,
    }

    return render(request, "teams.html", context)
# --------------------------------------------------------------

# --------------------------------------------------------------
def like_team(request, team_name):
    team = Team.objects.get(name=team_name)

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.info(request, "Login first, please!")
            return redirect("teams", team_name)

        is_liked = FavoriteTeam.objects.filter(user_account=request.user, team=team_name)

        if is_liked:
            is_liked.delete()
            messages.info(request, f"Team {team_name}'s Like removed")
        else:
            FavoriteTeam.objects.create(
                user_account=request.user,
                team=team,
            )
            messages.success(request, f"Liked team {team_name}")

    return redirect("teams")
# --------------------------------------------------------------

# --------------------------------------------------------------
def dislike_team(request, team_name):
    account_id = request.user.id
    team = Team.objects.get(name=team_name)

    is_liked = FavoriteTeam.objects.filter(user_account=request.user, team=team_name)

    if is_liked:
        is_liked.delete()
        messages.info(request, f"Team {team_name}'s Like removed")

    return redirect("member_account", account_id)
# --------------------------------------------------------------

# --------------------------------------------------------------
def team_schedule(request, team_name):
    schedule_form = TeamScheduleForm(request.GET)
    comment_form = CreateCommentForm()
    team = team_name
    games = ( Game.objects.filter(team_1=team) | Game.objects.filter(team_2=team) ).distinct()
    comments = Comment.objects.filter(game__in=games)
    game_comments = []
    flags = Flag.objects.all()  
    
    if schedule_form.is_valid():
        month = schedule_form.cleaned_data.get('month')
        date = schedule_form.cleaned_data.get('date')
        result = schedule_form.cleaned_data.get('result')

        if month:
            if month == "All":
                games = ( Game.objects.filter(team_1=team) | Game.objects.filter(team_2=team) ).distinct()
            else:
                games = games.filter(date_time__month=int(month))

        if date:
            if date == "Ascending":
                games = games.order_by("-date_time")
            elif date == "Descending":
                games = games.order_by("date_time")

        if result:
            if result == "Win":
                games = games.filter(winner=team)
            elif result == "Lose":
                games = games.exclude(winner=team).exclude(team1_score=F('team2_score')).exclude(team1_score__isnull=True).exclude(team2_score__isnull=True)
            elif result == "Tie":
                games = games.filter(team1_score=F('team2_score'), team1_score__isnull=False, team2_score__isnull=False)

    for game in games:
        game_comments.append({
            "game": game,
            "comments": comments.filter(game=game).order_by("-date"),
        }) 

    context = {
        "schedule_form": schedule_form,
        "comment_form": comment_form,
        "team": team,
        "games": games,
        "comments": comments,
        "game_comments": game_comments,
        "flags": flags,
    }
    return render(request, "team_schedule.html", context)
# --------------------------------------------------------------

# --------------------------------------------------------------
def create_comment(request, team_name):
    team = team_name

    if request.method == "POST":
        comment_form = CreateCommentForm(request.POST)
        game_id = request.POST.get("post")
        comments = Comment.objects.filter(game=game_id)
        
        if comment_form.is_valid():
            game = Game.objects.get(id=game_id)
            user_account = request.user
            content = comment_form.cleaned_data.get('content')

            if not request.user.is_authenticated:
                messages.info(request, "Login before posting a comment")
                return redirect("team_schedule", team)

            comment = Comment.objects.get_or_create(
                game=game,
                user_account=user_account,
                content=content
            )

            if comment:
                messages.success(request, "Comment is posted successfully")
                return redirect("team_schedule", team)
            
        messages.error(request, "Comment Can't be created. Please try again.")
    return redirect("team_schedule", team_name)
# --------------------------------------------------------------

# --------------------------------------------------------------
def like_comment(request, team_name):
    team = team_name

    if request.method == "POST":
        comment_id = request.POST.get('like')
        comment = Comment.objects.get(id=comment_id)

        if not comment:
            messages.error(request, "Something went wrong")

        if not request.user.is_authenticated:
            messages.info(request, "Login first, please!")
            return redirect("team_schedule", team)

        is_liked = LikedComment.objects.filter(comment=comment_id, user_account=request.user)

        if is_liked:
            is_liked.delete()
            comment.likes -= 1
            comment.save()
        else:
            LikedComment.objects.create(
                comment=comment,
                user_account=request.user,
            )
            comment.likes += 1
            comment.save()

    return redirect("team_schedule", team_name)
# --------------------------------------------------------------

# --------------------------------------------------------------
def flag_comment(request, team_name):
    team = team_name

    if request.method == "POST":
        comment_id = request.POST.get('flag')
        comment = Comment.objects.get(id=comment_id)

        if not comment:
            messages.error(request, "Something went wrong")

        if not request.user.is_authenticated:
            messages.info(request, "Login before flagging a comment")
            return redirect("team_schedule", team)


        is_flagged = Flag.objects.filter(user_account=request.user, comment=comment)

        if not is_flagged:
            flag = Flag.objects.create(
                user_account=request.user,
                comment=comment,
            )

            if flag:
                messages.success(request, "Comment flagged successfully")
                return redirect("team_schedule", team)
        else:
            messages.info(request, "Comment is already flagged")

    return redirect("team_schedule", team_name)
# --------------------------------------------------------------

# --------------------------------------------------------------
def edit_comment(request, team_name, comment_id):
    team = team_name

    if not comment_id:
        messages.error(request, "Something went wrong")
        return redirect("team_schedule", team)

    comment = get_object_or_404(Comment, id=comment_id)
    comment_form = CreateCommentForm(instance=comment)
    
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.info(request, "Login before editing a comment")
            return redirect("team_schedule", team)

        comment_form = CreateCommentForm(request.POST, instance=comment)

        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, "Comment edited successfully")
            return redirect("team_schedule", team)

        messages.error(request, "Can't be edited. Please try again.")

    return redirect("team_schedule", team_name)
# --------------------------------------------------------------

# --------------------------------------------------------------
def delete_comment(request, team_name):
    team = team_name

    if request.method == "POST":
        comment_id = request.POST.get('delete')
        comment = get_object_or_404(Comment, id=comment_id)
        
        if not comment:
            messages.error(request, "Comment can't be deleted")

        if not request.user.is_authenticated:
            messages.info(request, "Login before deleting a comment")
            return redirect("team_schedule", team)

        deleted = comment.delete()
        if deleted:
            messages.success(request, "Comment deleted")
            return redirect("team_schedule", team)    
        
        messages.error(request, "Can't be deleted. Please try again.")
    return redirect("team_schedule", team_name)    
# --------------------------------------------------------------

# --------------------------------------------------------------
def about(request):
    return render(request, "about.html")
# --------------------------------------------------------------
