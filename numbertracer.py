import phonenumbers
from phonenumbers import geocoder, carrier, PhoneNumberType
print(r"""
  _____                _____        ______  _____   ______         _____    ____   ____ 
 |\    \   _____   ___|\    \   ___|\     \|\    \ |\     \    ___|\    \  |    | |    |
 | |    | /    /| |    |\    \ |     \     \\\    \| \     \  /    /\    \ |    | |    |
 \/     / |    || |    | |    ||     ,_____/|\|    \  \     ||    |  |    ||    |_|    |
 /     /_  \   \/ |    |/____/ |     \--'\_|/ |     \  |    ||    |  |____||    .-.    |
|     // \  \   \ |    |\    \ |     /___/|   |      \ |    ||    |   ____ |    | |    |
|    |/   \ |    ||    | |    ||     \____|\  |    |\ \|    ||    |  |    ||    | |    |
|\ ___/\   \|   /||____| |____||____ '     /| |____||\_____/||\ ___\/    /||____| |____|
| |   | \______/ ||    | |    ||    /_____/ | |    |/ \|   ||| |   /____/ ||    | |    |
 \|___|/\ |    | ||____| |____||____|     | / |____|   |___|/ \|___|    | /|____| |____|
    \(   \|____|/   \(     )/    \( |_____|/    \(       )/     \( |____|/   \(     )/  
     '      )/       '     '      '    )/        '       '       '   )/       '     '
""")
print("\n****************************************************************")
print("\n* Copyright of wrench project, 2025                           *")
print("\n****************************************************************")
number_input = input("Enter the phone number (with country code, e.g., +91xxxxxxxxxx): ")
parsed_number = phonenumbers.parse(number_input, None)

if phonenumbers.is_valid_number(parsed_number):
    print("\nThis is a valid phone number.\n")
else:
    print("\nInvalid phone number.\n")
    exit()

region = geocoder.description_for_number(parsed_number, "en")
sim_carrier = carrier.name_for_number(parsed_number, "en")
num_type = phonenumbers.number_type(parsed_number)

type_mapping = {
    PhoneNumberType.MOBILE: "Mobile",
    PhoneNumberType.FIXED_LINE: "Fixed Line",
    PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
    PhoneNumberType.TOLL_FREE: "Toll Free",
    PhoneNumberType.PREMIUM_RATE: "Premium Rate",
    PhoneNumberType.SHARED_COST: "Shared Cost",
    PhoneNumberType.VOIP: "VOIP",
    PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
    PhoneNumberType.PAGER: "Pager",
    PhoneNumberType.UAN: "UAN",
    PhoneNumberType.VOICEMAIL: "Voicemail",
}
mobile_prefix_map = {
    '98': 'Delhi',
    '97': 'Maharashtra',
    '96': 'Karnataka',
    '95': 'Tamil Nadu',
    '94': 'Kerala',
    '93': 'Punjab',
    '90': 'Uttar Pradesh',
}

national_number = str(parsed_number.national_number)
if len(national_number) >= 2:
    prefix = national_number[:2]
    region_hint = mobile_prefix_map.get(prefix, "Unknown")
else:
    region_hint = "Unknown"

print("\n--------------------------------------")
print("Approx Region by Prefix: " + region_hint)
print("Region / State: " + (region if region else "Unknown"))
print("Carrier: " + (sim_carrier if sim_carrier else "Unknown"))
print("Number Type: " + type_mapping.get(num_type, "Unknown"))
print("--------------------------------------\n")
