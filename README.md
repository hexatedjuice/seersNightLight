# seersNightLight

SDG 11

Our, the [sustainableSeers'](https://sfwang.wixsite.com/mysite), goal is to anaylze the impact COVID-19 has made on our society by looking at the progress of the UN's Sustainable Developement Goals. In particular, our team is focused
on SDG 11: Sustainable Cities and Communities.


## Data and Conclusions

![Illumination in Impacted Cities](illuminationChart.png)

* a list of dates can be found on our [website](https://sfwang.wixsite.com/mysite)
* images of night radience were provided by [NOAA (NCIE) VIIRS DNB Nighttime Imagery](https://ngdc.noaa.gov/eog/viirs/download_dnb_composites.html)
  - images were scraped via the provided REST API powered by ArcGIS

City|Initial Illumination (% area)|Final Illumination (% area)| Delta
---|---|---|---
New York|11.280|10.380|-0.900
Atlanta|8.266|7.895|-0.372
Delhi|11.190|8.141|-3.049
Seoul|12.620|12.350|-0.527
Lombardy|16.040|16.530|+0.490

Standard Deviation of Delta: 1.0063563186069

In general, the amount of illumination in cities bearing the brunt of the
COVID-19 pandemic decreased. Our team believes this is due to the policies
implemented by governments for quarantine. A lockdown induces a decrease in the
number of people who go outside for shopping, vacations, and/or work. 


## syntax and process
```
$ python analyzeNightLight.py [file1] [file2] ...

#example
$ python analyzeNightLight.py febNy.png 
febNy.png has 11.280% illuminated

```

![New York in February](febNy.png)

Above is the preprocessed image of Wuhan, China on January 19, 2020. Using
OpenCV, the image is processed to remove noise and isolate the significant
areas of brightness. OpenCV is content aware and can thus outline the most prominent light pixels. 
Then, PIL is used to iterate through each pixel to find
the percentage of luminescence in the image.

![New York in February processed](febNy_cleaned.png)
