from os import system

PLAYERS = 15

ROLES = {
    "TOWN INVESTIGATIVE": ["INVESTIGATOR", "SPY", "LOOKOUT", "SHERIFF"],
    "TOWN KILLING": ["JAILOR", "VETERAN", "VIGILANTE"],
    "TOWN PROTECTIVE": ["BODYGUARD", "DOCTOR"],
    "TOWN SUPPORT": ["ESCORT", "MAYOR", "MEDIUM", "RETRIBUTIONIST", "TRANSPORTER"],
    "MAFIA DECEPTION": ["DISGUISER", "FORGER", "FRAMER", "HYPNOTIST", "JANITOR"],
    "MAFIA KILLING": ["AMBUSHER", "GODFATHER", "MAFIOSO"],
    "MAFIA SUPPORT": ["BLACKMAILER", "CONSIGLIERE", "CONSORT"],
    "NEUTRAL EVIL": ["EXECUTIONER", "JESTER", "WITCH"],
    "NEUTRAL KILLING": ["ARSONIST", "SERIAL KILLER", "WEREWOLF"]
}

ROLE_LIST = []
for a in ROLES:
    for b in ROLES[a]:
        ROLE_LIST.append(b)

ROLE_META = {"JAILOR": 1,
             "TOWN_INVESTIGATIVE": 2,
             "TOWN_PROTECTIVE": 1,
             "RANDOM_TOWN": 5,
             "GODFATHER": 1,
             "MAFIOSO": 1,
             "MAFIA_SUPPORT": 1,
             "RANDOM_MAFIA": 1,
             "NEUTRAL_EVIL": 1,
             "NEUTRAL_KILLING": 1}


def choose_player(prompt, num_max=PLAYERS):
    print(prompt)
    while True:
        try:
            i = int(input())
            if 0 < i <= num_max:
                return i
            elif i < 0 >= PLAYERS:
                print(f"Please enter a number between 1 and {num_max}")
        except ValueError:
            print("Please enter a valid whole number.")


def validated_integer(prompt):
    print(prompt)
    while True:
        try:
            i = int(input())
            return i
        except ValueError:
            print("Please enter a valid whole number.")


def print_list(items, numbered=True):
    for i, item in enumerate(items, start=1):
        if numbered:
            print(f'{i} - {item}')
        else:
            print(item)


def choose_from_list(items):
    print_list(items)
    while True:
        try:
            choice = validated_integer("Pick an item:")
            return items[(choice - 1)]
        except IndexError:
            print("Please choose a valid item.")


def print_player_list():
    no_claim_length = 9
    claims_length = 7
    confirmed_length = 10
    dead_length = 5

    no_claim_list = []
    for i in no_claims:
        temp_string = f'{i} - {players[i]["Role"]}'
        if len(temp_string) > no_claim_length:
            no_claim_length = len(players[i]["Role"])
        no_claim_list.append(temp_string)
    no_claim_list.insert(0, "No claims:")
    no_claim_length += 10

    claims_list = []
    for i in claims:
        temp_string = f'{i} - {players[i]["Role"]}'
        if len(temp_string) > claims_length:
            claims_length = len(players[i]["Role"])
        claims_list.append(temp_string)
    claims_list.insert(0, "Claims:")
    claims_length += 10

    confirmed_list = []
    for i in confirmed:
        temp_string = f'{i} - {players[i]["Role"]}'
        if len(temp_string) > confirmed_length:
            confirmed_length = len(players[i]["Role"])
        confirmed_list.append(temp_string)
    confirmed_list.insert(0, "Confirmed:")
    confirmed_length += 10

    dead_list = []
    for i in dead:
        temp_string = f'{i} - {players[i]["Role"]}'
        if len(temp_string) > dead_length:
            dead_length = len(players[i]["Role"])
        dead_list.append(temp_string)
    dead_list.insert(0, "Dead:")
    dead_length += 10

    cleaned_no_claims = []
    for i in no_claim_list:
        cleaned_no_claims.append(i.ljust(no_claim_length))

    cleaned_claims = []
    for i in claims_list:
        cleaned_claims.append(i.ljust(claims_length))

    cleaned_confirmed = []
    for i in confirmed_list:
        cleaned_confirmed.append(i.ljust(confirmed_length))

    cleaned_dead = []
    for i in dead_list:
        cleaned_dead.append(i.ljust(dead_length))

    count = 0
    rows = []
    col_1_fail = 0
    col_2_fail = 0
    col_3_fail = 0
    col_4_fail = 0

    while True:
        temp_row = []
        try:
            temp_row.append(cleaned_no_claims[count])
        except IndexError:
            temp_row.append(" " * no_claim_length)
            col_1_fail = 1
        try:
            temp_row.append(cleaned_claims[count])
        except IndexError:
            col_2_fail = 1
            temp_row.append(" " * claims_length)
        try:
            temp_row.append(cleaned_confirmed[count])
        except IndexError:
            col_3_fail = 1
            temp_row.append(" " * confirmed_length)
        try:
            temp_row.append(cleaned_dead[count])
        except IndexError:
            temp_row.append(" " * dead_length)
            col_4_fail = 1
        if col_1_fail + col_2_fail + col_3_fail + col_4_fail < 4:
            rows.append(temp_row)
        else:
            break
        count += 1
    for i in rows:
        print(" ".join(i))


