import openai, os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"
openai.api_key = OPENAI_API_KEY

NOT_A_CITY = "NOT A CITY"

def correct_city_name(city):
    corrected_city = ""
    try:
        prompt = f"Correct city name for {city}, it will be used on OpenWeather API,\
         if it is not a city, just reply {NOT_A_CITY},\
         remember to just reply the corrected city name or {NOT_A_CITY}, no additional text"
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        if response.choices:
            corrected_city = response.choices[0].text.strip()
        else:
            return city
    except:
        if corrected_city and NOT_A_CITY in corrected_city:
            raise Exception("El nombre de ciudad brindado no es un nombre válido.")
        elif corrected_city:
            return corrected_city
        else:
            return city
