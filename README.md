# seersNightLight

SDG 11

Our goal is to anaylze the impact COVID-19 has made on our society by looking at the 
progress of the UN's Sustainable Developement Goals. In particular, our team is focused
on SDG 11: Sustainable Cities and Communities.

## syntax and process
```
$ python analyzeNightLight.py [file1] [file2] ...

#example
$ python analyzeNightLight.py hubei_vir_2020019.png hubei_vir_2020035.png
hubei_vir_2020019.png has 8.166% illuminated
hubei_vir_2020035.png has 7.627% illuminated

```

![Hubei January](hubei_vir_2020019.png)

Above is the preprocessed image of Wuhan, China on January 19, 2020. Using
OpenCV, the image is processed to remove noise and isolate the significant
areas of brightness. Then, PIL is used to iterate through each pixel to find
the percentage of luminescence in the image.

![Hubei January Processed](hubei_vir_2020019_cleaned.png)