def select_role(prompt):
    print(prompt)

    count = 1
    column_1 = []
    column_2 = []
    column_3 = []
    col_1_max_length = 0
    col_2_max_length = 0
    col_3_max_length = 0

    for group in ROLES:
        if group.startswith("TOWN"):
            column_1.append(group)
            for role in ROLES[group]:
                column_1.append(f"{count} - {role}")
                count += 1
                if len(role) > col_1_max_length:
                    col_1_max_length = len(role) + 10

        elif group.startswith("MAFIA"):
            column_2.append(group)
            for role in ROLES[group]:
                column_2.append(f"{count} - {role}")
                count += 1
                if len(role) > col_2_max_length:
                    col_2_max_length = len(role) + 10

        elif group.startswith("NEUTRAL"):
            column_3.append(group)
            for role in ROLES[group]:
                column_3.append(f"{count} - {role}")
                count += 1
                if len(role) > col_3_max_length:
                    col_3_max_length = len(role) + 10

    cleaned_column_1 = []
    cleaned_column_2 = []
    cleaned_column_3 = []

    for i in column_1:
        cleaned_column_1.append(i.ljust(col_1_max_length))
    for i in column_2:
        cleaned_column_2.append(i.ljust(col_2_max_length))
    for i in column_3:
        cleaned_column_3.append(i.ljust(col_3_max_length))

    rows = []
    count = 0
    fail = 0
    col_1_fail = 0
    col_2_fail = 0
    col_3_fail = 0

    while True:
        temp_list = []
        try:
            temp_list.append(cleaned_column_1[count])
        except IndexError:
            col_1_fail = 1
        try:
            temp_list.append(cleaned_column_2[count])
        except IndexError:
            col_2_fail = 1
        try:
            temp_list.append(cleaned_column_3[count])
        except IndexError:
            col_3_fail = 1
        count += 1
        if col_1_fail + col_2_fail + col_3_fail < 3:
            rows.append(temp_list)
        else:
            break

    for i in rows:
        print((" ".join(i).title()))

    while True:
        try:
            choice = int(input("Choose a role: "))
            choice -= 1
            return ROLE_LIST[choice]
        except ValueError:
            print("Please enter a valid number.")
            continue
        except IndexError:
            print("Please choose a valid item.")


players = {1: {"Role": "Unknown"},
           2: {"Role": "Unknown"},
           3: {"Role": "Unknown"},
           4: {"Role": "Unknown"},
           5: {"Role": "Unknown"},
           6: {"Role": "Unknown"},
           7: {"Role": "Unknown"},
           8: {"Role": "Unknown"},
           9: {"Role": "Unknown"},
           10: {"Role": "Unknown"},
           11: {"Role": "Unknown"},
           12: {"Role": "Unknown"},
           13: {"Role": "Unknown"},
           14: {"Role": "Unknown"},
           15: {"Role": "Unknown"}}

no_claims = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
claims = []
confirmed = []
dead = []

player_number = validated_integer("Enter your number: ")
player_role = select_role("Choose your role: ")
no_claims.remove(player_number)
confirmed.append(player_number)
players[player_number]["Role"] = player_role

system('cls')
while True:
    system('cls')
    print_player_list()

    player = choose_player("Enter a player number")
    system('cls')
    print("Choose an action:")
    main_choice = choose_from_list(["Claim", "Confirm", "Report Dead", "Print claims"])
    system('cls')
    if main_choice == "Claim":
        players[player]["Role"] = select_role("Choose a role")
        if player not in claims:
            claims.append(player)
        if player in no_claims:
            no_claims.remove(player)
    elif main_choice == "Confirm":
        role = select_role("Choose a role")
        players[player]["Role"] = role
        if player not in confirmed:
            confirmed.append(player)
        if player in claims:
            claims.remove(player)
        if player in no_claims:
            no_claims.remove(player)
    elif main_choice == "Report Dead":
        role = select_role("Choose a role")
        players[player]["Role"] = role
        if player not in dead:
            dead.append(player)
        if player in claims:
            claims.remove(player)
        if player in no_claims:
            no_claims.remove(player)
        if player in confirmed:
            confirmed.remove(player)
    elif main_choice == "Print claims":
        for i in players:
            print(f'{i} - {players[i]["Role"]}')
