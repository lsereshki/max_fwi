'''
to find max FWI on a day in 2022 in "FWI_FENZ_NOV2022-MAY2023.nc"

(this file is in this directory: /mnt/data3/Bottle_Lake/FWI)

1) ncdump -h FWI_FENZ_NOV2022-MAY2023.nc

time = 174 , since "2022 / 11 / 24 "  ----> 38 days in 2022 from index 0 to index 37.

!!! Because of there are a few days (just 38), a simple manual script answers here to find the day with highest fwi. !!!

2) ncdump -v fwi FWI_FENZ_NOV2022-MAY2023.nc > highestfwi.txt

just select the first 38 fwi data, copy & paste in a txt file.

3)a python script to find the max value:

'''

data = [0.03911087, 0.3012013, 0.8093393, 0.8630512, 1.418867, 3.049367,
    3.841439, 4.823643, 4.989804, 5.145607, 5.845535, 4.058474, 5.620821,
    5.7239, 6.932714, 4.482241, 12.99771, 10.62719, 7.054913, 6.218336,
    9.493385, 5.501343, 5.421355, 6.055143, 1.91745, 2.694818, 3.577439,
    5.279019, 5.321653, 5.787808, 6.577081, 6.820519, 6.704732, 6.015117,
    6.943768, 8.910357, 8.743788, 9.476202]

max_value = max(data)
print(max_value)  

''' 

max value would be 12.99771 corresponds to index 16 or 17 days from 24 / 11 / 2022.

this day is 10 / 12 / 2022.

'''