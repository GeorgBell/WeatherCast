def form_cloth_pic_path(gender, city_weather):
    """
    The function implements logic to recommend clothes by filling the path:
    - start with general folder
    - define gender
    - define temperature conditions
    - define precipation conditions
    - return file path
    """
    # Define gender and add to the path
    if gender == "F":
        cloth_pic = 'clothes/female'
    elif gender == "M":
        cloth_pic = 'clothes/male'
    else:
        cloth_pic = ""

    # Define temperature conditions and add to the path
    if city_weather['temperature'] <0:
        cloth_pic += "/cold"
    elif city_weather['temperature'] > 20:
        cloth_pic += "/hot"
    else:
        cloth_pic += "/mild"

    # Define precipation conditions and add to the path
    if city_weather['main'] == "Clear":
        cloth_pic += "_clear"
    elif city_weather['main'] == "Clouds" or city_weather['main'] == "Mist":
        cloth_pic += "_cloud"
    else:
        cloth_pic += "_precip"

    # Add the file format and return the path
    cloth_pic += ".png"
    return cloth_pic
