
# THIS FILE IS RESPONSIBLE FOR THE CONSTRUCTION OF DYNAMIC URLS


# PREFIXES
QUERRY_PREFIX = 'q='
TYPES_PREFIX = 'type='
MARKET_PREFIX = 'market='
LIMIT_PREFIX = 'limit='
OFFSET_PREFIX = 'offset='


def search_endpoint(keywords:str, types:list, filters:dict, market:str, limit:int, offset:int):
    
    endpoint = 'https://api.spotify.com/v1/search?'
    querry_keywords = keywords.split() 
    
    for filter, value in filters.items():
        value = value.replace(' ', '%20')
        querry_keywords.append('{0}:{1}'.format(filter, value))
    
    querry_str = QUERRY_PREFIX + '%20'.join(querry_keywords)  
    market_str = MARKET_PREFIX + str(market)
    offset_str = OFFSET_PREFIX + str(offset)
    types_str = TYPES_PREFIX + ','.join(types)
    limit_str = LIMIT_PREFIX + str(limit)

    url_arguments = [
        querry_str, 
        market_str, 
        offset_str,
        types_str, 
        limit_str 
    ]    
    
    url = endpoint + '&'.join(url_arguments)
    
    return url
