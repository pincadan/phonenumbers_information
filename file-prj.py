import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Prompt user for phone number
phone_number = input("Enter a phone number (e.g. +1234567890): ")

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number)

# Check if the phone number is valid
is_valid = phonenumbers.is_valid_number(parsed_number)

# Get the country code
country_code = phonenumbers.region_code_for_number(parsed_number)

# Get the geolocation
geolocation = geocoder.description_for_number(parsed_number, "en")

# Get the carrier
carrier_name = carrier.name_for_number(parsed_number, "en")

# Get the timezone
timezone_name = timezone.time_zones_for_number(parsed_number)

# Print the gathered information
print("Phone Number:", phone_number)
print("Is Valid:", is_valid)
print("Country Code:", country_code)
print("Geolocation:", geolocation)
print("Carrier:", carrier_name)
print("Timezone:", timezone_name)