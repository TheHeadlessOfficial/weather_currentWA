# Lock file to tell conky that the script is running
lock_file = "/tmp/script_wacurrent.lock"
try:
    # Check for file lock
    open(lock_file, 'w').close()
    import os
    from PIL import Image
    import time
    import requests
    import urllib.request
    # import module GEOPY
    from geopy.geocoders import Photon
    # initialize Nominatim API
    geolocator = Photon(user_agent="measurements")
    ################################ get your HOME automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set your latitude, longitude, city and APPID
    mylat = 
    mylon = 
    mycity = ''
    myAPPID = ''
    ################################ pattern url CURRENT
    url = 'https://api.weatherapi.com/v1/current.json?key=' + myAPPID + '&q=' + mycity + '&aqi=yes'
    res = requests.get(url).json()
    data = res
    ################################ set variables (TYPE YOUR myd)
    myd = 72 # north degree
    tdeg = 0
    winddeg = 0
    ################################ insert angle of my North in 'myd' (if no wind then winddeg doesn't load)
    vtext = 'n/a'
    ################################ set default conky folder (change it if needed)
    home = '/home/'
    conky = '/.conky/'
    defconkyfol = conky + 'weather/Weatherapi/'
    ################################ set the paths for the API files
    ptemp = defconkyfol + 'today/'
    #                   set the path for the ERROR
    perr = home + homename + ptemp + '-error.txt'
    ################################ get data for ERROR section
    responseHTTP = requests.get(url)
    # get status code
    status_code = responseHTTP.status_code
    ################################ write raw data for ERROR section
    fo = open(perr, 'w')
    fo.write('error: {}\n'.format(status_code))
    fo.close()
    ############################################### GEOPY NEW SYNTAX
    urlGeopy = 'https://photon.komoot.io/reverse?lon=' + str(mylon) + '&lat='  + str(mylat)
    resGeopy = requests.get(urlGeopy).json()
    dataGeopy = resGeopy
    Glocation = urllib.request.urlopen(urlGeopy)
    Ghousenumber = "housenumber is old syntax"
    Groad = "street is old syntax"#dataGeopy['features'][0]['properties']['street']
    Gsuburb = dataGeopy['features'][0]['properties']['district']
    Gmunicipality = "municipality is old syntax"
    Gcity = dataGeopy['features'][0]['properties']['city']
    Gcounty = dataGeopy['features'][0]['properties']['county']
    Gstate = dataGeopy['features'][0]['properties']['state']
    Gcountry = dataGeopy['features'][0]['properties']['country']
    Gcodetemp = dataGeopy['features'][0]['properties']['countrycode']
    Gcode = Gcodetemp.lower()
    Gzipcode = dataGeopy['features'][0]['properties']['postcode']
    ################################ write raw data for GEOPY
    pgeopy = '/home/' + homename + ptemp + '-geopy.txt'
    fo = open(pgeopy, 'w')
    fo.write('lat: {}\n'.format(mylat))
    fo.write('lon: {}\n'.format(mylon))
    fo.write('house number: {}\n'.format(Ghousenumber))
    fo.write('road: {}\n'.format(Groad))
    fo.write('suburb: {}\n'.format(Gsuburb))
    fo.write('municipality: {}\n'.format(Gmunicipality))
    fo.write('city: {}\n'.format(Gcity))
    fo.write('state: {}\n'.format(Gstate))
    fo.write('county: {}\n'.format(Gcounty))
    fo.write('country: {}\n'.format(Gcountry))
    fo.write('country_code: {}\n'.format(Gcode))
    fo.write('zip: {}\n'.format(Gzipcode))
    #                   next row writes geopy data as dict
    fo.write('addressraw: {}\n'.format(Glocation.read()))
    fo.close()
    ################################ get data for general current
    cityname = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']
    lat = data['location']['lat']
    lon = data['location']['lon']
    timezone = data['location']['tz_id']
    timezone = timezone + '        '
    et = data['location']['localtime_epoch']
    lt = time.strftime("%d-%B-%Y", time.localtime(et))
    ################################ write general current raw data on a file
    #                   set the path for general today raw data
    pgentodayraw = '/home/' + homename + ptemp + 'wagentodayraw.txt'
    fo = open(pgentodayraw, 'w')
    fo.write('cityname: {}\n'.format(cityname))
    fo.write('region: {}\n'.format(region))
    fo.write('country: {}\n'.format(country))
    fo.write('lat: {}\n'.format(lat))
    fo.write('lon: {}\n'.format(lon))
    fo.write('timezone: {}\n'.format(timezone))
    fo.write('epochtime: {}\n'.format(et))
    fo.write('localtime: {}\n'.format(lt))
    ################################ write general current clean data on a file
    #                   set the path for general today clean data
    pgentodayclean = '/home/' + homename + ptemp + 'wagentodayclean.txt'
    fo = open(pgentodayclean, 'w')
    fo.write('{}\n'.format(cityname))
    fo.write('{}\n'.format(region))
    fo.write('{}\n'.format(country))
    fo.write('{}\n'.format(lat))
    fo.write('{}\n'.format(lon))
    fo.write('{}\n'.format(timezone))
    fo.write('{}\n'.format(et))
    fo.write('{}\n'.format(lt))
    ################################ get data for current
    lue = data['current']['last_updated_epoch']
    lu = data['current']['last_updated']
    tempc = data['current']['temp_c']
    tempf = data['current']['temp_f']
    isday = data['current']['is_day']
    text = data['current']['condition']['text']
    icon = data['current']['condition']['icon']
    code = data['current']['condition']['code']
    windspeedmph = data['current']['wind_mph']
    windspeedkmh = data['current']['wind_kph']
    winddeg = data['current']['wind_degree']
    winddegabb = data['current']['wind_dir']
    pressuremb = data['current']['pressure_mb']
    pressurein = data['current']['pressure_in']
    precipmm = data['current']['precip_mm']
    precipin = data['current']['precip_in']
    humidity = data['current']['humidity']
    clouds = data['current']['cloud']
    tempfeelslikec = data['current']['feelslike_c']
    tempfeelslikef = data['current']['feelslike_f']
    try:
        windchillc = data['current']['windchill_c']
    except:
        windchillc = vtext
    try:
        windchillf = data['current']['windchill_f']
    except:
        windchillf = vtext
    try:
        heatindexc = data['current']['heatindex_c']
    except:
        heatindexc = vtext
    try:
        heatindexf = data['current']['heatindex_f']
    except:
        heatindexf = vtext
    try:
        dewpointc = data['current']['dewpoint_c']
    except:
        dewpointc = vtext
    try:
        dewpointf = data['current']['dewpoint_f']
    except:
        dewpointf = vtext
    viskm = data['current']['vis_km']
    vismh = data['current']['vis_miles']
    uv = data['current']['uv']
    windgustmph = data['current']['gust_mph']
    windgustkmh = data['current']['gust_kph']
    co = data['current']['air_quality']['co']
    co = round(co, 2)
    no2 = data['current']['air_quality']['no2']
    no2 = round(no2, 2)
    o3 = data['current']['air_quality']['o3']
    o3 = round(o3, 2)
    so2 = data['current']['air_quality']['so2']
    so2 = round(so2, 2)
    pm25 = data['current']['air_quality']['pm2_5']
    pm25 = round(pm25, 2)
    pm10 = data['current']['air_quality']['pm10']
    pm10 = round(pm10, 2)
    usepaindex = data['current']['air_quality']['us-epa-index']
    gbdefraindex = data['current']['air_quality']['gb-defra-index']
    ################################ write raw data on a file
    #                   set the path for today raw data
    ptodayraw = '/home/' + homename + ptemp + 'watodayraw.txt'
    fo = open(ptodayraw, 'w')
    fo.write('lastupdatedepoch: {}\n'.format(lue))
    fo.write('lastupdated: {}\n'.format(lu))
    fo.write('tempc: {}\n'.format(tempc))
    fo.write('tempf: {}\n'.format(tempf))
    fo.write('day-night: {}\n'.format(isday))
    fo.write('weathertext: {}\n'.format(text))
    fo.write('icon: {}\n'.format(icon))
    fo.write('code: {}\n'.format(code))
    fo.write('windspeedmph: {}\n'.format(windspeedmph))
    fo.write('windspeedkmh: {}\n'.format(windspeedkmh))
    fo.write('winddeg: {}\n'.format(winddeg))
    fo.write('winddegabb: {}\n'.format(winddegabb))
    fo.write('presmb: {}\n'.format(pressuremb))
    fo.write('presin: {}\n'.format(pressurein))
    fo.write('precipmm: {}\n'.format(precipmm))
    fo.write('precipin: {}\n'.format(precipin))
    fo.write('humidity: {}\n'.format(humidity))
    fo.write('clouds: {}\n'.format(clouds))
    fo.write('tempfeelsc: {}\n'.format(tempfeelslikec))
    fo.write('tempfeelsf: {}\n'.format(tempfeelslikef))
    fo.write('viskm: {}\n'.format(viskm))
    fo.write('vismph: {}\n'.format(vismh))
    fo.write('uvindex: {}\n'.format(uv))
    fo.write('windgustmph: {}\n'.format(windgustmph))
    fo.write('windgustkmh: {}\n'.format(windgustkmh))
    fo.write('co: {}\n'.format(co))
    fo.write('no2: {}\n'.format(no2))
    fo.write('o3: {}\n'.format(o3))
    fo.write('so2: {}\n'.format(so2))
    fo.write('pm2-5: {}\n'.format(pm25))
    fo.write('pm10: {}\n'.format(pm10))
    fo.write('us-epa-index: {}\n'.format(usepaindex))
    fo.write('gb-defra-index: {}\n'.format(gbdefraindex))
    fo.write('windchillc: {}\n'.format(windchillc))
    fo.write('windchillf: {}\n'.format(windchillf))
    fo.write('heatindexc: {}\n'.format(heatindexc))
    fo.write('heatindexf: {}\n'.format(heatindexf))
    fo.write('dewpointc: {}\n'.format(dewpointc))
    fo.write('dewpointf: {}\n'.format(dewpointf))
    fo.close()
    ################################ write clean data on a file
    #                   set the path for general current clean data
    ptodayclean = '/home/' + homename + ptemp + 'watodayclean.txt'
    fo = open(ptodayclean, 'w')
    fo.write('{}\n'.format(lue))
    fo.write('{}\n'.format(lu))
    fo.write('{}\n'.format(tempc))
    fo.write('{}\n'.format(tempf))
    fo.write('{}\n'.format(isday))
    fo.write('{}\n'.format(text))
    fo.write('{}\n'.format(icon))
    fo.write('{}\n'.format(code))
    fo.write('{}\n'.format(windspeedmph))
    fo.write('{}\n'.format(windspeedkmh))
    fo.write('{}\n'.format(winddeg))
    fo.write('{}\n'.format(winddegabb))
    fo.write('{}\n'.format(pressuremb))
    fo.write('{}\n'.format(pressurein))
    fo.write('{}\n'.format(precipmm))
    fo.write('{}\n'.format(precipin))
    fo.write('{}\n'.format(humidity))
    fo.write('{}\n'.format(clouds))
    fo.write('{}\n'.format(tempfeelslikec))
    fo.write('{}\n'.format(tempfeelslikef))
    fo.write('{}\n'.format(viskm))
    fo.write('{}\n'.format(vismh))
    fo.write('{}\n'.format(uv))
    fo.write('{}\n'.format(windgustmph))
    fo.write('{}\n'.format(windgustkmh))
    fo.write('{}\n'.format(co))
    fo.write('{}\n'.format(no2))
    fo.write('{}\n'.format(o3))
    fo.write('{}\n'.format(so2))
    fo.write('{}\n'.format(pm25))
    fo.write('{}\n'.format(pm10))
    fo.write('{}\n'.format(usepaindex))
    fo.write('{}\n'.format(gbdefraindex))
    fo.write('{}\n'.format(windchillc))
    fo.write('{}\n'.format(windchillf))
    fo.write('{}\n'.format(heatindexc))
    fo.write('{}\n'.format(heatindexf))
    fo.write('{}\n'.format(dewpointc))
    fo.write('{}\n'.format(dewpointf))
    fo.close()
    ################################ create FLAG path
    #                   set the path for the FLAGS
    pflags = home + homename + ptemp + 'flags.txt'
    pi = '${image ' + home
    pi2 = homename
    pi3 = conky + 'flags/'
    pf = '.png -p 381,0 -s 19x13}'
    Gcode = Gcode.lower()
    tot = pi + pi2 + pi3 + Gcode + pf
    if Gcode == vtext:
       fo = open(pflags, 'w')
       tot = 'transparent'
       fo.write('{}\n'.format(tot))
    elif Gcode != vtext:
       fo = open(pflags, 'w')
       fo.write('{}\n'.format(tot))
    fo.close()
    ################################ create the path for weatherapi logo
    #                   set the path for the Weatherapi logo
    pwblogo = home + homename + ptemp + 'walogo.txt'
    pi = '${image ' + home
    pi2 = homename
    pi3 = defconkyfol + 'walogo2'
    est = '.png -p '
    x = 100
    virg = ','
    y = 0
    pf = ' -s 15x15}'
    fo = open(pwblogo, 'w')
    tot = pi + pi2 + pi3 + est + str(x) + virg + str(y) + pf
    fo.write('{}\n'.format(tot))
    fo.close()
    ################################ write the path for COMPASS icon
    #                   set the paths for the compass
    parrow = home + homename + conky + 'weather/compass/arrow.png'
    parrow2 = home + homename + conky + 'weather/compass/arrow2.png'
    parrowt = home + homename + conky + 'weather/compass/arrowt.png'
    parrowt2 = home + homename + conky + 'weather/compass/arrowt2.png'
    pcompass = home + homename + ptemp + 'todaycompass.txt'
    pathwindrose = '${image $HOME' + conky + 'weather/compass/windsrose.png -p 305,50 -s 100x100}'
    #                  grades calculation for winddeg, trasparent image if no wind (use negative tdeg to rotate clockwise)
    if winddeg == 'empty':
        tdeg = myd
        temp1 = Image.open(parrowt)
        temp2 = temp1.rotate(-tdeg)
        temp2.save(parrowt2)
        temp3 = '${image ' + home
        temp4 = homename
        temp5 = conky + 'weather/compass/arrowt2'
        pfcomp = '.png -p 305,50 -s 100x100}'
        totcomp = temp3 + temp4 + temp5 + pfcomp
        fo = open(pcompass, 'w')
        fo.write('{}\n'.format(totcomp))
        fo.write('{}\n'.format(pathwindrose))
    elif winddeg != 'empty':
        tdeg = myd + winddeg
        temp1 = Image.open(parrow)
        temp2 = temp1.rotate(-tdeg)
        temp2.save(parrow2)
        temp3 = '${image ' + home
        temp4 = homename
        temp5 = conky + 'weather/compass/arrow2'
        pfcomp = '.png -p 305,50 -s 100x100}'
        totcomp = temp3 + temp4 + temp5 + pfcomp
        fo = open(pcompass, 'w')
        fo.write('{}\n'.format(totcomp))
        fo.write('{}\n'.format(pathwindrose))
    fo.close()
    ################################ calculate today UV index color and write it
    #                   set the path for today uv index
    puvindex = home + homename + ptemp + 'todaywauvindex.txt'
    value = uv
    if (value >=0 and value < 3):
        color = 6
    elif (value >=3 and value < 6):
        color = 9
    elif (value >=6 and value < 8):
        color = 3
    elif (value >=8 and value < 11):
        color = 4
    elif (value >= 11):
        color = 0
    else:
        color = 2
    fo = open(puvindex, 'w')
    fo.write('{}\n'.format(value))
    fo.write('{}\n'.format(color))
    fo.close()
    ################################ calculate today AQI color and write it
    #                   set the path for today aqi
    paqi = home + homename + ptemp + 'todaywaaqi.txt'
    value = usepaindex
    if value == 1:
        color = 6
    elif value == 2:
        color = 9
    elif value == 3:
        color = 3
    elif value == 4:
        color = 4
    elif value == 5:
        color = 0
    elif value == 6:
        color = 1
    fo = open(paqi, 'w')
    fo.write('{}\n'.format(value))
    fo.write('{}\n'.format(color))
    fo.close()
    ################################ write main icon path
    #                   set the path for today main icon
    ptodaymainicon = home + homename + ptemp + 'todayicon.txt'
    icon = (icon[5:-4])
    icon = (icon[-3:])
    pi = '${image ' + home
    pi2 = homename
    pi3 = conky + 'weather/Weatherapi/icons/day/'
    pi4 = conky + 'weather/Weatherapi/icons/night/'
    icontemp = isday
    if icontemp == 1:
        icontemp = 'd'
    elif icontemp == 0:
        icontemp = 'n'
    pf = '.png -p 0,30 -s 120x120}'
    fo = open(ptodaymainicon, 'w')
    if icontemp == 'd':
        tot = pi + pi2 + pi3 + str(icon) + pf
        fo.write('{}\n'.format(tot))
    elif icontemp == 'n':
        tot = pi + pi2 + pi4 + str(icon) + pf
        fo.write('{}\n'.format(tot))
    fo.close()
    ################################ write icon HOT path
    #                   set the path for HOT icon
    photicon = home + homename + ptemp + 'todayiconhot.txt'
    fo = open(photicon, 'w')
    pi = '${image ' + home
    pi2 = homename
    pi3 = conky + 'weather/Weatherapi/icons/'
    pf = '.png -p 240,70 -s 85x51}'
    if tempfeelslikec >= 38:
        temp = 'hot'
        tot = pi + pi2 + pi3 + temp + pf
        fo.write('{}\n'.format(tot))
    else:
        temp = 'transparent'
        tot = pi + pi2 + pi3 + temp + pf
        fo.write('{}\n'.format(tot))
    fo.close()
    ################################ write icon COLD path
    #                   set the path for COLD icon
    pcoldicon = home + homename + ptemp + 'todayiconcold.txt'
    fo = open(pcoldicon, 'w')
    pi = '${image ' + home
    pi2 = homename
    pi3 = conky + 'weather/Weatherapi/icons/'
    if tempfeelslikec <= 0:
        temp = 'cold'
        tot = pi + pi2 + pi3 + temp + pf
        fo.write('{}\n'.format(tot))
    else:
        temp = 'transparent'
        tot = pi + pi2 + pi3 + temp + pf
        fo.write('{}\n'.format(tot))
    fo.close()
    ################################ create CURRENT, section
    #                   set the path for the TODAY conky section
    pathtodayconky = home + homename + ptemp + 'todayconky.txt'
    #                 main CURRENT in todayconky.txt
    pathtemp = "$HOME" + defconkyfol + "today/"
    pathtemp2 = "$HOME" + defconkyfol
    wbpylogo = '${image ' + pathtemp2 + 'python_logo.png -p 120,0 -s 15x15}'
    infotz = "${color2}${font URW Gothic L:size=8}        WEATHERAPI${font}${color1}${alignr}${execpi 900 sed -n '6p' " + pathtemp + "wagentodayraw.txt}"
    infotzerr = "${color2}${font URW Gothic L:size=8}WEATHERAPI     ${color4}HTTP STATUS CODE ERROR: " + str(status_code) + "${font}${color1}${alignr}${execpi 900 sed -n '6p' " + pathtemp + "wagentodayraw.txt}"
    latlon = "${alignr}(${execpi 900 sed -n '4p' " + pathtemp + "wagentodayraw.txt} - ${execpi 900 sed -n '5p' " + pathtemp + "wagentodayraw.txt})${font}${color}"
    curricon = "${execpi 900 sed -n '1p' " + pathtemp + "todayicon.txt}"
    firstdesc = "${color4}${goto 190}${execpi 900 sed -n '6p' " + pathtemp + "watodayclean.txt}${color}"
    currtemp = "${color}${goto 190}temp: ${execpi 900 sed -n '3p' " + pathtemp + "watodayclean.txt}${color}°C"
    currtempf = "${goto 190}(feel: ${execpi 900 sed -n '19p' " + pathtemp + "watodayclean.txt}°C)"
    thermo = "${execpi 900 sed -n '1p' " + pathtemp + "todayiconhot.txt}${execpi 900 sed -n '1p' " + pathtemp + "todayiconcold.txt}"
    raininfo = "${color}${goto 190}rain/h: ${execpi 900 sed -n '15p' " + pathtemp + "watodayclean.txt}mm"
    winds = "${color}${goto 190}wind speed: ${execpi 900 sed -n '10p' " + pathtemp + "watodayclean.txt} Km/h"
    windg = "${color}${goto 190}wind gust: ${execpi 900 sed -n '25p' " + pathtemp + "watodayclean.txt} Km/h"
    info1 = "${color2}HUMIDITY: $color${execpi 900 sed -n '17p' " + pathtemp + "watodayclean.txt}%${goto 260}${color2}PRESSURE: $color${execpi 900 sed -n '13p' " + pathtemp + "watodayclean.txt}mb"
    info2 = "${color2}UV INDEX (${color6}0${color2}-${color0}11+${color2}): ${eval $${color${execpi 900 sed -n '2p' " + pathtemp + "todaywauvindex.txt}}}${execpi 900 sed -n '1p' " + pathtemp + "todaywauvindex.txt}${goto 260}${color2}PRESSURE: $color${execpi 900 sed -n '14p' " + pathtemp + "watodayclean.txt}in"
    info4 = "${color2}CLOUDS COVER: $color${execpi 900 sed -n '18p' " + pathtemp + "watodayclean.txt}%${goto 260}${color2}AQI (${color6}1${color2}-${color8}6${color2}): ${eval $${color${execpi 900 sed -n '2p' " + pathtemp + "todaywaaqi.txt}}}${execpi 900 sed -n '1p' " + pathtemp + "todaywaaqi.txt}"
    info6= "${color2}CO: $color${execpi 900 sed -n '26p' " + pathtemp + "watodayclean.txt} μg/m3${color2}${goto 260}SO2: $color${execpi 900 sed -n '29p' " + pathtemp + "watodayclean.txt} μg/m3${color}"
    info7= "${color2}NO2: $color${execpi 900 sed -n '27p' " + pathtemp + "watodayclean.txt}μg/m3${color2}${goto 260}PM2.5: $color${execpi 900 sed -n '30p' " + pathtemp + "watodayclean.txt} μg/m3${color}"
    info8= "${color2}O3: $color${execpi 900 sed -n '28p' " + pathtemp + "watodayclean.txt}μg/m3${color2}${goto 260}PM10: $color${execpi 900 sed -n '31p' " + pathtemp + "watodayclean.txt} μg/m3${color}"
    #dashedline = "${alignc}-------------------------------------------------------------------------------------------"
    fo = open(pathtodayconky, 'w')
    if status_code != 200:
        fo.write('{}\n'.format(wbpylogo + infotzerr))
    else:
        fo.write('{}\n'.format(wbpylogo + infotz))
        fo.write('{}\n'.format(latlon))
        fo.write('{}\n'.format(firstdesc))
        fo.write('{}\n'.format(currtemp))
        fo.write('{}\n'.format(currtempf + thermo))
        fo.write('{}\n'.format(raininfo))
        fo.write('{}\n'.format(winds))
        fo.write('{}\n'.format(windg))
        fo.write('{}\n'.format(info1))
        fo.write('{}\n'.format(info2))
        fo.write('{}\n'.format(info4))
        fo.write('{}\n'.format(info6))
        fo.write('{}\n'.format(info7))
        fo.write('{}\n'.format(info8))
        #fo.write('{}\n'.format(dashedline))
    fo.close()
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed