import requests
from models import StackOverflowTagsInfo


class StackExchangeInfo(object):
    """
    Uses StackExchange API to fetch data from its sites
    """
    def __init__(self):
        self.base_url = 'https://api.stackexchange.com/2.2/'
        self.site = 'stackoverflow'

    def get_tag_info(self):
        """
        Fetch data from StackOverflow: tags,
        post count and unanswered post count
        """
        try:
            tags_url = '{0}/tags'.format(self.base_url)
            params = {'order': 'desc', 'sort': 'popular', 'site': self.site,
                      'pagesize': 50}
            resp = requests.get(tags_url, params=params)

            data = resp.json()
            items = data['items']
            tag_dict = {}
            for item in items:
                tag = item['name']
                post_count = item['count']

                unanswered_url = '{0}/questions/unanswered'.format(self.base_url)
                item_params = {'site': self.site, 'filter': 'total', 'tagged': tag}
                r = requests.get(unanswered_url, params=item_params)
                unanswered_count = r.json()['total']

                tag_dict['tag'] = tag
                tag_dict['post_count'] = post_count
                tag_dict['unanswered_count'] = unanswered_count

                so_tag_info = StackOverflowTagsInfo(**tag_dict)
                so_tag_info.save()

        except Exception as e:
            raise e

if __name__ == '__main__':
    pass
