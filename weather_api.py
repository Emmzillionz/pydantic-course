from pydantic import BaseModel, ConfigDict

class WeatherResponse(BaseModel):
    model_config = ConfigDict(strict=True)
    
    temperature: float
    city: str
    humidity: int
    description: str
    
api_data = {
    "city": "Amsterdam",
    "temperature": 18.5,
    "humidity": 75,
    "description": "Partly Cloudy",
}

weather = WeatherResponse.model_validate(api_data)
print(f"The Weather in {weather.city}: {weather.temperature}")
print(f"Humidity: {weather.humidity}%")
print(f"Conditions: {weather.description}")