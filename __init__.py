import aiohttp

from opsdroid.matchers import match_regex

ISS_API           = "http://api.open-notify.org/iss-now.json"
GOOGLE_MAPS_API   = "https://maps.googleapis.com/maps/api/staticmap"
DEFAULT_MAP_SIZE  = "1024x768"
DEFAULT_ZOOM      = 5
DEFAULT_MAP_TYPE  = "roadmap"
GOOGLE_MAPS_QUERY = "{api}?center={lat},{lon}&zoom={zoom}&size={size}&maptype={type}&markers=color:blue%7Clabel:ISS%7C{lat},{lon}&key={api_key}"


async def get_iss_location():
    async with aiohttp.ClientSession() as session:
        async with session.get(ISS_API) as resp:
            if resp.status == 200:
                response = await resp.json()
                return (response["iss_position"]["latitude"],
                        response["iss_position"]["longitude"])


@match_regex(r'[Ww]here( i|\'|)s the (iss|ISS|Iss|space station|international space station)')
async def where_is_the_iss(opsdroid, config, message):
    api_key  = config.get("api-key")
    zoom     = str(config.get("zoom", DEFAULT_ZOOM))
    map_size = config.get("map-size", DEFAULT_MAP_SIZE)
    map_type = config.get("map-type", DEFAULT_MAP_TYPE)
    lat, lon = await get_iss_location()

    if api_key is None:
        await message.respond(
            "Whoops you need to configure this skill with a Google Maps API key.")
        return

    await message.respond(GOOGLE_MAPS_QUERY.format(api=GOOGLE_MAPS_API,
                                                   lat=lat,
                                                   lon=lon,
                                                   zoom=zoom,
                                                   size=map_size,
                                                   type=map_type,
                                                   api_key=api_key
                                                   ))
