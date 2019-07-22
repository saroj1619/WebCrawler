from rest_framework.views import APIView
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
import urllib.request
import re


# Create your views here.
class WebCrawlerView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        try:
            extracted_data = []
            visited_url = []
            data = []
            main_url = request.data.get('url')
            url = request.data.get('url')
            depth = request.data.get('depth')
            flag = request.data.get('flag')

            # Block to extract URLs
            if flag == 0:
                pass

                count = 0

                HTML_TAG_REGEX = re.compile(r'<a[^<>]+?href=([\'\"])(.*?)\1', re.IGNORECASE)

                for iterator in range(depth):
                    if iterator < 1:
                        temp_list = []
                        fp = urllib.request.urlopen(url)
                        mybytes = fp.read()

                        mystr = mybytes.decode("utf8")
                        fp.close()

                        for match in HTML_TAG_REGEX.findall(mystr):
                            temp_url = match[1]

                            if temp_url[0] == '/' or main_url in temp_url:
                                temp_list.append(temp_url)
                            else:
                                continue

                        visited_url.append(url)
                        count += 1
                        extracted_data.append(list(set(temp_list)))

                    else:

                        l_list = extracted_data[iterator - 1]
                        temp_list = []
                        for i in l_list:
                        # for i in [x for x in l_list if x not in visited_url]:
                            if i[0] == '/' and len(i) > 2:
                                url = main_url + i
                            elif i[0] == '/' and i[1] == '/':
                                url = "https:" + i
                            else:
                                url = i

                            if url not in visited_url:
                                fp = urllib.request.urlopen(url)
                                mybytes = fp.read()

                                mystr = mybytes.decode("utf8")
                                fp.close()

                                for match in HTML_TAG_REGEX.findall(mystr):
                                    temp_url = match[1]

                                    if temp_url[0] == '/' or main_url in temp_url:
                                        temp_list.append(temp_url)
                                    else:
                                        continue

                                visited_url.append(url)
                                count += 1
                        extracted_data.append(list(set(temp_list)))


                # print(count)
                # print(visited_url)

                return HttpResponse(json.dumps(extracted_data, cls=DjangoJSONEncoder), content_type='application/json', status=200)

            # Block to extract Image links
            elif flag == 1:
                extracted_imgs = []
                temp =[]
                fp = urllib.request.urlopen(url)
                mybytes = fp.read()

                mystr = mybytes.decode("utf8")
                fp.close()

                IMG_TAG_REGEX = re.compile(r'<img[^<>]+?src=([\'\"])(.*?)\1')

                for match in IMG_TAG_REGEX.findall(mystr):
                    temp.append(match[1])

                extracted_imgs.append(list(set(temp)))
                return HttpResponse(json.dumps(extracted_imgs, cls=DjangoJSONEncoder), content_type='application/json',
                                    status=200)

        except:
            error = {
                "msg": "Error in fetching results."
            }

            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)
