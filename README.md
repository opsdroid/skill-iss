# opsdroid skill ISS

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to locate and show a map of the ISS.

Uses data from [open notify][open-notify] and [Google Maps][google-maps-api] for mapping.

## Requirements

A Google Maps [API key][google-maps-api].

## Configuration

```yaml
skills:
  - name: iss
    # Required
    api-key: "mygooglemapsapikey"
    # Optional
    zoom: "5"
    map-size: "1024x768"
    map-type: "hybrid" # hybrid, satellite or roadmap
```

## Usage

#### `Where is the ISS?`

Shows the user a map of the ISS location

> user: Where is the ISS?
>
> opsdroid:
> ![ISS](https://cloud.githubusercontent.com/assets/1610850/25489364/7e09dffa-2b61-11e7-9539-788fa67544b2.png)

## License

GNU General Public License Version 3 (GPLv3)

[google-maps-api]: https://developers.google.com/maps/documentation/static-maps/intro
[open-notify]: http://api.open-notify.org/
