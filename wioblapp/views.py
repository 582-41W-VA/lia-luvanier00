from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Role, UserAccount, Team, Player, RegistrationType, Registration, Park, Game, Comment, Announcement, Flag
from .forms import SignUpForm, RegistrationForm, ModifyAccountForm, LoginForm, FilterTeamsForm, CreateCommentForm, TeamScheduleForm

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
            role = signup_form.cleaned_data.get("role")
            bio = signup_form.cleaned_data.get("bio")

            if UserAccount.objects.filter(first_name=firstname).exists():
                messages.error(request, f"Firstname {firstname} is already exist!")
                return render (request, "sign-up.html", {"signup_form": signup_form,})

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
                role=Role.objects.get(name=role),
                bio=bio
            )

            if role.name in ["Admin", "Coach"]:
                member.is_staff = True
                member.is_superuser = True
                member.save()

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
            member.role = account_form.cleaned_data["role"]
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
    filter_teams_form = FilterTeamsForm()
    groups = RegistrationType.objects.all()
    teams = Team.objects.all()
    players = Player.objects.all()

    filter_teams_form = FilterTeamsForm(request.GET)

    if filter_teams_form.is_valid():
        group = filter_teams_form.cleaned_data.get('group')
        coach = filter_teams_form.cleaned_data.get('coach')
        keyword = filter_teams_form.cleaned_data.get('search')

        if group: 
            teams = teams.filter(group=group)

        if keyword:
            teams = teams.filter(name__icontains=keyword)
            players = players.filter(name__icontains=keyword)

        if coach:
            teams = teams.filter(coaches=coach)
        
        players = players.filter(team_name__in=teams)

    context = {
        "filter_teams_form": filter_teams_form,
        "groups": groups,
        "teams": teams,
        "players": players,
    }

    return render(request, "teams.html", context)
# --------------------------------------------------------------

def team_schedule(request, team_name):
    schedule_form = TeamScheduleForm()
    team = team_name
    context = {
        "schedule_form": schedule_form,
        "team": team,
    }
    return render(request, "team_schedule.html", context)

# --------------------------------------------------------------
def team_schedule(request, team_name):
    schedule_form = TeamScheduleForm()
    team = team_name
    context = {
        "schedule_form": schedule_form,
        "comment_form": comment_form,
        "team": team,
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

            comment = Comment.objects.create(
                game=game,
                user_account=user_account,
                content=content
            )

            if comment:
                messages.success(request, "Comment is posted successfully")
                return redirect("team_schedule", team)
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
            messages.info(request, "Login before posting a comment")
            return redirect("team_schedule", team)

        comment.likes += 1
        comment.save()
        return redirect("team_schedule", team)
# --------------------------------------------------------------

# --------------------------------------------------------------
def flag_comment(request, team_name):
    team = team_name

    if request.method == "POST":
        comment_id = request.POST.get('flag')
        comment = Comment.objects.get(id=comment_id)
        flagged_content = comment.content

        if not comment:
            messages.error(request, "Something went wrong")

        if not request.user.is_authenticated:
            messages.info(request, "Login before posting a comment")
            return redirect("team_schedule", team)

        user_account = request.user
        flag = Flag.objects.create(
            user_account=user_account,
            flagged_content=flagged_content,
        )

        if flag:
            messages.success(request, "Comment flagged successfully")
            return redirect("team_schedule", team)
# --------------------------------------------------------------

# --------------------------------------------------------------
def about(request):
    return render(request, "about.html")
# --------------------------------------------------------------
