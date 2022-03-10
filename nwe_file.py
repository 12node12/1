import urllib.request
import os
import requests
base_url='https://www.mybidfood.com.au/api/s_v1/Image/GetImage/'
print(base_url)
print('all done')
for i in range(1,100):
    image_id=str(62167)+ str(i)
    print(image_id)

    full_url='https://www.mybidfood.com.au/api/s_v1/Image/GetImage/'+image_id

    print(full_url)
    image_name='fulldata/'+image_id+'.jpg'

    page = requests.get(full_url)
    # print(page.content)

    # urllib.request.urlretrieve(full_url, image_name)
    with open(image_name, 'wb') as f:
        f.write(page.content)




# url = 'https://www.mybidfood.com.au/api/s_v1/Image/GetImage/6216741'
# page = requests.get(url)
#
# f_ext = os.path.splitext(url)[-1]
# f_name = 'img{}'.format(f_ext)
# with open(f_name, 'wb') as f:
#     f.write(page.content)
